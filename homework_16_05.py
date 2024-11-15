from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()
templates = Jinja2Templates(directory='templates')

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/")
async def main_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get("/user/{user_id}")
async def user_page(request: Request,
                    user_id: Annotated[int, Path(ge=1, le=100,
                                                 description='Enter User ID',
                                                 example='42')]) -> HTMLResponse:
    for user in users:
        if int(user.id) == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": user})
    raise HTTPException(status_code=404, detail='User was not found.')


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
