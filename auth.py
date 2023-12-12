import uvicorn
from fastapi import Depends, FastAPI
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Annotated

app = FastAPI()
basic = HTTPBasic()


@app.get('/hello')
def get_hello():
    return {'message': 'Hello World!'}


@app.get("/who")
def get_user(credentials: Annotated[HTTPBasicCredentials, Depends(basic)]):
    return {'username': credentials.username, 'password': credentials.password}


if __name__ == '__main__':
    uvicorn.run('auth:app', reload=True)