from returns.pipeline import is_successful
import strawberry

from placeNoteApi2024.controller.account_user_controller import (
    get_account_user_by_id_handler,
)
from placeNoteApi2024.graphql.strawberry_object import (
    AccountUserResponse,
)
from placeNoteApi2024.service.account_user_service import (
    get_user_account_id_from_context_dict,
)


@strawberry.type
class PlaceNoteQuery:
    @strawberry.field
    def get_account_user_by_token(self, info: strawberry.Info) -> AccountUserResponse:
        user_account_id = get_user_account_id_from_context_dict(info.context)
        result = get_account_user_by_id_handler(user_account_id)
        if is_successful(result):
            return result.unwrap()
        else:
            return result.failure()
