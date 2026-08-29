# 每次构建前自动递增版本号，保证 APK 可覆盖安装
# versionName 按 1.0 -> 1.0.1 -> 1.0.2 递增（功能大版本手动改）
# versionCode 同步 +1（安卓覆盖安装只认这个）
# 并同步 index5.0.html 里的 APP_VERSION 显示值
import re

path = "android/app/build.gradle"
src = open(path, encoding="utf-8").read()

m = re.search(r"versionCode (\d+)", src)
if not m:
    raise SystemExit("versionCode not found")
code = int(m.group(1)) + 1
src = src[:m.start()] + f"versionCode {code}" + src[m.end():]

m = re.search(r'versionName "([\d.]+)"', src)
if not m:
    raise SystemExit('versionName not found')
parts = m.group(1).split(".")
while len(parts) < 3:
    parts.append("0")
parts[2] = str(int(parts[2]) + 1)   # 1.0 -> 1.0.1 -> 1.0.2
name = ".".join(parts)
src = src[:m.start()] + f'versionName "{name}"' + src[m.end():]
open(path, "w", encoding="utf-8", newline="").write(src)

htmlp = "index5.0.html"
old_const = 'const APP_VERSION = "'
new_const = f'const APP_VERSION = "{name}"'
for f in (htmlp, "www/index.html"):
    try:
        html = open(f, encoding="utf-8").read()
    except FileNotFoundError:
        continue
    i = html.find(old_const)
    if i < 0:
        continue
    j = html.index('"', i + len(old_const)) + 1
    html = html[:i] + new_const + html[j:]
    open(f, "w", encoding="utf-8", newline="").write(html)
print(f"versionCode -> {code}, versionName -> {name} (APP_VERSION 已同步到 index5.0.html 和 www/index.html)")
