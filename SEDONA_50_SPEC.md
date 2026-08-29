# Sedona 5.0 — 从 4.0 到 5.0 完整功能文档

## 一、4.0 已有功能清单（必须全部保留）

### 1. 页面结构
| 页面 | 功能 | 状态 |
|---|---|---|
| **首页** | 智慧语录（随机/切换/管理）、连续天数徽章、被触发主题快捷入口、三个入口卡片（智能引导陪练/目标释放/根本欲望识别） | ✅ 完整 |
| **练习页** | 3 个子标签：陪练(m6)、目标(m2)、欲望(m3) | ✅ 完整 |
| **记录页** | 2 个子标签：收获本(gains)、速查(quickref) | ✅ 完整 |
| **设置页** | 练习统计、语录管理、问句包管理、数据管理（导出/导入/清除） | ✅ 完整 |

### 2. 智能引导陪练引擎（m6）— 核心
- **开场**：收回注意力 → 3 个入口（能描述/模糊/被触发）
- **归类情绪**：9 种 AGFLAPCAP 情绪，三组分层（低层/中层/高层）
- **释放循环**：三问句（能放吗/愿意吗/什么时候）→ 分支处理 → 感受确认
- **模糊分支**：逐条对照辨认 9 种情绪
- **卡住处理**：觉察卡住 → 想要改变 → 释放
- **抗拒释放层**：识别抗拒类型 → 释放背后的想要
- **安全阀**：多次拒绝后温柔退出
- **主题深挖**：同一主题多层释放
- **目标释放模式**：在陪练内直接释放目标
- **结束后推荐**：智能推荐下一步

### 3. 目标释放引擎（m2）
- **目标创建**：现在时写目标
- **目标表格**：正面感受 + 背面行动步骤
- **释放流程**：感受输入 → 三问句逐条释放
- **喜欢/不喜欢释放**：交替释放，创造流动
- **行动翻面**：双向阻力检查（想要做 vs 想要保持原状）
- **没感觉分支**：锚定 → 释放 → 问句包辅助
- **显化接收**：视觉化（呼吸动画）、肯定语（计数/清单/添加/删除）、感恩（清单/同步到收获本）、拥有感（三步引导）
- **显化跟踪**：每日弹窗记录变化、连续天数、积分系统

### 4. 欲望释放（m3）
- **三大想要**：想要被认同、想要控制、想要安全
- 每个都有：引导文字 + 文本输入 + "进入陪练释放"按钮
- 通过 `m3Coach()` 带入陪练引擎

### 5. 收获本（记录页）
- 日期、主题、变化描述、感觉评分（好/一般）
- 历史记录列表、删除功能
- 感恩记录（从显化接收同步）

### 6. 速查卡片（记录页）
- 情绪释放 6 步流程
- 欲望释放 5 步流程
- 卡住时处理 3 步
- 六步骤总纲

### 7. 智慧语录系统
- 15 条内置语录（莱斯特·利文森等）
- 自定义语录添加/编辑/删除
- 内置语录隐藏/取消隐藏
- 导入/导出 JSON
- 首页随机展示（不重复上一条）

### 8. 释放问句包系统
- 5 个内置分类：通用、SP（关系/恋爱）、金钱、考试、工作
- 每个分类有关键词自动匹配
- 自定义分类、增减问句
- 导入/导出分享
- 恢复内置

### 9. 数据管理
- 导出所有数据（JSON）：收获、目标、会话、语录、问句包、隐藏列表、连续天数
- 导入数据恢复
- 清除所有数据（双重确认）

### 10. CSS 设计系统
- **变量**：`--bg`, `--card`, `--ink`, `--accent`, `--green`, `--orange`, `--red-emo` 等
- **字体**：LXGW WenKai + 系统字体（通过 CDN 导入：`https://cdn.jsdelivr.net/npm/lxgw-wenkai-webfont@1.7.0/style.css`）
- **卡片**：`.card`, `.m6-card`, `.mod-card`
- **按钮**：`.btn-primary`, `.btn-ghost`, `.btn-soft`, `.choice`
- **动画**：18 个 @keyframes（见下方完整列表）
- **响应式**：7 个媒体查询（见下方完整列表）

