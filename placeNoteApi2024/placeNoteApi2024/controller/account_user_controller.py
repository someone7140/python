from mongoengine import *
from graphql import GraphQLError
from returns.result import Result, Failure

from placeNoteApi2024.service.account_user_service import (
    add_account_user_by_google_service,
    google_auth_code_verify_service,
)
from placeNoteApi2024.graphql.strawberry_object import (
    AddAccountUserResponse,
    GoogleAuthCodeVerifyResponse,
)


def google_auth_code_verify(
    auth_code: str,
) -> Result[GoogleAuthCodeVerifyResponse, GraphQLError]:
    try:
        return google_auth_code_verify_service(auth_code)
    except Exception as e:
        return Failure(GraphQLError(message=str(e), extensions={"code": 500}))


def add_account_user_by_google(
    auth_token: str,
    user_setting_id: str,
    name: str,
) -> Result[AddAccountUserResponse, GraphQLError]:
    try:
        return add_account_user_by_google_service(auth_token, user_setting_id, name)
    except Exception as e:
        return Failure(GraphQLError(message=str(e), extensions={"code": 500}))
