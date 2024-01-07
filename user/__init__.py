from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    name: str
    surname: str = None
    email: str
    password: str
    city: str = None
    birthday: str = None
    profile_photo: str = None
    reg_date: datetime


