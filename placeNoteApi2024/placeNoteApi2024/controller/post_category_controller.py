from typing import List
from mongoengine import *
from graphql import GraphQLError
from returns.result import Result, Failure, Success

from placeNoteApi2024.graphql.strawberry_object import PostCategoryResponse
from placeNoteApi2024.service.post_service.post_category_service import (
    add_post_category_service,
    delete_post_category_service,
    edit_post_category_service,
    get_my_post_categories_service,
)
from placeNoteApi2024.service_model.post_category_service_model import (
    PostCategoryServiceModel,
)


def add_post_category_handler(
    user_account_id: str,
    name: str,
    parent_category_id: str | None,
    display_order: int | None,
    detail: str | None,
) -> Result[bool, GraphQLError]:
    try:
        add_category = PostCategoryServiceModel(
            user_account_id=user_account_id,
            name=name,
            parent_category_id=parent_category_id,
            display_order=display_order,
            detail=detail,
        )
        return add_post_category_service(add_category)
    except Exception as e:
        return Failure(GraphQLError(message=str(e), extensions={"code": 500}))


def edit_post_category_handler(
    id: str,
    user_account_id: str,
    name: str,
    parent_category_id: str | None,
    display_order: int | None,
    detail: str | None,
) -> Result[bool, GraphQLError]:
    try:
        edit_category = PostCategoryServiceModel(
            id=id,
            user_account_id=user_account_id,
            name=name,
            parent_category_id=parent_category_id,
            display_order=display_order,
            detail=detail,
        )
        return edit_post_category_service(edit_category)
    except Exception as e:
        return Failure(GraphQLError(message=str(e), extensions={"code": 500}))


def delete_post_category_handler(
    id: str,
    user_account_id: str,
) -> Result[bool, GraphQLError]:
    try:
        return delete_post_category_service(id, user_account_id)
    except Exception as e:
        return Failure(GraphQLError(message=str(e), extensions={"code": 500}))


def get_post_categories_handler(
    user_account_id: str, name_filter: str | None
) -> Result[List[PostCategoryResponse], GraphQLError]:
    try:
        return get_my_post_categories_service(user_account_id, None, name_filter)
    except Exception as e:
        return Failure(GraphQLError(message=str(e), extensions={"code": 500}))


def get_post_category_by_id_handler(
    user_account_id: str, id_filter: str
) -> Result[PostCategoryResponse, GraphQLError]:
    try:
        results = get_my_post_categories_service(
            user_account_id, id_filter, None
        ).unwrap()

        if len(results) > 0:
            return Success(results[0])
        else:
            return Failure(GraphQLError(message=str(e), extensions={"code": 404}))
    except Exception as e:
        return Failure(GraphQLError(message=str(e), extensions={"code": 500}))