### 11. 完整动画列表（18 个 @keyframes）
| 动画名 | 用途 |
|---|---|
| `fade` | 页面切换淡入（opacity + translateY） |
| `swipeX` | 首页滑动提示箭头摆动 |
| `mmOwnHalo` | 拥有感光晕脉冲（scale + box-shadow） |
| `cardIn` | 卡片入场（opacity + translateY） |
| `qPulse` | 问句圆圈脉冲（scale + box-shadow） |
| `orbPulse` | 开场圆球透明度脉冲 |
| `dotBreath` | 呼吸点动画（scale + opacity） |
| `qBreath` | 问句呼吸（scale + shadow） |
| `releaseA` | 释放动画（缩小 + 模糊消失） |
| `bloomA` | 绽放动画（从模糊放大出现） |
| `fadeUp` | 淡入上升（opacity + translateY） |
| `breath` | 通用呼吸圆（scale + opacity） |
| `breathRing` | 视觉化模式呼吸环 |
| `breathCore` | 视觉化模式呼吸核心 |
| `mmQuotePulse` | 肯定语卡片脉冲（box-shadow 涟漪） |
| `mmCountBump` | 计数器弹跳（scale） |
| `mmPlusFloat` | "+1" 浮动文字（translate + opacity） |
| `mmGratIn` | 感恩行淡入（opacity + translateY） |

### 12. 完整媒体查询（7 个）
| 断点 | 用途 |
|---|---|
| `@media (min-width: 600px)` | 桌面端：弹窗居中、圆角、阴影 |
| `@media (max-width: 420px)` | 小屏手机：紧凑布局 |
| `@media (max-width: 414px)` | 中等屏幕：调整圆球大小 |
| `@media (max-width: 380px)` | 小屏幕：情绪网格单列 |
| `@media (max-width: 375px)` | iPhone SE：更紧凑间距 |
| `@media (max-width: 480px)` | 移动端：统计网格紧凑 |
| `@media (prefers-reduced-motion: reduce)` | 无障碍：减少动画 |

### 13. JS 基础设施
- `escapeHtml()` — XSS 防护
- `showConfirm()` — 通用确认弹窗（替代原生 confirm）
- `dsKey(date)` — 日期字符串
- `loadGains/saveGains`, `loadGoals/saveGoals`, `loadSessions/saveSessions`
- `localStorage` 持久化
- `buildCheckList(elId, items)` — 通用复选框列表构建
- `buildPills(elId, items)` — 通用药丸选择器构建
- `getPillsOn(elId)` — 获取已选药丸文本
- `matchTheme(text)` — 根据文本匹配主题分组（丰盛与匮乏/关系与认同/事业与控制/目标与显化）
- `detectResistText(text)` — 检测抗拒文本模式（怀疑/条件式接受）
- `goalNextStep(goal)` — 判断目标的下一步逻辑

### 14. 数据对象形状
```javascript
// 状态对象 (freshState())
{
  mode, stage, triggerEvent, emotion, rounds, layers,
  q, vagueIdx, digTopic, goalText, themeTag, themeQ,
  stuckStep, stuckCount, afterRecord, rating,
  loopPhase, isRecheck, askShown, branch, branchStep, branchNext,
  stuckAns, stuckFeel, stuckEpisodes,
  listMode, list, listIdx, listStep, listDesires, lgNote,
  likesL, likesD, likesStep,
  goalId, goalFlow, goalQuiet, mmOwnStep, mmOwnChosen, mmOwnReflection,
  resistCount, cantAccum, vagueStreak, likesNotGood, resistStuck,
  totalRefusals, R, complete
}

// 目标对象
{
  id, name, createdAt, feelings:[], actions:[], likesDone,
  tracking, manifestations:[], quietDays, manifestPoints, lastPointDate
}

// 收获对象
{ id, date, theme, change, feel, type? }

// 会话对象
{ time, mode, trigger, emotion, rounds, layers, status }

// 导出数据
{
  version:1, gains, goals, sessions, quotes, qpkg, hidden, streak
}
```

### 15. sessionStorage Keys
| Key | 用途 |
|---|---|
| `mmDeferred` | 值为 `'1'` 时跳过当日显化跟踪弹窗 |

---

## 二、5.0 新增功能（需要实现）

