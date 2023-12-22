from __future__ import annotations

from pydantic import BaseModel


class ErrorDTO(BaseModel):  # type: ignore
    http_status: int
    code: int
    message: str

    class Config:
        allow_mutation = False

    def with_message(self, message: str) -> ErrorDTO:
        return ErrorDTO(http_status=self.http_status, code=self.code, message=message)
