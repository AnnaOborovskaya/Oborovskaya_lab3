from config import settings
from sqlalchemy import Column, String, Integer, Sequence, insert, select
from sqlalchemy import create_engine, text
from models.model import *
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

ur_s = settings.POSTGRES_DATABASE_URLS
ur_a = settings.POSTGRES_DATABASE_URLA



#engine = create_engine(ur_p, echo=True)

engine_s = create_async_engine(ur_a, echo=True)
#SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

def create_tables():
    Base.metadata.drop_all(bind=engine_s)
    Base.metadata.create_all(bind=engine_s)

def f():
    with engine_s.connect() as conn:
        answer = conn.execute(text("select * from users;"))
        print(f"answer = {answer.all()}")

def f_builder():
    with engine_s.connect() as conn:
        query = insert(User).values([
            {"name": "Koval", "password": "112233"}
        ])
        conn.execute(query)
        conn.execute(text('commit;'))
        query = select(User)
        answer = conn.execute(query)
        print(f"answer = {answer.all()}")


#asyncio.run(f())
#asyncio.get_event_loop().run_until_complete(f())