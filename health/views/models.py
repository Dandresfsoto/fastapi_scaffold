from pydantic import BaseModel


class HealthDTO(BaseModel):  # type: ignore
    message: str

    class Config:
        allow_mutation = False
