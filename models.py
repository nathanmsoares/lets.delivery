from typing import List, Optional
from fastapi import FastAPI, Body
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = []

class BaseM(BaseModel):
    list_of_cats: List[Item] = Body(...)