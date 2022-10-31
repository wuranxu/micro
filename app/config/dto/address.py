from klose.excpetions.ParamsException import ParamsError
from pydantic import validator, BaseModel


class PityAddressForm(BaseModel):
    id: int = None
    env: int = None
    name: str = ''
    gateway: str = ''

    @validator('gateway', whole=True)
    def prefix_match(cls, v):
        if not v.startswith(("http://", "https://", "ws://", "wss://")):
            raise ParamsError("前缀不为http或ws")
        return v


class CustomDto(BaseModel):
    id: int


class PityGatewayDto(BaseModel):
    name: str = ''
    env: int = None
    gateway: str = ""
