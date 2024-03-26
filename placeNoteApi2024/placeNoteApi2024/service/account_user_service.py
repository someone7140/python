from mongoengine import *
from graphql import GraphQLError
from returns.result import Result, Failure, Success

from placeNoteApi2024.graphql.graphene_object import AddAccountUserResponse
from placeNoteApi2024.repository.account_user_repository import (
    add_user_account,
    get_user_accounts_by_query,
)


def add_account_user_by_google_service(
    user_setting_id: str,
    name: str,
    gmail: str,
) -> Result[AddAccountUserResponse, GraphQLError]:
    # すでに登録済みの値の場合はエラー
    result_list = get_user_accounts_by_query(
        Q(user_setting_id=user_setting_id) | Q(gmail=gmail)
    )
    if len(result_list) > 0:
        return Failure(
            GraphQLError(message="Duplicate input error", extensions={"code": 400})
        )

    account_user = add_user_account(user_setting_id, name, gmail)
    return Success(AddAccountUserResponse(token=account_user.id))
