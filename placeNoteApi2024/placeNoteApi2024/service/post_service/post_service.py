import datetime
from typing import List
from graphql import GraphQLError
from returns.result import Result, Success

from placeNoteApi2024.graphql.strawberry_object import (
    LatLon,
    PostPlaceInfo,
    PostResponse,
)
from placeNoteApi2024.repository.post_repository import (
    add_post,
    delete_post_by_id,
    edit_post,
    find_my_posts_by_lat_lon,
    find_posts,
)
from placeNoteApi2024.service_model.post_service_model import (
    PostQueryServiceModel,
    UrlServiceModel,
)


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


def get_posts_service(
    user_account_id: str | None,
    id_filter: str | None,
    category_ids_filter: List[str] | None,
    place_id_filter: str | None,
    user_setting_id: str | None,
    is_open_only: bool,
    is_order_post_date: bool,
    limit: int,
) -> Result[List[PostResponse], GraphQLError]:
    post_results = find_posts(
        user_account_id,
        id_filter,
        category_ids_filter,
        place_id_filter,
        user_setting_id,
        is_open_only,
        is_order_post_date,
        limit,
    )
    return Success(get_response_posts_from_db_query_model(post_results))


def get_my_posts_by_lat_lon_service(
    user_account_id: str,
    lat_lon: LatLon,
    radius_kilo_meter: float,
    is_order_post_date: bool,
    limit: int,
) -> Result[List[PostResponse], GraphQLError]:
    post_results = find_my_posts_by_lat_lon(
        user_account_id,
        lat_lon,
        radius_kilo_meter * 1000,
        is_order_post_date,
        limit,
    )
    return Success(get_response_posts_from_db_query_model(post_results))


# DBから取得したPostのモデルをレスポンスに変換して取得
def get_response_posts_from_db_query_model(
    post_list_db_query_model: List[PostQueryServiceModel],
) -> List[PostQueryServiceModel]:
    return list(
        map(
            lambda p: PostResponse(
                id=p._id,
                user_setting_id=p.user_setting_id,
                user_name=p.user_name,
                user_image_url=p.user_image_url,
                title=p.title,
                visited_date_str=p.visited_date.isoformat() + "Z",
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
            post_list_db_query_model,
        )
    )
