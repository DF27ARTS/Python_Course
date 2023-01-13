
from fastapi import APIRouter
# from routers import products

router = APIRouter(
    prefix="/products",
    tags=["products"],
    responses={404: {"message": "No encontrado"}}
)

products_list = ["products1", "products2",
                 "products3", "products4", "products5"]


@router.get("/")
async def products():
    return ["products1", "products2", "products3", "products4", "products5"]


@router.get("/{id}")
async def products(id: int):
    return products_list[id]
