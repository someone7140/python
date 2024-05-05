from typing import List
from returns.pipeline import is_successful
import strawberry

from placeNoteApi2024.controller.account_user_controller import (
    get_account_user_by_id_handler,
)
from placeNoteApi2024.controller.post.post_category_controller import (
    get_post_categories_handler,
    get_post_category_by_id_handler,
)
from placeNoteApi2024.controller.post.post_place_controller import (
    get_lat_lon_from_address,
    get_post_places_handler,
)
from placeNoteApi2024.graphql.strawberry_object import (
    AccountUserResponse,
    LatLonResponse,
    PostCategoryResponse,
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

    @strawberry.field
    def get_my_post_categories(
        self, info: strawberry.Info, name_filter: str | None
    ) -> List[PostCategoryResponse]:
        user_account_id = get_user_account_id_from_context_dict(info.context)
        result = get_post_categories_handler(user_account_id, name_filter)
        if is_successful(result):
            return result.unwrap()
        else:
            return result.failure()

    @strawberry.field
    def get_my_post_category_by_id(
        self, info: strawberry.Info, id_filter: str
    ) -> PostCategoryResponse:
        user_account_id = get_user_account_id_from_context_dict(info.context)
        result = get_post_category_by_id_handler(user_account_id, id_filter)
        if is_successful(result):
            return result.unwrap()
        else:
            return result.failure()

    @strawberry.field
    def get_post_places(
        self,
        info: strawberry.Info,
        id_filter: str | None,
        category_filter: str | None,
    ) -> PostCategoryResponse:
        user_account_id = get_user_account_id_from_context_dict(info.context)
        result = get_post_places_handler(user_account_id, id_filter, category_filter)
        if is_successful(result):
            return result.unwrap()
        else:
            return result.failure()

    @strawberry.field
    def get_lat_lon_from_address(
        self, info: strawberry.Info, address: str
    ) -> LatLonResponse | None:
        # 認証済みのユーザのみ使えるようにする
        get_user_account_id_from_context_dict(info.context)
        result = get_lat_lon_from_address(address)
        if is_successful(result):
            return result.unwrap()
        else:
            return result.failure()
