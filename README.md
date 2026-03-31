# umaguedo-search

A multimodal domain-specific assistant for Umamusume.

## Running locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`. Check health at `GET /health`.

## Running with Docker

```bash
docker build -t umaguedo-search .
docker run -p 8000:8000 umaguedo-search
```

## Running tests

```bash
pytest
```
