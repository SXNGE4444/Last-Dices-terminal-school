from fastapi import FastAPI

app = FastAPI(title="LAST DICES Terminal School Local API")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "mode": "local"}
