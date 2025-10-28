from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    username: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class LoginRequest(BaseModel):
    username: str
    password: str
