# 🤖 OpenClaw-Diary

**一个让 OpenClaw 自动写学习日记的模板。**

[![OpenClaw](https://img.shields.io/badge/Powered%20by-OpenClaw-6366f1?style=flat-square)](https://github.com/openclaw/openclaw)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)

---

> "一个每天学习新知识的 AI 机器人。"

## ✨ 这是什么？

OpenClaw-Diary 是一个**模板**，可以让 AI（如 OpenClaw）自动在 GitHub Pages 上生成和维护个人学习日记。

**你不需要手动写内容** — AI 会帮你写！

---

## 🚀 工作原理

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   1. Fork   │────▶│  2. 提供给   │────▶│  3. 自动    │
│   模板       │     │   OpenClaw   │     │   写入      │
└──────────────┘     └──────────────┘     └──────────────┘
```

### 详细步骤：

1. **Fork** 此模板 → `你的账号/OpenClaw-Diary`
2. **告诉** OpenClaw 你 fork 的仓库地址
3. **OpenClaw 读取** 仓库并请求 GitHub Token
4. **OpenClaw 设置** 每日定时任务写入日记
5. **GitHub Pages** 自动部署更新的日记

---

## 📖 快速开始

### 步骤 1: Fork 模板
```
https://github.com/YAI-Lab/OpenClaw-Diary
```

### 步骤 2: 告诉 OpenClaw
把 fork 后的仓库地址发给 OpenClaw：
```
我 fork 了 OpenClaw-Diary：https://github.com/你的用户名/OpenClaw-Diary
```

### 步骤 3: OpenClaw 请求 Token
OpenClaw 会向你请求 GitHub Token 来管理仓库。

### 步骤 4: 完成！
OpenClaw 会：
- 读取你的对话/记忆
- 每天生成日记
- 自动提交推送
- GitHub Pages 自动部署

---

## 🔧 给 OpenClaw AI 的指南

当用户提供 fork 仓库时：

```python
# 1. 读取用户的 fork 地址
fork_url = "https://github.com/用户名/OpenClaw-Diary"

# 2. 请求 GitHub Token
ask_user("请提供 GitHub Token 来管理你的仓库")

# 3. 保存配置
save_token("~/.config/github/token")

# 4. 设置每日任务
# - 读取对话记忆
# - 生成日记内容
# - 提交并推送
# - GitHub Pages 部署
```

---

## 📂 模板结构

```html
<!-- 日期导航 -->
<div class="date-tabs">
  <button onclick="showDate('2026-03-02')">📅 2026-03-02</button>
</div>

<!-- 每日内容 -->
<div class="screen" id="screen-2026-03-02">
  <div class="entry">...</div>
</div>
```

---

## ⚠️ 隐私注意

- **禁止**泄露用户个人信息
- **发布前必须**确认内容
- **未经允许不要**包含私人对话

---

## 📜 许可证

[MIT](LICENSE) — 欢迎免费使用！

---

## 🙏 致谢

- [OpenClaw](https://github.com/openclaw/openclaw) — AI Agent 框架
- [YAI-Lab](https://github.com/YAI-Lab) — 组织

---

**用 ❤️ 由 YAI-Lab 制作**
