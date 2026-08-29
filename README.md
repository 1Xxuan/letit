# Letit

基于「圣多纳释放法」的中文自我练习应用（Android，Capacitor 封装）。

## 下载

- 最新版：https://github.com/1Xxuan/letit/releases/latest
- 下载 APK 直接安装（首次需允许"安装未知应用"）
- 应用内置自动检查更新，有新版本时打开会提示

## 功能

- 释放练习流程引导（含「没什么感受」问句包）
- AI 引导师：可接入 DeepSeek / 智谱 / Moonshot / SiliconFlow 等（使用自己的 API Key，仅存本地）
- 语音朗读：系统 TTS / SiliconFlow / Qwen TTS / Kokoro 本地部署
- 云同步备份：WebDAV（坚果云等）/ S3 兼容存储
- 语录收藏、目标与收获记录

## 从源码构建

需要：Node.js、Python 3、JDK 17+、Android SDK（含 platform 36 / build-tools 35+）。

```bat
npm install
copy index5.0.html www\index.html
npx cap sync android
cd android && gradlew.bat assembleDebug
```

构建产物在 `android\app\build\outputs\apk\debug\app-debug.apk`。

## 技术

Capacitor 8 + Android WebView，单文件 Web 应用；正文字体为 [霞鹜文楷](https://github.com/lxgw/LxgwWenKai)（SIL OFL 1.1）。

## 声明

本项目仅供个人学习与自我练习，不构成任何心理治疗建议；与圣多纳释放法原方法及其作者无关。

## License

MIT
