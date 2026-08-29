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
html = open(htmlp, encoding="utf-8").read()
m2 = re.search(r'const APP_VERSION = "([^"]*)"', html)
if m2:
    html = html[:m2.start()] + f'const APP_VERSION = "{name}"' + html[m2.end():]
    open(htmlp, "w", encoding="utf-8", newline="").write(html)
    print(f"versionCode -> {code}, versionName -> {name} (APP_VERSION 已同步)")
else:
    print(f"versionCode -> {code}, versionName -> {name} (未找到 APP_VERSION 常量)")
