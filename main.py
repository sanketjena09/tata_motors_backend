from fastapi import FastAPI
import uvicorn
from api import api_router

app = FastAPI(title='Monalisha Motors',debug=True)

app.include_router(api_router, prefix="/api")

if __name__ == '__main__':
    uvicorn.run(app=app,host = '127.0.0.1',port=8005)
