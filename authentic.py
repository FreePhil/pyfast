import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Annotated

app = FastAPI()

secret_user: str = 'new'
secret_password: str = 'who'

basic: HTTPBasicCredentials = HTTPBasic()


@app.get("/who")
def get_user(creds: Annotated[HTTPBasicCredentials, Depends(basic)]) -> dict:
    if creds.username == secret_user and creds.password == secret_password:
        return {'username': creds.username, 'password': creds.password}
    raise HTTPException(status_code=401, detail='Hey!')


if __name__ == '__main__':
    uvicorn.run('authentic:app', reload=True)