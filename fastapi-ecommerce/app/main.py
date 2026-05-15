from fastapi import FastAPI, HTTPException, Query
from services.products import get_products
# from typing import List, Dict, Any

app = FastAPI()

@app.get("/")
def root():
    return "Welcome to fast-api"

# dynamic route

@app.get("/products")
def product():
    return get_products()

# Query
@app.get("/items")
def list_product(
    name:str = Query(
        default=None,
        min=1,
        max=50,
        description="Search by product name(case_sensitive)"
    )
):
    return name