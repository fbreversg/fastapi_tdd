import uvicorn                  # Not for production
from fastapi import FastAPI, Depends

from app.config import get_settings, Settings

app = FastAPI()


@app.get('/ping')
async def pong(settings: Settings = Depends(get_settings)):
    return {"ping": "pong!",
            "environment": settings.environment,
            "testing": settings.testing
            }


# Not for production
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
