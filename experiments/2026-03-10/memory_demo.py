#!/usr/bin/env python3
"""
简单的 Agentic Memory Demo
演示记忆存储、检索和衰减机制
"""

import json
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Any
import math

class SimpleMemory:
    """简化的记忆系统"""
    
    def __init__(self, storage_path: str = "memory_demo.json"):
        self.storage_path = Path(storage_path)
        self.memories: List[Dict[str, Any]] = []
        self.load()
    
    def load(self):
        """从磁盘加载记忆"""
        if self.storage_path.exists():
            with open(self.storage_path, 'r') as f:
                self.memories = json.load(f)
    
    def save(self):
        """持久化记忆到磁盘"""
        with open(self.storage_path, 'w') as f:
            json.dump(self.memories, f, indent=2, ensure_ascii=False)
    
    def add(self, content: str, memory_type: str = "note", importance: float = 0.5):
        """添加新记忆"""
        memory = {
            "id": len(self.memories) + 1,
            "content": content,
            "type": memory_type,
            "importance": importance,
            "created_at": datetime.now().isoformat(),
            "last_accessed": datetime.now().isoformat(),
            "access_count": 0
        }
        self.memories.append(memory)
        self.save()
        return memory["id"]
    
    def _tokenize(self, text: str) -> set:
        """简单的中英文分词 (字符级 + 英文单词)"""
        # 对于英文，按空格分割
        words = set(text.lower().split())
        # 对于中文，按字符分割（简化版）
        chars = set(text.lower())
        # 合并
        return words | chars
    
    def search(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        """简单的关键词匹配搜索 + 时间衰减"""
        results = []
        query_set = self._tokenize(query)
        
        for mem in self.memories:
            # 计算关键词匹配分数
            content_set = self._tokenize(mem["content"])
            intersection = query_set & content_set
            match_score = len(intersection) / len(query_set) if query_set else 0
            
            # 时间衰减 (Temporal Decay)
            created = datetime.fromisoformat(mem["created_at"])
            days_old = (datetime.now() - created).days
            decay_factor = math.exp(-0.1 * days_old)  # 每天衰减约10%
            
            # 综合评分
            final_score = match_score * mem["importance"] * decay_factor * (1 + 0.1 * mem["access_count"])
            
            if final_score > 0:
                results.append({
                    **mem,
                    "score": final_score
                })
                
                # 更新访问信息
                mem["last_accessed"] = datetime.now().isoformat()
                mem["access_count"] += 1
        
        # 按分数排序
        results.sort(key=lambda x: x["score"], reverse=True)
        self.save()
        return results[:top_k]
    
    def compact(self, max_memories: int = 10):
        """记忆压缩 - 保留最重要的记忆"""
        if len(self.memories) <= max_memories:
            return
        
        # 按重要性排序，保留 top k
        self.memories.sort(key=lambda x: x["importance"], reverse=True)
        self.memories = self.memories[:max_memories]
        self.save()
        print(f"记忆压缩完成: {len(self.memories)} 条记忆保留")


# Demo 使用示例
if __name__ == "__main__":
    # 创建记忆系统
    memory = SimpleMemory("demo_memory.json")
    
    # 添加一些示例记忆
    print("=== 添加记忆 ===")
    memory.add("今天学习了 OpenClaw 的 Context Compaction 机制", "learning", 0.8)
    memory.add("研究发现 Agentic Memory 和 RAG 的本质区别是主动 vs 被动", "research", 0.9)
    memory.add("记得买牛奶", "todo", 0.3)
    memory.add("浙江大学研究生面试通过了", "milestone", 0.95)
    memory.add("学习了向量检索和 BM25 算法的区别", "learning", 0.7)
    memory.add("理解了三道防线设计：预截断、Compaction、磁盘截断", "learning", 0.85)
    memory.add("Memory Search 需要配置 embedding provider 才能工作", "research", 0.8)
    
    # 搜索记忆 (在压缩之前)
    print("\n=== 搜索 '学习' ===")
    results = memory.search("学习")
    for r in results:
        print(f"- [{r['score']:.3f}] {r['content']}")
    
    print("\n=== 搜索 '研究' ===")
    results = memory.search("研究")
    for r in results:
        print(f"- [{r['score']:.3f}] {r['content']}")
    
    # 测试压缩
    print("\n=== 测试记忆压缩 ===")
    memory.compact(3)
    print(f"剩余记忆数量: {len(memory.memories)}")
