# fastapi
FastAPI framework, high performance, easy to learn, fast to code, ready for production

# setup local
- Setup postgesql database
- Edit env file
- Run pip install -r requirements.txt 
# migration
- alembic revision -m "REVISION DESCRIPTION"
- alembic upgrade head

# run
- cd ./app
- uvicorn main:app --reload
- api docs: http://127.0.0.1:8000/docs