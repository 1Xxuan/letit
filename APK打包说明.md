# 圣多纳释放法 - APK 打包指南

## 方法一：使用 Android Studio（推荐）

### 1. 安装 Android Studio
下载地址：https://developer.android.com/studio

### 2. 打开项目
1. 打开 Android Studio
2. 选择 "Open an Existing Project"
3. 选择 `android` 文件夹

### 3. 构建 APK
1. 等待 Gradle 同步完成
2. 菜单 → Build → Build Bundle(s) / APK(s) → Build APK(s)
3. 构建完成后点击通知栏的 "locate" 找到 APK

### 4. APK 位置
```
android\app\build\outputs\apk\debug\app-debug.apk
```

---

## 方法二：使用命令行

### 前提条件
- 已安装 Android Studio 或 Android SDK
- 已设置 ANDROID_HOME 环境变量

### 构建步骤
```batch
cd android
gradlew.bat assembleDebug
```

---

## 方法三：在线打包

如果不想安装 Android Studio，可以使用在线工具：

1. **PWABuilder** - https://www.pwabuilder.com/
   - 上传 index5.0.html
   - 选择 Android 平台
   - 下载 APK

2. **HTML一键打包APK工具**
   - 下载地址：https://html2apk.leapever.com/
   - 选择本地项目文件夹
   - 配置应用信息后打包

---

## 应用信息
- 应用名称：圣多纳释放法
- 包名：com.sedona.release
- 版本：5.0
- 最低支持：Android 7.0 (API 24)

---

## 自定义图标

将图标文件放到以下位置：
```
android\app\src\main\res\mipmap-hdpi\ic_launcher.png
```

推荐尺寸：72x72 像素
