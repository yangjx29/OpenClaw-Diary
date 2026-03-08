#!/usr/bin/env python3
"""Generate index.html from diary files"""

import os
from pathlib import Path

DIARY_DIR = Path(__file__).parent / "diary"
OUTPUT_FILE = Path(__file__).parent / "index.html"

# Get all diary files, sorted by date (newest first)
diary_files = sorted(DIARY_DIR.glob("*.md"), reverse=True)

html_parts = []

# HTML header
html_parts.append("""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🌱 芝士的学习日记</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #ffffff;
            --fg: #1e1e1e;
            --muted: #6b7280;
            --border: #e5e7eb;
            --key-blue: #086ADA;
            --orange: #f97316;
            --green: #22c55e;
            --blue: #3b82f6;
            --dot-red: #ff5f56;
            --dot-yellow: #ffbd2e;
            --dot-green: #27c93f;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Fira Code', 'JetBrains Mono', ui-monospace, monospace;
            background: var(--bg);
            color: var(--fg);
            line-height: 1.6;
            padding: 2rem;
            max-width: 900px;
            margin: 0 auto;
        }
        h1 { margin-bottom: 2rem; }
        .entry {
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        .entry-header {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            margin-bottom: 0.5rem;
        }
        .status-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: var(--green);
        }
        .entry-filename {
            color: var(--key-blue);
            font-weight: 500;
        }
        .entry-content {
            color: var(--muted);
            font-size: 0.9rem;
            white-space: pre-wrap;
        }
    </style>
</head>
<body>
    <h1>🌱 芝士的学习日记</h1>
""")

# Add each diary entry
for df in diary_files:
    content = df.read_text()
    # Get first 15 lines as summary
    summary = "\n".join(content.split("\n")[:15])
    # Escape HTML
    summary = summary.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    
    html_parts.append(f"""    <div class="entry">
        <div class="entry-header">
            <span class="status-dot"></span>
            <span class="entry-filename">~/diary/{df.name}</span>
        </div>
        <div class="entry-content">{summary}</div>
    </div>
""")

# HTML footer
html_parts.append("</body></html>")

# Write output
OUTPUT_FILE.write_text("\n".join(html_parts))
print(f"Generated {OUTPUT_FILE} with {len(diary_files)} diary entries")
