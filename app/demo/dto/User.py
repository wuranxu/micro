from pydantic import BaseModel, EmailStr


class UserInfo(BaseModel):
    role: int
    name: str
    email: str
    id: int = None


class UserLoginRequest(BaseModel):
    username: str
    password: str


class UserRegisterRequest(BaseModel):
    name: str
    password: str
    username: str
    email: EmailStr


class UserQueryRequest(BaseModel):
    token: str


class ResetPwdForm(BaseModel):
    password: str
    token: str


class GenerateUrlRequest(BaseModel):
    email: EmailStr


class UserUpdateForm(BaseModel):
    id: int
    name: str = None
    email: str = None
    phone: str = None
    role: int = None
    is_valid: bool = None


class GithubLoginCode(BaseModel):
    code: str


class CustomDto(BaseModel):
    """只包含id的form
    """
    id: int


class CheckTokenDto(BaseModel):
    token: str
