from __future__ import annotations

import logging

from fastapi import Request, FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from shared.errors.exceptions import ResponseException
from shared.errors.responses import BAD_REQUEST_ERROR

logger = logging.getLogger(__name__)


def register_error_handlers(app: FastAPI) -> None:
    @app.exception_handler(RequestValidationError)
    async def handle_request_errors(_: Request, e: RequestValidationError) -> JSONResponse:

        error = BAD_REQUEST_ERROR.with_message(str(e))

        return JSONResponse(
            status_code=error.http_status,
            content=error.dict(),
        )

    @app.exception_handler(ResponseException)
    async def handle_custom_errors(_: Request, e: ResponseException) -> JSONResponse:
        return JSONResponse(
            status_code=e.error.http_status,
            content=e.error.model_dump(),
        )
