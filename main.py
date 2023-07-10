import secrets
import string
import uuid

import uvicorn
from fastapi import FastAPI

from schemas import LoginRequest, UserObj, LoginResponse

app = FastAPI()


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
    user = UserObj(
        email='some_email@example.com',
        person=uuid.uuid4(),
        company_id='d7a2f439-9600-4b64-ae31-d451362b8551',
    )
    data = LoginResponse(
        token=get_token(),
        user=user
    )
    return data


if __name__ == "__main__":
    uvicorn.run("main:app", port=4001, reload=True, access_log=False)
