from mongoengine import *
from graphql import GraphQLError
from returns.result import Result, Failure
from strawberry.file_uploads import Upload

from placeNoteApi2024.service.account_user_service import (
    add_account_user_by_google_service,
    edit_account_user,
    get_user_account_by_id,
    google_auth_code_verify_service,
    login_by_google_auth_code_service,
)
from placeNoteApi2024.graphql.strawberry_object import (
    AccountUserResponse,
    GoogleAuthCodeVerifyResponse,
)


def google_auth_code_verify_handler(
    auth_code: str,
) -> Result[GoogleAuthCodeVerifyResponse, GraphQLError]:
    try:
        return google_auth_code_verify_service(auth_code)
    except Exception as e:
        return Failure(GraphQLError(message=str(e), extensions={"code": 500}))


def add_account_user_by_google_handler(
    auth_token: str,
    user_setting_id: str,
    name: str,
    image_file: Upload | None,
) -> Result[AccountUserResponse, GraphQLError]:
    try:
        return add_account_user_by_google_service(
            auth_token, user_setting_id, name, image_file
        )
    except Exception as e:
        return Failure(GraphQLError(message=str(e), extensions={"code": 500}))


def edit_account_user_handler(
    user_account_id: str,
    user_setting_id: str,
    name: str,
    image_file: Upload | None,
) -> Result[AccountUserResponse, GraphQLError]:
    try:
        return edit_account_user(user_account_id, user_setting_id, name, image_file)
    except Exception as e:
        return Failure(GraphQLError(message=str(e), extensions={"code": 500}))


def login_by_google_auth_code_handler(
    auth_code: str,
) -> Result[AccountUserResponse, GraphQLError]:
    try:
        return login_by_google_auth_code_service(auth_code)
    except Exception as e:
        return Failure(GraphQLError(message=str(e), extensions={"code": 500}))


def get_account_user_by_id_handler(
    user_account_id: str,
) -> Result[AccountUserResponse, GraphQLError]:
    try:
        return get_user_account_by_id(user_account_id)
    except Exception as e:
        return Failure(GraphQLError(message=str(e), extensions={"code": 500}))
