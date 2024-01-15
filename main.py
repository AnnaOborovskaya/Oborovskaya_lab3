from fastapi import FastAPI, Path, Response, Query, Body, Header
from public.users import users_router
from typing import Union
from pydantic import BaseModel
from fastapi.responses import HTMLResponse, PlainTextResponse


app = FastAPI()
app.include_router(users_router)

@app.get('/', response_class=PlainTextResponse)
def func_1():
    html_content = f"<b>Welcome to this page!</b>"
    return HTMLResponse(content=html_content)

