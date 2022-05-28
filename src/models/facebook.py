from typing import Optional

from pydantic import BaseModel, Field


class FacebookPageSchema(BaseModel):
    page_name: str = Field(...)
    number_follower: int = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "page_name": "Cr7",
                "number_follower": 100
            }
        }


class UpdateFacebookModel(BaseModel):
    page_name: Optional[str]
    number_follower: Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "page_name": "Cr7",
                "number_follower": 100
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
