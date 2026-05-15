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
    name : str = Query(
        default=None,
        min_length=1,
        max_length=50,
        description="Search by product name(case_sensitive)"
    ),
    sort_by_price : bool = Query(
        default=False,
        description="Sort products by price"
    ),
    order : str = Query(
        default="asc",
        description="Sort Order when sort by prices(asc,desc)"
    ),
    limit : int = Query(
        default = 3,
        description="Sets a product_show limit for better readability"
    ),
    offset : int = Query(
        default = 0,
        description = "Sets a product_show pagination for start pagination offset"
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

    if sort_by_price:
        reverse = order == "desc"
        products = (sorted(products, key=lambda p:p.get("price",0), reverse = reverse))  

    total = len(products)
    products = products[offset:(offset+limit)]  

    return {"total": total, "items": products}


@app.get("/products/{product_id}")
def get_product_by_id(product_id:str):
    products = get_products()
    for product in products:
        if product["id"] == product_id:
            return product
    raise HTTPException(
        status_code=404,
        detail= f"Product for the matching id:{product_id} not found"
    )

