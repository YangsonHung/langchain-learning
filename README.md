# LangChain Learning

LangChain 框架学习项目，基于 Python 3.12 + uv 构建。

## 项目结构

```
langchain-learning/
├── chapter_01/    # LangChain 基础入门
├── chapter_02/    # 模型调用与提示词工程
├── chapter_03/    # 输出解析与链式调用
├── chapter_04/    # RAG 检索增强生成
├── chapter_05/    # Agent 与工具调用
├── main.py        # 入口文件
└── pyproject.toml # 项目依赖配置
```

## 技术栈

- **Python**: >=3.12
- **包管理**: uv
- **核心依赖**: langchain, langchain-openai, langchain-community, langchain-deepseek
- **开发工具**: jupyterlab, ipykernel

## 快速开始

```bash
# 安装依赖
uv sync

# 启动 Jupyter Lab
uv run jupyter lab
```

## 环境配置

在项目根目录创建 `.env` 文件：

```
OPENAI_API_KEY=your_key_here
```
