import secrets
import string
import uuid

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from schemas import LoginRequest, UserObj, LoginResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PATCH", "OPTIONS", "get", "post", "patch", "options"],
    allow_headers=['content-disposition', 'accept-encoding', 'origin',
                   'content-type', 'accept', 'authorization',
                   'access-control-allow-methods', 'access-control-allow-origin', 'set-cookie',
                   'Content-Disposition', 'Accept-Encoding', 'Origin',
                   'Content-Type', 'Accept', 'Authorization',
                   'Access-Control-Allow-Methods', 'Access-Control-Allow-Origin', 'Set-Cookie']
)


def get_token():
    alphabet = string.ascii_letters + string.digits
    token = ''.join(secrets.choice(alphabet) for i in range(200))
    return token


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post(
    path='/login/',
    response_model=LoginResponse,
    status_code=200
)
def fake_login(
        request: LoginRequest
):
    token = get_token()
    user = UserObj(
        email='some_email@example.com',
        person=uuid.uuid4(),
        company_id='d7a2f439-9600-4b64-ae31-d451362b8551',
    )
    data = LoginResponse(
        token=token,
        user=user
    )
    response = JSONResponse(content=data, status_code=200)
    response.set_cookie(key='login_token', value=token)
    return response


if __name__ == "__main__":
    uvicorn.run("main:app", port=4001, reload=True, access_log=False)
