from typing import Union, Annotated
from pydantic import BaseModel, Field

class Main_User(BaseModel):
    name: Union[str, None] = None
    id: Annotated[Union[int, None], Field(default=100, ge=1, lt=288)] = None

class Main_UserDB(Main_User):
    password: Annotated[Union[str, None], Field(min_length=8, max_length=20)] = None

class New_Respons(BaseModel):
    message: str