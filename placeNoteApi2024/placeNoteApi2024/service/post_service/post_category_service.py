from typing import List
from graphql import GraphQLError
from returns.result import Result, Failure, Success

from placeNoteApi2024.graphql.strawberry_object import PostCategoryResponse
from placeNoteApi2024.repository.post.post_category_repository import (
    add_post_category,
    delete_category_by_id,
    edit_post_category,
    find_post_categories,
)
from placeNoteApi2024.service_model.post_service_model import PostCategoryServiceModel


def add_post_category_service(
    service_model: PostCategoryServiceModel,
) -> Result[bool, GraphQLError]:
    add_post_category(service_model)
    return Success(True)


def edit_post_category_service(
    service_model: PostCategoryServiceModel,
) -> Result[bool, GraphQLError]:
    result = edit_post_category(service_model)
    if result == False:
        return Failure(
            GraphQLError(
                message="Can not find update category", extensions={"code": 404}
            )
        )
    return Success(True)


def delete_post_category_service(
    id: str,
    user_account_id: str,
) -> Result[bool, GraphQLError]:
    delete_category_by_id(id, user_account_id)
    return Success(True)


def get_my_post_categories_service(
    user_account_id: str, name_filter: str | None
) -> Result[List[PostCategoryResponse], GraphQLError]:
    return Success(
        list(
            map(
                lambda c: PostCategoryResponse(
                    id=c._id,
                    user_account_id=c.create_user_account_id,
                    name=c.name,
                    parent_category_id=c.parent_category_id,
                    display_order=c.display_order,
                    memo=c.memo,
                ),
                find_post_categories(user_account_id, name_filter),
            )
        )
    )
