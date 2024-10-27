from typing import List
from mongoengine import *
from graphql import GraphQLError
from returns.result import Result, Failure

from placeNoteApi2024.graphql.strawberry_object import (
    LatLon,
    LatLonResponse,
    PostPlaceResponse,
)
from placeNoteApi2024.service.post_service.post_place_service import (
    add_post_place_service,
    delete_post_place_service,
    edit_post_place_service,
    get_lat_lon_from_address_service,
    get_post_places_service,
)
from placeNoteApi2024.service_model.post_place_service_model import (
    PostPlaceServiceModel,
)


def add_post_place_handler(
    user_account_id: str,
    name: str,
    address: str | None,
    lat_lon: LatLon | None,
    prefecture_code: str | None,
    category_id_list: List[str],
    detail: str | None,
    url: str | None,
) -> Result[bool, GraphQLError]:
    try:
        add_place = PostPlaceServiceModel(
            user_account_id=user_account_id,
            name=name,
            address=address,
            lat_lon=lat_lon,
            prefecture_code=prefecture_code,
            category_id_list=category_id_list,
            detail=detail,
            url=url,
        )
        return add_post_place_service(add_place)
    except Exception as e:
        return Failure(GraphQLError(message=str(e), extensions={"code": 500}))


def edit_post_place_handler(
    id: str,
    user_account_id: str,
    name: str,
    address: str | None,
    lat_lon: LatLon | None,
    prefecture_code: str | None,
    category_id_list: List[str],
    detail: str | None,
    url: str | None,
) -> Result[bool, GraphQLError]:
    try:
        edit_place = PostPlaceServiceModel(
            id=id,
            user_account_id=user_account_id,
            name=name,
            address=address,
            lat_lon=lat_lon,
            prefecture_code=prefecture_code,
            category_id_list=category_id_list,
            detail=detail,
            url=url,
        )
        return edit_post_place_service(edit_place)
    except Exception as e:
        return Failure(GraphQLError(message=str(e), extensions={"code": 500}))


def delete_post_place_handler(
    id: str,
    user_account_id: str,
) -> Result[bool, GraphQLError]:
    try:
        return delete_post_place_service(id, user_account_id)
    except Exception as e:
        return Failure(GraphQLError(message=str(e), extensions={"code": 500}))


def get_post_places_handler(
    user_account_id: str,
    id_filter: str | None,
    category_filter: str | None,
    name_filter: str | None,
) -> Result[List[PostPlaceResponse], GraphQLError]:
    try:
        return get_post_places_service(
            user_account_id, id_filter, category_filter, name_filter
        )
    except Exception as e:
        return Failure(GraphQLError(message=str(e), extensions={"code": 500}))


def get_lat_lon_from_address(
    address: str,
) -> Result[LatLonResponse | None, GraphQLError]:
    try:
        return get_lat_lon_from_address_service(address)
    except Exception as e:
        return Failure(GraphQLError(message=str(e), extensions={"code": 500}))
