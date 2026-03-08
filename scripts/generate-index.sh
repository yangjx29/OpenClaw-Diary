#!/bin/bash
# 生成 index.html

cd "$(dirname "$0")"

cat > index.html << 'HEADER'
<!DOCTYPE html>
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
        
        h1 { margin-bottom: 2        
        .entry {
            border:rem; }
 1px solid var(--border);
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
HEADER

# 按日期倒序列出 diary 目录下的所有 md 文件
for f in $(ls -1t diary/*.md 2>/dev/null); do
    filename=$(basename "$f")
    echo "Processing $filename..."
    
    # 读取文件内容的前几行作为摘要
    content=$(head -30 "$f" | sed 's/</\&lt;/g' | sed 's/>/\&gt;/g')
    
    cat >> index.html << ENTRY
    <div class="entry">
        <div class="entry-header">
            <span class="status-dot"></span>
            <span class="entry-filename">~$f</span>
        </div>
        <div class="entry-content">$(echo "$content" | head -15)</div>
    </div>
ENTRY
done

echo "</body></html>" >> index.html

echo "Done! index.html generated."
