# models.py
from pydantic import BaseModel, ConfigDict, field_validator

class Post(BaseModel):
    model_config = ConfigDict(extra="forbid")   # extra fields become errors

    userId: int
    id: int
    title: str
    body: str

    @field_validator("title")
    @classmethod
    def title_not_blank(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("title must not be blank")
        return v
