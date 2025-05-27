import datetime
from typing import List
from mongoengine import *
from graphql import GraphQLError
from returns.result import Result, Failure

from placeNoteApi2024.graphql.strawberry_object import LatLon, PostResponse
from placeNoteApi2024.service.post_service.post_service import (
    add_post_service,
    delete_post_service,
    edit_post_service,
    get_my_posts_by_lat_lon_service,
    get_posts_service,
)
from placeNoteApi2024.service_model.post_service_model import UrlServiceModel


def add_post_handler(
    user_account_id: str,
    title: str,
    place_id: str,
    visited_date: datetime.datetime,
    is_open: bool,
    category_id_list: List[str],
    detail: str | None,
    url_list: List[str],
) -> Result[bool, GraphQLError]:
    try:
        url_service_model_list = list(
            map(
                lambda u: UrlServiceModel.make_object_from_url(u),
                url_list,
            )
        )
        return add_post_service(
            user_account_id,
            title,
            place_id,
            visited_date,
            is_open,
            category_id_list,
            detail,
            url_service_model_list,
        )
    except Exception as e:
        return Failure(GraphQLError(message=str(e), extensions={"code": 500}))


def edit_post_handler(
    user_account_id: str,
    id: str,
    title: str,
    place_id: str,
    visited_date: datetime.datetime,
    is_open: bool,
    category_id_list: List[str],
    detail: str | None,
    url_list: List[str],
) -> Result[bool, GraphQLError]:
    try:
        url_service_model_list = list(
            map(
                lambda u: UrlServiceModel.make_object_from_url(u),
                url_list,
            )
        )
        return edit_post_service(
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
    except Exception as e:
        return Failure(GraphQLError(message=str(e), extensions={"code": 500}))


def delete_post_handler(
    id: str,
    user_account_id: str,
) -> Result[bool, GraphQLError]:
    try:
        return delete_post_service(id, user_account_id)
    except Exception as e:
        return Failure(GraphQLError(message=str(e), extensions={"code": 500}))


def get_my_posts_handler(
    user_account_id: str,
    id_filter: str | None,
    category_ids_filter: List[str] | None,
    place_id_filter: str | None,
    is_order_post_date: bool,
) -> Result[List[PostResponse], GraphQLError]:
    try:
        return get_posts_service(
            user_account_id,
            id_filter,
            category_ids_filter,
            place_id_filter,
            None,
            False,
            is_order_post_date,
            200,
        )
    except Exception as e:
        return Failure(GraphQLError(message=str(e), extensions={"code": 500}))


def get_open_posts_handler(
    user_setting_id: str | None,
) -> Result[List[PostResponse], GraphQLError]:
    try:
        return get_posts_service(
            None, None, None, None, user_setting_id, True, True, 50
        )
    except Exception as e:
        return Failure(GraphQLError(message=str(e), extensions={"code": 500}))


def get_my_posts_by_lat_lon_handler(
    user_account_id: str,
    lat_lon: LatLon,
    radius_kilo_meter: float,
    is_order_post_date: bool,
) -> Result[List[PostResponse], GraphQLError]:
    try:
        return get_my_posts_by_lat_lon_service(
            user_account_id,
            lat_lon,
            radius_kilo_meter,
            is_order_post_date,
            200,
        )
    except Exception as e:
        return Failure(GraphQLError(message=str(e), extensions={"code": 500}))
