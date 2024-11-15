from typing import Annotated, List
from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/users")
async def users_list() -> List[User]:
    return users


@app.post("/user/{username}/{age}")
async def add_user(
        username: Annotated[str, Path(min_length=4, max_length=15, description='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=100, description='Enter age', example='42')]) -> User:
    if users:
        user_id = max(users, key=lambda x: int(x.id)).id + 1
    else:
        user_id = 1
    user = User(id=user_id, username=username, age=age)
    users.append(user)
    return user


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
        user_id: Annotated[int, Path(ge=1, le=100, description='Enter user id', example='42')],
        username: Annotated[str, Path(min_length=4, max_length=15, description='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=100, description='Enter age', example='42')]) -> User:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail='User was not found.')


@app.delete("/user/{user_id}")
async def delete_user(
        user_id: Annotated[int, Path(ge=1, le=100, description='Enter user id', example='42')]) -> User:
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail='User was not found.')
