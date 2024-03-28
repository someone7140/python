import strawberry
from returns.pipeline import is_successful

from placeNoteApi2024.controller.account_user_controller import (
    add_account_user_by_google,
)
from placeNoteApi2024.graphql.strawberry_object import AddAccountUserResponse


@strawberry.type
class PlaceNoteMutation:
    @strawberry.mutation
    def add_account_user_by_google(
        user_setting_id: str, name: str, gmail: str | None
    ) -> AddAccountUserResponse:
        result = add_account_user_by_google(user_setting_id, name, gmail)
        aaa = result.unwrap()
        if is_successful(result):
            return result.unwrap()
        else:
            return result.failure()
