from pickletools import int4
from pydantic import BaseModel, EmailStr, field_validator

class User(BaseModel):
    name:str
    age: int

    @field_validator('age')
    @classmethod
    def validate_age(cls,value):
        if value <= 0:
            raise ValueError(f"age must be postive: {value}")
        return value



