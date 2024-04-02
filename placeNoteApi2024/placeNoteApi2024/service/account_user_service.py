from mongoengine import *
from graphql import GraphQLError
from returns.result import Result, Failure, Success

from placeNoteApi2024.graphql.strawberry_object import AddAccountUserResponse
from placeNoteApi2024.repository.account_user_repository import (
    add_user_account,
    get_user_accounts_by_query,
)
from placeNoteApi2024.service.jwt_service import decode_jwt, encode_jwt


def google_auth_code_verify_service(
    auth_code: str,
) -> Result[AddAccountUserResponse, GraphQLError]:
    gmail = "sample@gmail.com"
    # すでに登録済みの値の場合はエラー
    result_list = get_user_accounts_by_query(Q(gmail=gmail))
    if len(result_list) > 0:
        return Failure(
            GraphQLError(message="Duplicate input error", extensions={"code": 400})
        )

    auth_token = encode_jwt({"gmail": gmail}, 14400)
    return Success(AddAccountUserResponse(token=auth_token))


def add_account_user_by_google_service(
    auth_token: str,
    user_setting_id: str,
    name: str,
) -> Result[AddAccountUserResponse, GraphQLError]:
    decode_result = decode_jwt(auth_token)
    if decode_result == None:
        return Failure(
            GraphQLError(message="Failed decode token", extensions={"code": 401})
        )
    gmail = decode_result["gmail"]

    # すでに登録済みの値の場合はエラー
    result_list = get_user_accounts_by_query(
        Q(user_setting_id=user_setting_id) | Q(gmail=gmail)
    )
    if len(result_list) > 0:
        return Failure(
            GraphQLError(message="Duplicate input error", extensions={"code": 400})
        )

    account_user = add_user_account(user_setting_id, name, gmail)
    return Success(AddAccountUserResponse(token=account_user._id))
