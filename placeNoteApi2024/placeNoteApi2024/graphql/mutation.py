import strawberry
from returns.pipeline import is_successful

from placeNoteApi2024.controller.account_user_controller import (
    add_account_user_by_google,
    google_auth_code_verify,
)
from placeNoteApi2024.graphql.strawberry_object import (
    AddAccountUserResponse,
    GoogleAuthCodeVerifyResponse,
)


@strawberry.type
class PlaceNoteMutation:
    @strawberry.mutation
    def google_auth_code_verify(auth_code: str) -> GoogleAuthCodeVerifyResponse:
        result = google_auth_code_verify(auth_code)
        if is_successful(result):
            return result.unwrap()
        else:
            return result.failure()

    @strawberry.mutation
    def add_account_user_by_google(
        user_setting_id: str, name: str, auth_token: str
    ) -> AddAccountUserResponse:
        result = add_account_user_by_google(auth_token, user_setting_id, name)
        if is_successful(result):
            return result.unwrap()
        else:
            return result.failure()
