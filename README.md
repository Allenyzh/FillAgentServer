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