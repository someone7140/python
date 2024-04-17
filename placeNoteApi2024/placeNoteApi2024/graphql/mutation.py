from returns.pipeline import is_successful
import strawberry

from placeNoteApi2024.controller.account_user_controller import (
    add_account_user_by_google_handler,
    google_auth_code_verify_handler,
    login_by_google_auth_code_handler,
)
from placeNoteApi2024.graphql.strawberry_object import (
    AccountUserResponse,
    GoogleAuthCodeVerifyResponse,
)


@strawberry.type
class PlaceNoteMutation:
    @strawberry.mutation
    def google_auth_code_verify(auth_code: str) -> GoogleAuthCodeVerifyResponse:
        result = google_auth_code_verify_handler(auth_code)
        if is_successful(result):
            return result.unwrap()
        else:
            return result.failure()

    @strawberry.mutation
    def add_account_user_by_google(
        user_setting_id: str, name: str, auth_token: str
    ) -> AccountUserResponse:
        result = add_account_user_by_google_handler(auth_token, user_setting_id, name)
        if is_successful(result):
            return result.unwrap()
        else:
            return result.failure()

    @strawberry.mutation
    def login_by_google_auth_code(auth_code: str) -> AccountUserResponse:
        result = login_by_google_auth_code_handler(auth_code)
        if is_successful(result):
            return result.unwrap()
        else:
            return result.failure()
