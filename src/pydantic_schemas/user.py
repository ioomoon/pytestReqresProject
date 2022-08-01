"""
Pydantic — это библиотека, которая обеспечивает проведение валидации данных и управление настройками с помощью
аннотаций типов.
"""


from pydantic import BaseModel, validator, ValidationError, Field
from src.enums.user_enums import UserErrors


class Data(BaseModel):
    id: int
    email: str = Field(min_length=5)  # Встроенный валидатор
    first_name: str
    last_name: str
    avatar: str = ""  # Необязательное поле

    @validator("id")  # Собственный валидатор
    def check_id_is_not_negative(cls, user_id):
        if user_id < 0:
            raise ValidationError("ID value cannot be negative")
        else:
            return user_id

    @validator("email")
    def check_dog_in_email(cls, user_email):
        if '@' in user_email:
            return user_email
        else:
            raise ValueError(UserErrors.WRONG_EMAIL.value)


class Support(BaseModel):
    url: str
    text: str


class User(BaseModel):
    data: Data
    support: Support
