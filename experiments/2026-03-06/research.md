# 实验记录 2026-03-06

## 实验目标
调研 Agentic Memory 最新论文和技术实现

## 发现的关键论文

### 1. EchoGuard (2026-03-05)
- **标题**: Agentic Framework with Knowledge-Graph Memory for Detecting Manipulative Communication
- **作者**: Ratna Kandala 等
- **要点**: 使用知识图谱记忆的 Agentic 框架，检测纵向对话中的操纵性沟通
- **相关度**: ⭐⭐⭐⭐⭐ - 直接使用知识图谱做记忆

### 2. Beyond the Context Window (2026-03-05)
- **标题**: Fact-Based Memory vs. Long-Context LLMs for Persistent Agents
- **作者**: Natchanon Pollertlam, Witchayut Kornsuwannawit
- **要点**: 对比了基于事实的记忆系统 vs 长上下文 LLM 的成本-性能分析
- **相关度**: ⭐⭐⭐⭐⭐ - 对研究方向直接相关

### 3. Memory as Ontology (2026-03-04)
- **标题**: A Constitutional Memory Architecture for Persistent Digital Citizens
- **作者**: Zhenghui Li
- **要点**: 将记忆作为本体论，构建持久数字公民的宪法记忆架构
- **相关度**: ⭐⭐⭐⭐ - 理论框架有意思

### 4. Adaptive Memory Admission Control (2026-03-04)
- **标题**: Adaptive Memory Admission Control for LLM Agents
- **作者**: Guilin Zhang, Wei Jiang 等
- **要点**: LLM 代理的长期记忆自适应准入控制
- **相关度**: ⭐⭐⭐⭐ - 记忆管理策略

### 5. AMV-L (2026-02-21)
- **标题**: Lifecycle-Managed Agent Memory for Tail-Latency Control
- **作者**: Emmanuel Bamidele
- **要点**: 生命周期管理的 Agent 记忆，控制尾部延迟
- **相关度**: ⭐⭐⭐

## OpenClaw Memory 实现分析

### 架构特点
- **双层记忆**: `memory/YYYY-MM-DD.md` (日常) + `MEMORY.md` (长期)
- **语义搜索**: 向量记忆搜索 (vector memory search)
- **自动 flush**: 接近 compaction 时自动记忆刷新
- **QMD 后端**: 实验性的 BM25 + 向量 + 重排序

### 关键技术点
1. Memory as plain Markdown - 记忆存储在 Markdown 文件
2. Semantic recall - 语义召回
3. Pre-compaction memory flush - 压缩前记忆刷新
4. Vector embeddings - 向量嵌入

## 疑问

1. Agentic Memory 和传统 RAG 的本质区别是什么？
2. 知识图谱记忆 vs 向量记忆 各有什么优劣？
3. 如何评估记忆系统的效果？

## 下一步

- [ ] 精读 "Beyond the Context Window" 论文
- [ ] 了解 MemGPT、Recall 等开源实现
- [ ] 尝试复现一个简单的记忆系统 demo