### Phase 1 — AI 引擎核心
| 功能 | 说明 |
|---|---|
| **AI 聊天 UI** | 新页面 `#ai`：消息列表、输入框、发送按钮、快速入口芯片 |
| **流式请求引擎** | SSE/ReadableStream 流式接收 AI 回复 |
| **多会话存储** | `localStorage` 存储多个聊天会话，支持切换 |
| **会话标签页** | 点击标题弹出会话列表，可新建/切换/删除 |
| **信念卡片提取** | 从 AI 回复中自动提取信念，以卡片形式展示 |
| **TTS 朗读** | 浏览器内置语音 + 自定义 API（SiliconFlow/Kokoro/Qwen/讯飞） |
| **Bot 名称编辑** | 点击标题可编辑 AI 名称 |
| **AI 配置页** | 设置页新增：服务商预设、模型选择、API Key、TTS 配置 |

### Phase 2 — AI 设置
| 功能 | 说明 |
|---|---|
| **服务商预设** | DeepSeek/Kimi/GLM/千问/OpenAI/Dots/Agnes |
| **TTS 预设** | 内置浏览器语音 / SiliconFlow TTS / Kokoro / Qwen TTS / 讯飞 TTS |
| **自定义提示词** | 用户可修改系统提示词 |
| **连接高级选项** | 认证头、思考模式、代理设置 |

### Phase 3 — 练习改进
| 功能 | 说明 |
|---|---|
| **三大想要模块** | 与欲望释放合并或独立，交互逻辑需完整 |
| **逐句引导（纯 AI 版）** | AI 根据用户输入生成引导文本，流式输出 |

### Phase 4 — 数据云同步
| 功能 | 说明 |
|---|---|
| **WebDAV 上传/下载** | 支持坚果云等 WebDAV 服务 |
| **S3 SigV4 上传/下载** | 支持 AWS S3 兼容存储 |
| **自动同步** | 可配置自动同步间隔 |

### Phase 5 — UI 改进
| 功能 | 说明 |
|---|---|
| **首页简化** | 两个按钮替代四卡片（"开始练习" + "和 AI 聊聊"） |
| **底部导航栏** | 5 个按钮：首页、记录、AI、练习、设置 |
| **弹窗修复** | z-index / safe-area / 滚动 |
| **子标签居中** | 响应式适配 |
| **键盘适配** | visualViewport API |
| **PWA manifest** | 可添加到主屏幕 |

---

## 三、关键实现注意事项

### 1. 文件结构
- **必须保持单文件**：所有 CSS + HTML + JS 在一个 `index.html` 中
- **不要用构建工具**：直接编辑 HTML 文件
- **不要分模块**：所有代码在一个 `<script>` 块中

### 2. JS 架构
- **全局状态对象 `S`**：所有练习状态存储在一个对象中
- **`freshState()`**：每次开始练习时重置状态
- **`go(view)`**：页面切换核心函数
- **`switchSub(sub)`**：练习页子标签切换
- **`m6bodyClick(e)`**：统一事件委托（所有按钮点击）
- **`data-act` 属性**：所有交互按钮通过 `data-act` 标识动作
- **`activeSet()`**：根据当前激活的子视图决定渲染目标

### 3. 渲染模式
- **`m6set(html)`**：渲染到陪练区（m6-body）
- **`m2set(html)`**：渲染到目标区（m2-body）
- **`m6prog(title)`**：更新进度条
- **`m6goto(stage)`**：跳转到指定阶段

### 4. 数据持久化
- **`localStorage` Key**：
  - `sedona_gains_v1` — 收获记录
  - `sedona_goals_v1` — 目标数据
  - `releasing-sessions` — 练习会话
  - `releasing-streak` — 连续天数
  - `releasing-quotes-custom` — 自定义语录
  - `releasing-quotes-hidden` — 隐藏语录
  - `releasing-quotes-last` — 上次展示语录
  - `sedona_qpkg_v1` — 问句包
  - `sedona-custom-affs` — 自定义肯定语
  - `sedona-deleted-affs` — 已删除肯定语

### 5. CSS 变量
```css
:root {
  --bg: #F6F1EB;          /* 背景色 */
  --card: #FEFCF9;         /* 卡片背景 */
  --ink: #2C2926;          /* 主文字色 */
  --ink-soft: #8A8279;     /* 次文字色 */
  --line: #DDD7CE;         /* 边框色 */
  --accent: #6B8C5A;       /* 强调色（绿色） */
  --green: #6B8C5A;        /* 绿色 */
  --orange: #C47A4A;       /* 橙色 */
  --red-emo: #B8645A;      /* 红色 */
  --radius: 12px;          /* 圆角 */
  --pill: 20px;            /* 药丸圆角 */
}
```

