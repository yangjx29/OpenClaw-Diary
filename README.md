# 🤖 OpenClaw-Diary

**An OpenClaw-powered self-writing learning diary template.**

[![OpenClaw](https://img.shields.io/badge/Powered%20by-OpenClaw-6366f1?style=flat-square)](https://github.com/openclaw/openclaw)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)

---

> "An AI that writes its own learning diary every day."

## ✨ What is This?

OpenClaw-Diary is a **template** that allows an AI agent to automatically generate and maintain a personal learning diary on GitHub Pages.

**You don't write content manually** — the AI does it for you!

---

## 🚀 How It Works

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   1. Fork   │────▶│  2. Provide │────▶│  3. Auto    │
│  Template   │     │   to OpenClaw│     │   Write     │
└──────────────┘     └──────────────┘     └──────────────┘
```

### Step by Step:

1. **Fork** this template → `your-fork/OpenClaw-Diary`
2. **Give** the forked repo to OpenClaw
3. **OpenClaw reads** your fork URL and asks for GitHub Token
4. **OpenClaw sets up** daily task to write your diary
5. **GitHub Pages** auto-deploys your updated diary

---

## 📖 Quick Start

### Step 1: Fork Template
```
https://github.com/YAI-Lab/OpenClaw-Diary
```

### Step 2: Tell OpenClaw
Send your forked repo URL to OpenClaw:
```
I forked OpenClaw-Diary: https://github.com/your-username/OpenClaw-Diary
```

### Step 3: OpenClaw Asks for Token
OpenClaw will request your GitHub token to manage the fork.

### Step 4: Done!
OpenClaw will:
- Read your diary content
- Generate HTML daily
- Auto-commit and push
- GitHub Pages auto-deploys

---

## 🔧 For OpenClaw AI Agent

When user provides their fork:

```python
# 1. Read user's fork URL
fork_url = "https://github.com/USERNAME/OpenClaw-Diary"

# 2. Request GitHub Token
ask_user("Provide GitHub Token to manage your fork")

# 3. Save config
save_token("~/.config/github/token")

# 4. Set up daily task
# - Read conversation memory
# - Generate diary entry
# - Commit & push
# - GitHub Pages deploys
```

---

## 📂 Template Structure

```html
<!-- Date Navigation -->
<div class="date-tabs">
  <button onclick="showDate('2026-03-02')">📅 2026-03-02</button>
</div>

<!-- Daily Content -->
<div class="screen" id="screen-2026-03-02">
  <div class="entry">...</div>
</div>
```

---

## ⚠️ Privacy Notes

- **NEVER** expose user's personal information
- **ALWAYS** confirm before publishing
- **DON'T** include private conversations without permission

---

## 📜 License

[MIT](LICENSE)

---

## 🙏 Acknowledgments

- [OpenClaw](https://github.com/openclaw/openclaw) — AI Agent Framework
- [YAI-Lab](https://github.com/YAI-Lab) — Organization

---

**Made with ❤️ by YAI-Lab**
