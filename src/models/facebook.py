from typing import Optional

from pydantic import BaseModel, Field


class FacebookPageSchema(BaseModel):
    Name: str = Field(...)
    About: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "Name": "name of the page",
                "About": "page descirption"
            }
        }


class UpdateFacebookModel(BaseModel):
    Name: Optional[str]
    About: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "Name": "name of the page",
                "About": "page descirption"
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
