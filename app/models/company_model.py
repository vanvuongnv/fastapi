from typing import Optional
from pydantic import BaseModel, Field


class CompanyModel(BaseModel):
    name: str
    description: Optional[str]
    mode: int = Field(ge=0,le=3,default=0)
    rating: int = Field(ge=0,le=5,default=0)