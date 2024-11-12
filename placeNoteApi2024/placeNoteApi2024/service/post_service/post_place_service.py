from typing import List
from graphql import GraphQLError
import requests
from returns.result import Result, Success, Failure
import urllib.parse
import xmltodict

from placeNoteApi2024.graphql.strawberry_object import (
    LatLonResponse,
    PostPlaceResponse,
)
from placeNoteApi2024.repository.post_place_repository import (
    add_post_place,
    delete_place_by_id,
    edit_post_place,
    find_post_places,
)
from placeNoteApi2024.service_model.post_place_service_model import (
    PostPlaceServiceModel,
)


def add_post_place_service(
    service_model: PostPlaceServiceModel,
) -> Result[str, GraphQLError]:
    post_place = add_post_place(service_model)
    return Success(post_place._id)


def edit_post_place_service(
    service_model: PostPlaceServiceModel,
) -> Result[bool, GraphQLError]:
    result = edit_post_place(service_model)
    if result == False:
        return Failure(
            GraphQLError(message="Can not find update place", extensions={"code": 404})
        )
    return Success(True)


def delete_post_place_service(
    id: str,
    user_account_id: str,
) -> Result[bool, GraphQLError]:
    delete_place_by_id(id, user_account_id)
    return Success(True)


def get_post_places_service(
    user_account_id: str,
    id_filter: str | None,
    category_filter: str | None,
    name_filter: str | None,
) -> Result[List[PostPlaceResponse], GraphQLError]:
    return Success(
        list(
            map(
                lambda p: PostPlaceResponse(
                    id=p._id,
                    user_setting_id=p.user_setting_id,
                    name=p.name,
                    category_id_list=p.category_id_list,
                    address=p.address,
                    url=p.url,
                    lat_lon=p.get_lat_lon_object(),
                    prefecture_code=p.prefecture_code,
                    detail=p.detail,
                ),
                find_post_places(
                    user_account_id, id_filter, category_filter, name_filter
                ),
            )
        )
    )


def get_lat_lon_from_address_service(
    address: str,
) -> Result[LatLonResponse | None, GraphQLError]:
    try:
        safe_address = urllib.parse.quote_plus(address)
        res = requests.get("https://www.geocoding.jp/api/?q=" + safe_address)
        if res.status_code != 200:
            return Success(None)
        parsed = xmltodict.parse(res.text)
        coordinate = parsed["result"]["coordinate"]

        return Success(
            LatLonResponse(lat=float(coordinate["lat"]), lon=float(coordinate["lng"]))
        )
    except Exception as e:
        return Success(None)
