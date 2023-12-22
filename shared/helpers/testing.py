import unittest

from httpx import Response

from shared.errors.models import ErrorDTO


def assert_expected_response_error(
        self: unittest.TestCase,
        response: Response,
        expected_error: ErrorDTO,
) -> None:
    self.assertEqual(expected_error.http_status, response.status_code)

    response_error = response.json()

    self.assertEqual(expected_error.http_status, response_error['http_status'])
    self.assertEqual(expected_error.code, response_error['code'])
    self.assertEqual(expected_error.message, response_error['message'])
