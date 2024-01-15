import uuid
from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse, FileResponse
from models.model import Main_User, Main_UserDB, New_Respons
import hashlib
from typing import Union, Annotated

users_router = APIRouter()

def coder_password(cod: str):
    result = cod*2


users_list = [Main_UserDB(name='Ivanov', id=188, password='12345678'), Main_UserDB(name="Petrov", id=134, password="01234567")]


def find_user(id: int) -> Union [Main_UserDB, Main_UserDB, None]:
    for user in users_list:
        if user.id == id:
            return user
    return None

@users_router.get("/api/users", response_model=Union[list[Main_User], list[Main_UserDB], None])
def get_users():
    """Вывод всех пользователей"""
    return users_list

@users_router.get("/api/users/{id}", response_model=Union [Main_User, Main_UserDB, New_Respons])
def get_user(id: int):
    """Найти пользователя по ID"""
    user = find_user(id)
    print(user)
    if user == None:
        return New_Respons(message="Пользователь не найден")
    return user

@users_router.post("/api/users", response_model=Union[Main_User, Main_UserDB, New_Respons])
def create_user(item: Annotated[Main_User, Main_UserDB, Body(embed=True, description="Новый пользователь")]):
    """Добавить нового пользователя"""
    user = Main_UserDB(name=item.name, id=item.id, password=item.password)
    users_list.append(user)
    return user


@users_router.put("/api/users", response_model=Union[Main_User, Main_UserDB, New_Respons])
def edit_person(item: Annotated[Main_User, Main_UserDB, Body(embed=True, description="Изменяем данные для пользователя по id")]):
    """Отредактировать данные пользователя по ID"""
    user = find_user(item.id)
    if user == None:
        return New_Respons(message="Пользователь не найден")
    user.id = item.id
    user.name = item.name
    user.password = item.password
    return user

@users_router.delete("/api/users/{id}", response_model=Union[list[Main_User], list[Main_UserDB], None])
def delete_person(id: int):
    """Удалить пользователя"""
    user = find_user(id)
    if user == None:
        return New_Respons (message= "Пользователь не найден")

    users_list.remove(user)
    return users_list