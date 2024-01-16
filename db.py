from config import settings
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_session
from models.model import *
#from sqlalchemy import Column, String, Integer, Sequence, insert, select
#from sqlalchemy import create_engine, text
#from sqlalchemy import create_engine, text
#from sqlalchemy.orm import declarative_base
#import asyncio



#ur_p = "postgresql+asyncpg://postgres:61891@localhost:5432/Shop"

ur_a = settings.POSTGRES_DATABASE_URLA

engine_s = create_async_engine(ur_a, echo=True)

async def create_tables():
    #Base.metadata.drop_all(bind=engine_s)
    Base.metadata.create_all(bind=engine_s)

# def f():
#     with engine_s.connect() as conn:
#         answer = conn.execute(text("select * from users;"))
#         print(f"answer = {answer.all()}")
#
# def f_builder(): #хз
#     with engine_s.connect() as conn:
#         query = insert(User).values([
#             {"name": "Koval", "password": "112233"}
#         ])
#         conn.execute(query)
#         conn.execute(text('commit;'))
#         query = select(User)
#         answer = conn.execute(query)
#         print(f"answer = {answer.all()}")