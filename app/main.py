from fastapi import FastAPI

app = FastAPI(title="umaguedo-search")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
