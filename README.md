# Sense Cache

Sense Cache is a production-grade semantic caching proxy server for LLM APIs. It reduces latency and costs by caching semantically similar requests using vector embeddings.

## Features

- **Semantic Caching**: Uses vector embeddings to find similar queries.
- **Pluggable Backends**: Supports Redis and In-Memory caching (extensible).
- **Clean Architecture**: Separation of concerns with API, Core, Cache, and Embeddings modules.
- **Production Ready**: Structured logging, configuration management, and dependency injection.

## Requirements

- Python 3.10+
- Redis (optional, for production cache backend)

## Setup

1.  **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd sensecache
    ```

2.  **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment:**

    Copy `.env.example` to `.env` and update the values.

    ```bash
    cp .env.example .env
    ```

## Running the Server

To start the server in development mode with hot-reload:

```bash
uvicorn server:app --reload
```

The API will be available at `http://localhost:8000`.
API Documentation (Swagger UI) is available at `http://localhost:8000/docs`.

## Running Tests

Run the test suite using `pytest`:

```bash
pytest
```

## Project Structure

-   `api/`: FastAPI routes, models, and dependencies.
-   `cache/`: Cache implementations (Redis, Memory) and base protocol.
-   `core/`: Core configuration, logging, security, and utilities.
-   `embeddings/`: Embedding generation service.
-   `tests/`: Unit and integration tests.

## Philosophy

This project follows clean architecture principles:
-   **Dependency Injection**: Dependencies like cache backends and embedders are injected into routes.
-   **Structured Logging**: Uses `structlog` for machine-readable JSON logs in production.
-   **Type Safety**: Fully typed codebase with `mypy` strict mode support.
