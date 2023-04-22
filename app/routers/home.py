
from fastapi import APIRouter


router = APIRouter(prefix="/home", tags=["Home"])

@router.get("")
async def index():
    return {'version':'0.0.1','author':'vuongnv'}