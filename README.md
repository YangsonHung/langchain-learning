# LangChain Learning

LangChain 框架学习项目，基于 Python 3.12 + uv 构建。

## 项目结构

```
langchain-learning/
├── chapter_*/     # 各章节学习笔记与代码，章节持续增加
├── main.py        # 入口文件
├── pyproject.toml # 项目依赖配置
└── uv.lock        # 依赖锁文件
```

## 技术栈

- **Python**: >=3.12
- **包管理**: uv
- **依赖**: 以 `pyproject.toml` 为准

## 快速开始

```bash
# 安装依赖
uv sync

# 启动 Jupyter Lab
uv run jupyter lab
```

## 环境配置

在项目根目录创建 `.env` 文件：

```env
OPENAI_API_KEY=your_key_here
```

## 约定

- 使用约定式提交（Conventional Commits）
- API 密钥通过 `.env` 管理，不提交到仓库