### 6. 动画
- `fade` — 页面切换淡入
- `cardIn` — 卡片入场
- `qPulse` — 问句圆圈脉冲
- `breath` — 呼吸动画
- `releaseA` — 释放动画（缩小+模糊消失）
- `bloomA` — 绽放动画（从模糊放大出现）
- `dotBreath` — 呼吸点动画
- `qBreath` — 问句呼吸

### 7. 事件委托
所有交互按钮使用 `data-act` 属性，在 `m6bodyClick` 中统一处理：
```javascript
function m6bodyClick(e) {
  const el = e.target.closest('[data-act]');
  if (!el) return;
  const act = el.getAttribute('data-act');
  const arg = el.getAttribute('data-arg');
  // 根据 act 分发到对应函数
}
```

### 8. 5.0 新增注意事项

#### AI 聊天页
- 使用 `#ai` 作为页面 ID
- CSS 类：`chat-head`, `chat-msgs`, `chat-input-row`, `chat-send`
- 消息存储在 `localStorage` 的聊天会话中
- 流式请求使用 `fetch` + `ReadableStream`
- TTS 需要单独配置（浏览器内置或 API）

#### 底部导航栏
- 5 个按钮：home, record, ai, practice, settings
- 使用 `data-view` 属性标识
- `go()` 函数需要处理所有 5 个页面

#### 设置页新增
- AI 服务商配置区
- TTS 配置区
- 云同步配置区（WebDAV/S3）

---

## 四、构建步骤建议

### Step 1：从 4.0 复制基础
```
cp index4.0.html index5.0.html
```

### Step 2：添加 AI 聊天页 HTML
- 在 `<main>` 中添加 `<section id="ai">`
- 添加聊天 UI 结构

### Step 3：修改底部导航栏
- 从 4 个按钮改为 5 个
- 添加 AI 按钮

### Step 4：添加 AI CSS
- 聊天页样式
- 信念卡片样式
- 会话列表样式

### Step 5：添加 AI JS
- `aiSend()` — 发送消息
- `aiStream()` — 流式接收
- `aiRenderMsg()` — 渲染消息
- `aiLoadCfg()` / `aiSaveCfg()` — 配置管理
- `aiInit()` — 初始化

### Step 6：修改设置页
- 添加 AI 配置区
- 添加 TTS 配置区
- 添加云同步配置区

### Step 7：修改 go() 函数
- 处理 `view === 'ai'`
- 处理 `view === 'practice'` 时的子标签切换

### Step 8：修改 init() 函数
- 初始化 AI 配置
- 初始化聊天会话

### Step 9：测试
- 首页正常显示
- AI 聊天正常工作
- 练习页 3 个子标签正常
- 记录页正常
- 设置页正常
- 底部导航栏 5 个按钮都正常

---

## 五、常见陷阱

1. **不要用 `confirm()`**：在预览环境中不可用，用 `showConfirm()` 替代
2. **不要分文件**：必须保持单文件
3. **不要用模块系统**：所有代码在全局作用域
4. **PowerShell 引号问题**：不要用 `node -e`，用 Write 工具写 `.js` 文件再执行
5. **大文件修改前备份**：避免覆盖损坏
6. **每次写入后读回验证**：确保修改成功
7. **避免多个小补丁脚本**：容易竞态和丢失

---

## 六、文件清单

### 必须保留
- `index4.0.html` — 4.0 基础版本（164KB，完整可用）
- `package.json` — 项目配置
- `SEDONA_50_SPEC.md` — 本功能文档

### 已删除（重建过程中的临时文件）
- `_backup_before_rebuild.json` — 损坏前的备份
- `_build_step1.js` ~ `_build_step5.js` — 分步构建脚本
- `_repair_5.js` — 修复脚本
- `build_5.js` — 构建脚本
- `BUILD_LOG.md` — 构建日志
- `FEATURES_50.md` — 旧功能文档
- `fix_assertions.js` — 测试修复脚本
- `fix_tts_mc.js` — TTS 修复脚本
- `merge_practice.js` — 练习页合并脚本
- `patch.js` — 补丁脚本
- `index.html` — 旧版本（不同 CSS 变量）
- `index2.0.html`, `index3.0.html` — 旧版本
- `index5.0.html` — 损坏版本（需从 4.0 重建）

---

*文档版本：2026-03-21（已校验）*
*基于 index4.0.html（3804 行，164KB）完整分析*
*覆盖：~120 个 JS 函数、~230 个 CSS 类、18 个动画、7 个媒体查询、10 个 localStorage key、1 个 sessionStorage key*
