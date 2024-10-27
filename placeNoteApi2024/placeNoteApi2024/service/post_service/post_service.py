import datetime
from typing import List
from graphql import GraphQLError
from returns.result import Result, Success

from placeNoteApi2024.repository.post_place_repository import (
    add_post_place,
)
from placeNoteApi2024.repository.post_repository import add_post
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
