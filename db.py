#from config import settings
from sqlalchemy import Column, String, Integer, Sequence
from sqlalchemy import create_engine, text
from models.model import Main_User, Main_UserDB, New_Respons
from sqlalchemy.orm import declarative_base
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_session
#from models.good import Main User, New Respons, Tags, User, Base
#import psycopg

from sqlalchemy import create_engine, text

#определяем параметры для подключения

#settings.DATABASE URL = 'sqlite:///./test02.db

#engine = create_engine (settings.POSTGRES_DATABASE_URL)

ur_p = "postgresql+asyncpg://postgres:61891@localhost:5432/Shop"

#engine = create_engine(ur_p, echo=True)

engine = create_async_engine(ur_p, echo=True)
#SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def f():
    async with engine.connect() as conn:
        answer = await conn.execute(text("select version()"))
        print(f"answer = {answer.all()}")

#asyncio.run(f())
asyncio.get_event_loop().run_until_complete(f())