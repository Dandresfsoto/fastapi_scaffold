import unittest

from fastapi import status

from shared.errors.models import ErrorDTO


class ErrorDTOTestCase(unittest.TestCase):
    def test_with_message_creates_a_new_dto_with_the_given_message(self) -> None:
        status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        code = 100
        original_message = 'original message'

        original_error = ErrorDTO(http_status=status_code, code=code, message=original_message)

        new_message = 'new message'
        new_error = original_error.with_message(new_message)

        self.assert_expected_error_dto(new_error, status_code, code, new_message)
        self.assert_expected_error_dto(original_error, status_code, code, original_message)

    def assert_expected_error_dto(
            self,
            error: ErrorDTO,
            expected_status: int,
            expected_code: int,
            expected_message: str,
    ) -> None:
        self.assertEqual(expected_status, error.http_status)
        self.assertEqual(expected_code, error.code)
        self.assertEqual(expected_message, error.message)
