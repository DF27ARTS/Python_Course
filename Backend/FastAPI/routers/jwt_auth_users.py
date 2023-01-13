
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1
SECRETE = "b4222d32454fda8f6f601d54978fc932a85413d0b6a47c6f61a93e39fd81bcaa"

router = APIRouter(
    prefix="/jwtauth",
    tags=["jwtauth"],
    responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}}
)

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])


class User(BaseModel):
    username: str
    full_name: str
    email: str
    desable: int


class UserDB(User):
    password: str


users_db = {
    "Tom": {
        "username": "Tom",
        "full_name": "Tom Holland",
        "email": "tom@gmail.com",
        "desable": False,
        "password": "$2a$12$3bxxUIOOh0DYVHVhrI0kmePmRGeJwyq4kx86EfpaGh2TNgUKUMlJi"
    },
    "Tom2": {
        "username": "Tom2",
        "full_name": "Tom2 Holland",
        "email": "tom2@gmail.com",
        "desable": True,
        "password": "$2a$12$uTH8tL.9R9oLVgB73kBVY.3wL7DswtrS4AEJ830tAadvEND9rls/q"
    }
}


def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])


def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])


async def auth_user(token: str = Depends(oauth2)):
    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales de autenticacion invalidas",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        username = jwt.decode(token, SECRETE, algorithms=ALGORITHM).get("sub")
        if username is None:
            raise exception

    except JWTError:
        raise exception

    return search_user(username)


async def current_user(user: User = Depends(auth_user)):
    if user.desable:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuarion inactivo",
            headers={"WWW-Authenticate": "Bearer"}
        )

    return user


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")

    user = search_user_db(form.username)

    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="La contraseña no es correcta")

    access_token = {
        "sub": user.username,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)
    }

    return {"acces_token": jwt.encode(access_token, SECRETE, algorithm=ALGORITHM), "token_type": "bearer"}


@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user
