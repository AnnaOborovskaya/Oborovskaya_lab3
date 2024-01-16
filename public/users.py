from fastapi import APIRouter, Depends, Body, HTTPException
from fastapi.responses import JSONResponse
from starlette import status
from models.model import *
from sqlalchemy.orm import sessionmaker, Session
from db import engine_s


# users_list = [Main_UserDB(name='Ivanov', password='12345678'), Main_UserDB(name="Petrov", password="01234567")]

async def get_session():
    with Session(engine_s) as session:
        try:
            yield session
        finally:
            session.close()

#users_router = APIRouter(tags=[Tags.users], prefix="/api/users")
#info_router = APIRouter(tags=[Tags.info])
users_router = APIRouter()


async def coder_password(cod: str):
    return cod*2

#@users_router.get("/", response_model=Union[list[Main_User], New_Respons], tags=[Tags.users])
@users_router.get("/api/users", response_model=Union[list[Main_User], list[Main_UserDB], None])
async def get_user_db(DB: Session = Depends(get_session)):
    '''получаем все записи таблицы'''
    users = DB.query(User).all()
    if users == None:
        return JSONResponse(status_code=404, content={"message": "Пользователи не найдены"})

#@users_router.get("/{id}", response_model=Union[New_Respons, Main_User], tags=[Tags.info])
@users_router.get("/api/users/{id}", response_model=Union [Main_User, Main_UserDB, New_Respons])
async def get_user_(id: int, DB: Session = Depends(get_session)):
    """получаем пользователя по id"""
    user = DB.query(User).filter(User.id == id).first()
    if user == None:
        return JSONResponse(status_code=484, content={"message": "Пользователь не найден"})
    else:
        return user


#@users_router.post("/", response_model=Union[Main_User, New_Respons], tags=[Tags.users], status_code=status.HTTP_201_CREATED)
@users_router.post("/api/users", response_model=Union[Main_User, Main_UserDB, New_Respons])
async def create_user(item: Annotated[Main_User, Body(embell=True, description="Новый пользователь")], DB: Session = Depends(get_session)):
    try:
        user = User(name=item.name, password=coder_password(item.name))
        if user is None:
            raise HTTPException(status_code=404, detail="Объект не определен")
        DB.add(user)
        DB.commit()
        DB.refresh(user)
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Произошла ошибка при добавлении объекта {user}")

#@users_router.put("/", response_model=Union[Main_User, New_Respons], tags=[Tags.users])
@users_router.put("/api/users", response_model=Union[Main_User, Main_UserDB, New_Respons])
async def edit_user_(item: Annotated[Main_User, Body(embed=True, description="Изменяем данные для пользователя по id")], DB: Session = Depends(get_session)):
    user = DB.query(User).filter(User.id == item.id).first()
    if user == None:
        return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})
    user.name = item.name
    try:
        DB.commit()
        DB.refresh(user)
    except HTTPException:
        return JSONResponse(status_code=404, content={"message": ""})
    return user

#@users_router.delete("/{id}", response_class=JSONResponse, tags=[Tags.users])
@users_router.delete("/api/users/{id}", response_model=Union[list[Main_User], list[Main_UserDB], None])
async def delete_user(id: int, DB: Session = Depends(get_session)):
    user = DB.query(User).filter(User.id == id).first()
    if user == None:
        return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})
    try:
        DB.delete(user)
        DB.commit()
    except HTTPException:
        JSONResponse(content={'message': f'Ошибка'})
    return JSONResponse(content={'message': f'Пользователь удалён {id}'})


#
# def find_user(id: int) -> Union[Main_UserDB, Main_UserDB, None]:
#     for user in users_list:
#         if user.id == id:
#             return user
#     return None

#@users_router.get("/api/users", response_model=Union[list[Main_User], list[Main_UserDB], None])
#def get_users():
#    """Вывод всех пользователей"""
#    return users_list

#@users_router.get("/api/users/{id}", response_model=Union [Main_User, Main_UserDB, New_Respons])
#def get_user(id: int):
#    """Найти пользователя по ID"""
#    user = find_user(id)
#    print(user)
#    if user == None:
#        return New_Respons(message="Пользователь не найден")
#    return user

#@users_router.post("/api/users", response_model=Union[Main_User, Main_UserDB, New_Respons])
#def create_user(item: Annotated[Main_User, Main_UserDB, Body(embed=True, description="Новый пользователь")]):
#    """Добавить нового пользователя"""
#    user = Main_UserDB(name=item.name, id=item.id, password=item.password)
#    users_list.append(user)
#    return user


#@users_router.put("/api/users", response_model=Union[Main_User, Main_UserDB, New_Respons])
#def edit_person(item: Annotated[Main_User, Main_UserDB, Body(embed=True, description="Изменяем данные для пользователя по id")]):
#    """Отредактировать данные пользователя по ID"""
#    user = find_user(item.id)
#    if user == None:
#        return New_Respons(message="Пользователь не найден")
#    user.id = item.id
#    user.name = item.name
#    user.password = item.password
#    return user

#@users_router.delete("/api/users/{id}", response_model=Union[list[Main_User], list[Main_UserDB], None])
#def delete_person(id: int):
#    """Удалить пользователя"""
#    user = find_user(id)
#    if user == None:
#        return New_Respons (message= "Пользователь не найден")

#    users_list.remove(user)
#    return users_list