"""
Pydantic — это библиотека, которая обеспечивает проведение валидации данных и управление настройками с помощью
аннотаций типов.
"""


from pydantic import BaseModel, validator, ValidationError, Field


class Data(BaseModel):
    id: int
    email: str = Field(min_length=5)  # Встроенный валидатор
    first_name: str
    last_name: str
    avatar: str

    @validator("id")  # Собственный валидатор
    def check_id_is_not_negative(cls, user_id):
        if user_id < 0:
            raise ValidationError("ID value cannot be negative")
        else:
            return user_id


class Support(BaseModel):
    url: str
    text: str


class User(BaseModel):
    data: Data
    support: Support
