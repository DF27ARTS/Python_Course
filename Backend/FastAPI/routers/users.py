
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"message": "No encontrado"}}
)


class User(BaseModel):
    id: int
    name: str
    lastname: str
    url: str
    age: int


users_list = [
    User(id=1, name="Tom", lastname="Holland", url="http://tom.com", age=25),
    User(id=2, name="Tom", lastname="Holland", url="http://tom.com", age=25),
    User(id=3, name="Tom", lastname="Holland", url="http://tom.com", age=25)
]


@router.get("/json")
async def usersjson():
    return [
        {"name": "Tom", "lastname": "Holland", "url": "http://tom.com", "age": 25},
        {"name": "Tom", "lastname": "Holland", "url": "http://tom.com", "age": 25},
        {"name": "Tom", "lastname": "Holland", "url": "http://tom.com", "age": 25},
    ]


@router.get("/")
async def users():
    return users_list


@router.get("/{id}")
async def user(id: int):
    return search_user(id)


@router.get("/query")
async def user(id: int):
    return search_user(id)


@router.post("/", response_model=User, status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")

    users_list.append(user)
    return user


@router.put("/")
async def user_put(user: User):

    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        raise HTTPException(
            status_code=404, detail="No se a actualizado el usuario")
    return user


@router.delete("/{id}")
async def delete_user(id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
    if not found:
        raise HTTPException(
            status_code=404, detail="No se a eliminado el usuario")
    return {"message": "User deleted"}


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se a encontrado el usuario"}
