# Fill Agent Server


## Setup

1. Clone the repository:
2. Init venv and install dependencies:
```
uv venv
uv sync
```

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
