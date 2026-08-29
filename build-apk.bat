@echo off
chcp 65001 >nul
setlocal
set "ADB=%~dp0_android-sdk\platform-tools\adb.exe"
set "APK=%~dp0android\app\build\outputs\apk\debug\app-debug.apk"

echo ========================================
   Letit APK 构建脚本
echo ========================================
echo.

cd /d "%~dp0"

echo [1/6] versionCode 自增（保证可覆盖安装）...
python bump_version.py
if errorlevel 1 (
    echo [错误] versionCode 更新失败，请确认已安装 Python
    pause
    exit /b 1
)

echo.
echo [2/6] 同步网页源码到打包目录...
copy /Y "%~dp0index5.0.html" "%~dp0www\index.html" >nul
if errorlevel 1 (
    echo [错误] 复制失败
    pause
    exit /b 1
)

echo.
echo [3/6] 同步 web 资源到 android 工程...
call npx cap sync android
if errorlevel 1 (
    echo [错误] 资源同步失败
    pause
    exit /b 1
)

echo.
echo [4/6] 编译 APK...
cd android
call gradlew.bat assembleDebug
if errorlevel 1 (
    echo [错误] 编译失败
    cd ..
    pause
    exit /b 1
)
cd ..

echo.
echo [5/6] 检查手机连接...
"%ADB%" devices | findstr /C:"unauthorized" >nul
if not errorlevel 1 (
    echo 手机已连接但未授权：请在手机上点“允许 USB 调试”后重跑本脚本
    pause
    exit /b 1
)
"%ADB%" devices | findstr /R "device$" >nul
if errorlevel 1 (
    echo 未检测到手机，跳过安装。
) else (
    echo 检测到手机，自动安装中...
    "%ADB%" install -r "%APK%"
    if errorlevel 1 (
        echo [错误] 安装失败，请检查手机屏幕上的弹窗
        pause
        exit /b 1
    )
)

echo.
echo [6/6] 发布到 GitHub...
if not exist "%~dp0.github_token" (
    echo 未配置 .github_token，跳过发布（APK 在：%APK%）
    goto done
)
choice /C YN /N /M "是否发布新版本到 GitHub 供大家更新？[Y/N]"
if errorlevel 2 goto done
python publish_release.py "%~1"
if errorlevel 1 (
    echo [错误] 发布失败
    pause
    exit /b 1
)

:done
echo.
echo 完成！
pause
