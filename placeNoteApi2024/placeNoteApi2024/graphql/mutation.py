from typing import List
from returns.pipeline import is_successful
import strawberry

from placeNoteApi2024.controller.account_user_controller import (
    add_account_user_by_google_handler,
    google_auth_code_verify_handler,
    login_by_google_auth_code_handler,
)
from placeNoteApi2024.controller.post.post_category_controller import (
    add_post_category_handler,
    delete_post_category_handler,
    edit_post_category_handler,
)
from placeNoteApi2024.controller.post.post_place_controller import (
    add_post_place_handler,
    delete_post_place_handler,
    edit_post_place_handler,
)
from placeNoteApi2024.graphql.strawberry_object import (
    AccountUserResponse,
    GoogleAuthCodeVerifyResponse,
    LatLon,
)
from placeNoteApi2024.service.account_user_service import (
    get_user_account_id_from_context_dict,
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

    @strawberry.mutation
    def add_post_category(
        self,
        info: strawberry.Info,
        name: str,
        parent_category_id: str | None,
        display_order: int | None,
        memo: str | None,
    ) -> bool:
        user_account_id = get_user_account_id_from_context_dict(info.context)
        result = add_post_category_handler(
            user_account_id, name, parent_category_id, display_order, memo
        )
        if is_successful(result):
            return result.unwrap()
        else:
            return result.failure()

    @strawberry.mutation
    def edit_post_category(
        self,
        info: strawberry.Info,
        id: str,
        name: str,
        parent_category_id: str | None,
        display_order: int | None,
        memo: str | None,
    ) -> bool:
        user_account_id = get_user_account_id_from_context_dict(info.context)
        result = edit_post_category_handler(
            id, user_account_id, name, parent_category_id, display_order, memo
        )
        if is_successful(result):
            return result.unwrap()
        else:
            return result.failure()

    @strawberry.mutation
    def delete_post_category(
        self,
        info: strawberry.Info,
        id: str,
    ) -> bool:
        user_account_id = get_user_account_id_from_context_dict(info.context)
        result = delete_post_category_handler(id, user_account_id)
        if is_successful(result):
            return result.unwrap()
        else:
            return result.failure()

    @strawberry.mutation
    def add_post_place(
        self,
        info: strawberry.Info,
        name: str,
        address: str | None,
        lat_lon: LatLon | None,
        prefecture_code: str | None,
        category_id_list: List[str],
        detail: str | None,
        url_list: List[str],
    ) -> bool:
        user_account_id = get_user_account_id_from_context_dict(info.context)
        result = add_post_place_handler(
            user_account_id,
            name,
            address,
            lat_lon,
            prefecture_code,
            category_id_list,
            detail,
            url_list,
        )
        if is_successful(result):
            return result.unwrap()
        else:
            return result.failure()

    @strawberry.mutation
    def edit_post_place(
        self,
        info: strawberry.Info,
        id: str,
        name: str,
        address: str | None,
        lat_lon: LatLon | None,
        prefecture_code: str | None,
        category_id_list: List[str],
        detail: str | None,
        url_list: List[str],
    ) -> bool:
        user_account_id = get_user_account_id_from_context_dict(info.context)
        result = edit_post_place_handler(
            id,
            user_account_id,
            name,
            address,
            lat_lon,
            prefecture_code,
            category_id_list,
            detail,
            url_list,
        )
        if is_successful(result):
            return result.unwrap()
        else:
            return result.failure()

    @strawberry.mutation
    def delete_post_place(
        self,
        info: strawberry.Info,
        id: str,
    ) -> bool:
        user_account_id = get_user_account_id_from_context_dict(info.context)
        result = delete_post_place_handler(id, user_account_id)
        if is_successful(result):
            return result.unwrap()
        else:
            return result.failure()
