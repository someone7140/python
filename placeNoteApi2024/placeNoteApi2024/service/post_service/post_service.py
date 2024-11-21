import datetime
from typing import List
from graphql import GraphQLError
from returns.result import Result, Success

from placeNoteApi2024.graphql.strawberry_object import (
    PostPlaceInfo,
    PostResponse,
    PostUrl,
    PostUrlInfo,
)
from placeNoteApi2024.repository.post_place_repository import (
    add_post_place,
)
from placeNoteApi2024.repository.post_repository import (
    add_post,
    delete_post_by_id,
    edit_post,
    find_posts,
)
from placeNoteApi2024.service_model.post_service_model import UrlServiceModel


def add_post_service(
    user_account_id: str,
    title: str,
    place_id: str,
    visited_date: datetime.datetime,
    is_open: bool,
    category_id_list: List[str],
    detail: str | None,
    url_service_model_list: List[UrlServiceModel],
) -> Result[bool, GraphQLError]:
    add_post(
        user_account_id,
        title,
        place_id,
        visited_date,
        is_open,
        category_id_list,
        detail,
        url_service_model_list,
    )
    return Success(True)


def edit_post_service(
    user_account_id: str,
    id: str,
    title: str,
    place_id: str,
    visited_date: datetime.datetime,
    is_open: bool,
    category_id_list: List[str],
    detail: str | None,
    url_service_model_list: List[UrlServiceModel],
) -> Result[bool, GraphQLError]:
    edit_post(
        user_account_id,
        id,
        title,
        place_id,
        visited_date,
        is_open,
        category_id_list,
        detail,
        url_service_model_list,
    )
    return Success(True)


def delete_post_service(
    id: str,
    user_account_id: str,
) -> Result[bool, GraphQLError]:
    delete_post_by_id(
        id,
        user_account_id,
    )
    return Success(True)


def get_my_posts_service(
    user_account_id: str,
    id_filter: str | None,
    category_ids_filter: List[str] | None,
    place_id_filter: str | None,
) -> Result[List[PostResponse], GraphQLError]:
    return Success(
        list(
            map(
                lambda p: PostResponse(
                    id=p._id,
                    user_setting_id=p.user_setting_id,
                    title=p.title,
                    visited_date=p.visited_date,
                    is_open=p.is_open,
                    category_id_list=p.category_id_list,
                    detail=p.detail,
                    post_place=PostPlaceInfo(
                        id=p.place._id,
                        name=p.place.name,
                        prefecture_code=p.place.prefecture_code,
                        url=p.place.url,
                        address=p.place.address,
                        lat_lon=p.place.get_lat_lon_object(),
                    ),
                    url_list=p.url_list,
                ),
                find_posts(
                    user_account_id,
                    id_filter,
                    category_ids_filter,
                    place_id_filter,
                    False,
                    False,
                    200,
                ),
            )
        )
    )
