# 把当前 APK 发布为 GitHub Release，供应用内检查更新和分发
# 用法: python publish_release.py [更新说明]
# 前提: 项目根目录有 .github_token (PAT) 和 .github_repo (如 yourname/letit)
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))

token = open(os.path.join(ROOT, ".github_token"), encoding="utf-8").read().strip()
repo = open(os.path.join(ROOT, ".github_repo"), encoding="utf-8").read().strip()
ver = re.search(r'versionName "([^"]+)"',
                open(os.path.join(ROOT, "android/app/build.gradle"), encoding="utf-8").read()).group(1)
apk = os.path.join(ROOT, "android/app/build/outputs/apk/debug/app-debug.apk")

# 校验包内 APP_VERSION 与 versionName 一致，防止把旧版本号的包发出去
import zipfile
try:
    zhtml = zipfile.ZipFile(apk).read("assets/public/index.html").decode("utf-8")
    mver = re.search(r'const APP_VERSION = "([^"]*)"', zhtml)
    in_apk = mver.group(1) if mver else None
except Exception:
    in_apk = None
if in_apk != ver:
    print("中止：APK 内 APP_VERSION(%s) 与 versionName(%s) 不一致，请重新构建再发布" % (in_apk, ver))
    sys.exit(1)

note = sys.argv[1] if len(sys.argv) > 1 else "修复与体验优化"
tag = "v" + ver
name = "letit-v%s.apk" % ver


def git(*args):
    import base64
    auth = base64.b64encode(("x-access-token:" + token).encode()).decode()
    header = "Authorization: Basic " + auth
    env = dict(os.environ)
    env["GIT_TERMINAL_PROMPT"] = "0"
    cmd = ["git", "-c", "http.extraheader=" + header, *args]
    r = subprocess.run(cmd, cwd=ROOT, env=env,
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if r.returncode != 0:
        out = r.stdout.decode("utf-8", "ignore").replace(header, "***")
        print("git 命令失败: git " + " ".join(args) + "\n" + out)
        sys.exit(1)


# 先把最新源码推上去，让 Release 标签落在最新提交上
git("add", "-A")
if subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=ROOT).returncode != 0:
    git("commit", "-m", "release %s: %s" % (tag, note))
git("push", "origin", "main")
print("源码已同步到 main")


def api(url, data=None, headers=None, is_json=True):
    body = json.dumps(data, ensure_ascii=True).encode("utf-8") if (data is not None and is_json) else data
    req = urllib.request.Request(url, data=body)
    req.add_header("Authorization", "Bearer " + token)
    req.add_header("Accept", "application/vnd.github+json")
    for k, v in (headers or {}).items():
        req.add_header(k, v)
    with urllib.request.urlopen(req) as r:
        raw = r.read()
        return json.loads(raw) if raw else {}


try:
    rel = api("https://api.github.com/repos/%s/releases" % repo, data={
        "tag_name": tag, "name": "Letit " + tag, "body": note})
    print("已创建发布:", tag)
except urllib.error.HTTPError as e:
    if e.code == 422:  # 该版本已发布过，向现有 Release 补传
        rel = api("https://api.github.com/repos/%s/releases/tags/%s" % (repo, tag))
        print("发布已存在，补传 APK:", tag)
    else:
        print("创建发布失败:", e.code, e.read().decode("utf-8", "ignore")[:300])
        sys.exit(1)

upload_url = rel["upload_url"].split("{")[0]
try:
    api(upload_url + "?name=" + name, data=open(apk, "rb").read(),
        headers={"Content-Type": "application/vnd.android.package-archive"}, is_json=False)
    print("APK 已上传:", name)
except urllib.error.HTTPError as e:
    if e.code == 422:
        print("同名 APK 已存在，跳过上传（如需更新请先到 GitHub 网页删除该文件）")
    else:
        print("上传失败:", e.code, e.read().decode("utf-8", "ignore")[:300])
        sys.exit(1)

print("下载页: https://github.com/%s/releases/tag/%s" % (repo, tag))
