from fastapi import FastAPI, HTTPException, Query
from services.products import get_products
from typing import Any

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
) -> dict[str, Any]:
    
    products = product()

    if name:
        p_name = name.strip().lower()
        products = [p for p in products if p_name in p.get("name", "").lower()]

        if not products:
            raise HTTPException(
                status_code=404,
                detail=f"No product found matching name={name}"
            )         
    return {"total": len(products), "items": products}
