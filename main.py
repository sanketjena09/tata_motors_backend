from fastapi import FastAPI
import uvicorn
from api import api_router

from pydantic import AnyHttpUrl
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(title='Monalisha Motors',debug=True)

app.include_router(api_router, prefix="/api")

BACKEND_CORS_ORIGIN : list[AnyHttpUrl] = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in BACKEND_CORS_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == '__main__':
    uvicorn.run(app=app,host = '127.0.0.1',port=8005)
