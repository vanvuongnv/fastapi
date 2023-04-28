
from fastapi import FastAPI
from routers import task, company, auth

from routers import home


app = FastAPI()

app.include_router(home.router)
app.include_router(auth.router)
app.include_router(company.router)
app.include_router(task.router)

@app.get('/')
async def health_check():
    return 'Healthy'