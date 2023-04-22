
from fastapi import FastAPI

from routers import home


app = FastAPI()

app.include_router(home.router)

@app.get('/')
async def health_check():
    return 'Healthy'