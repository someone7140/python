import datetime
from typing import List
from mongoengine import *
from graphql import GraphQLError
from returns.result import Result, Failure

from placeNoteApi2024.service.post_service.post_service import add_post_service
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
