from uuid import UUID

from pydantic import BaseModel


class LoginRequest(BaseModel):
    login: str
    email: str
    password: str


class UserObj(BaseModel):
    email: str
    person: UUID
    company_id: UUID


class LoginResponse(BaseModel):
    token: str
    user: UserObj
