from typing import Annotated
from fastapi import FastAPI, Path

app = FastAPI()

users = {1: 'Имя: Example, возраст: 18'}


@app.get("/users")
async def users_list():
    return users


@app.post("/user/{username}/{age}")
async def add_user(
        username: Annotated[str, Path(min_length=4, max_length=15, description='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=100, description='Enter age', example='42')]):
    user_id = len(users)+1
    users.update({user_id: f"Имя: {username}, возраст: {age}"})
    return f'User {user_id} is registered.'


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
        user_id: Annotated[int, Path(ge=1, le=100, description='Enter user id', example='42')],
        username: Annotated[str, Path(min_length=4, max_length=15, description='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=100, description='Enter age', example='42')]):
    users[user_id] = f'Имя: {username}, возраст: {age}.'
    return f'The user {user_id} is updated.'


@app.delete("/user/{user_id}")
async def delete_user(
        user_id: Annotated[int, Path(ge=1, le=100, description='Enter user id', example='42')]):
    users.pop(user_id)
    return f'User {user_id} has been deleted.'
