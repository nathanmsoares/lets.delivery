from typing import List
from fastapi import Body
from pydantic import BaseModel, Field


class Cat(BaseModel):
    name: str = Field(..., max_length=50, description="Cat's name")
    breed: str = Field(..., max_length=300, description="Cat's breed")
    location_of_origin: str = Field(..., max_length=150,
                                    description="Cat's location of origin")
    coat_length: float = Field(..., gt=0, description="Cat's coat length")
    body_type: str = Field(..., max_length=50, description="Cat's body type")
    pattern: str = Field(..., max_length=50, description="Cat's pattern")


class BaseM(BaseModel):
    list_of_cats: List[Cat] = Body(...)
