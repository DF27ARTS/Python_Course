
# Main page Backend

from fastapi import FastAPI
from routers import products, users, basic_auth_users, jwt_auth_users, users_db
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(users.router)

app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)
app.include_router(users_db.router)
app.mount("/static", StaticFiles(directory="static"), name="static")


# pip install "fastapi[all]"
# Url local: http://127.0.0.1:8000
# Inicia el server: uvicorn main:app --reaload
# Detener el server: ATRL + C

""" Authentication """
# pip install "python-jose[cryptography]"
# pip install "passlib[bcrypt]


""" Create random number"""
# openssl rand -hex 32


@app.get("/")
async def hello():
    return "¡Hola FastAPI!"


@app.get("/url")
async def url():
    return {"url_api": "https://unsplash.it"}

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc
