# Fill Agent Server


## Setup

1. Clone the repository:
2. Init venv and install dependencies:
```
uv venv
uv sync
```
3. Install playwright browsers:
   
```
playwright install
```

## Development

### Development ufile_helper

1. Run the `test_server.py` to start the test server:
2. Run your `playwright_helper.py` in a separate terminal.

## Run

### Run a test web server

```
adk web --allow_origins "*"
```

### Run a cli 

```
adk run income_tax_agent
```


### Run a API Server

```
adk api_server --allow_origins "*"
```

### Run production server

```
uv run main.py
```

## Environment Variables

```
GOOGLE_GENAI_USE_VERTEXAI="False"
```

Google GenAI API key. Get it from `aistudio.google.com`
```
GOOGLE_API_KEY="yyy"
```

Server JWT secret key. This is used to sign JWT tokens. You can use `gentoken.py` to generate a token.
```
JWT_SECRET_KEY="xxx"
```

## English Documentation

### Description

An AI-driven automatic tax filing checker. Once users provide personal and tax-related information using natural language, the AI automatically opens the relevant tax form webpages, fills in personal details and tax data, and allows users to retrieve or summarize the provided information using natural language commands for easy verification.

### Features

- Automatically open webpages and fill tax information
- Natural language input and control
- Intelligent retrieval and summarization of filled data
- User-friendly interactive review interface

### Tech Stack

- Python
- Playwright
- Google GenAI
- JWT Authentication

### Installation

1. Clone repository:

```bash
git clone https://github.com/yourusername/fill-agent-server.git
```

2. Init virtual environment and install dependencies:

```bash
uv venv
uv sync
```

3. Install Playwright browsers:

```bash
playwright install
```

### Usage

#### Run a test web server

```bash
adk web --allow_origins "*"
```

#### Run CLI

```bash
adk run income_tax_agent
```

#### Run API Server

```bash
adk api_server --allow_origins "*"
```

#### Run production server

```bash
uv run main.py
```

### Environment Variables

Set Google GenAI API key and JWT secret key.

```bash
GOOGLE_GENAI_USE_VERTEXAI="False"
GOOGLE_API_KEY="your_google_api_key"
JWT_SECRET_KEY="your_jwt_secret_key"
```

Obtain your API key from [aistudio.google.com](https://aistudio.google.com).

### Development & Testing

#### Testing ufile_helper

1. Start the test server:

```bash
python test_server.py
```

2. Run Playwright helper in a separate terminal:

```bash
python playwright_helper.py
```

### Contributing

Contributions and suggestions are welcome:

1. Fork this repository
2. Create a new branch
3. Commit your changes
4. Create a Pull Request

### License

This project is licensed under the MIT License.

### Contact

- Your Name - your.email@example.com
- GitHub URL: [https://github.com/yourusername/fill-agent-server](https://github.com/yourusername/fill-agent-server)


## 中文文档

### 项目简介

一个基于人工智能的自动报税检查工具。用户通过自然语言向AI提供个人信息与报税数据后，AI即可自动打开相关报税网页，填写个人信息和税务数据，并支持自然语言指令回顾和总结填报信息，便于用户进行快速核查。

### 功能列表

- 自动打开网页并填写报税信息
- 支持自然语言输入与控制
- 智能检索已填信息并生成摘要
- 提供便捷的交互式核对界面

### 技术栈

- Python
- Playwright
- Google GenAI
- JWT Authentication

### 安装步骤

1. 克隆仓库：

```bash
git clone https://github.com/yourusername/fill-agent-server.git
```

2. 初始化虚拟环境并安装依赖：

```bash
uv venv
uv sync
```

3. 安装 Playwright 浏览器：

```bash
playwright install
```

### 使用说明

#### 运行测试服务器

```bash
adk web --allow_origins "*"
```

#### 运行 CLI 程序

```bash
adk run income_tax_agent
```

#### 运行 API 服务器

```bash
adk api_server --allow_origins "*"
```

#### 运行生产服务器

```bash
uv run main.py
```

### 环境变量配置

设置 Google GenAI API 密钥和 JWT 密钥。

```bash
GOOGLE_GENAI_USE_VERTEXAI="False"
GOOGLE_API_KEY="your_google_api_key"
JWT_SECRET_KEY="your_jwt_secret_key"
```

从 [aistudio.google.com](https://aistudio.google.com) 获取 API 密钥。

### 开发与测试

#### 测试 ufile_helper

1. 启动测试服务器：

```bash
python test_server.py
```

2. 在新终端中运行 Playwright 辅助程序：

```bash
python playwright_helper.py
```

### 贡献

欢迎贡献代码或提出改进建议，步骤如下：

1. Fork 本仓库
2. 创建新分支
3. 提交代码更改
4. 发起 Pull Request

### 许可协议

本项目遵循 MIT 协议。

### 联系方式

- Your Name - your.email@example.com
- GitHub 地址：[https://github.com/yourusername/fill-agent-server](https://github.com/yourusername/fill-agent-server)

---


