import os
from typing import Dict
import uuid
from mongoengine import *
from graphql import GraphQLError
from returns.result import Result, Failure, Success
from strawberry.file_uploads import Upload

from django.core.files.uploadedfile import UploadedFile

from placeNoteApi2024.graphql.graphql_view import USER_ACCOUNT_ID_CONTEXT_PROPERTY
from placeNoteApi2024.graphql.strawberry_object import (
    AccountUserResponse,
    GoogleAuthCodeVerifyResponse,
)
from placeNoteApi2024.repository.account_user_repository import (
    add_user_account,
    get_user_accounts_by_query,
)
from placeNoteApi2024.service.external_service.google_api_service import (
    get_gmail_from_auth_code,
    upload_file_gcs,
)
from placeNoteApi2024.service.jwt_service import decode_jwt, encode_jwt


def google_auth_code_verify_service(
    auth_code: str,
) -> Result[GoogleAuthCodeVerifyResponse, GraphQLError]:
    # auth_codeからgmailを取得
    gmail = get_gmail_from_auth_code(auth_code)
    if gmail == None:
        return Failure(
            GraphQLError(message="Failed auth google code", extensions={"code": 401})
        )

    # すでに登録済みの値の場合はエラー
    result_list = get_user_accounts_by_query(Q(gmail=gmail))
    if len(result_list) > 0:
        return Failure(
            GraphQLError(message="Duplicate input error", extensions={"code": 400})
        )

    auth_token = encode_jwt({"gmail": gmail}, 14400)
    return Success(GoogleAuthCodeVerifyResponse(token=auth_token))


def add_account_user_by_google_service(
    auth_token: str,
    user_setting_id: str,
    name: str,
    image_file: Upload | None,
) -> Result[AccountUserResponse, GraphQLError]:
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

    # image_fileがある場合はアップロード
    image_url = None
    if image_file != None:
        image_url = upload_icon_image_file(image_file)

    account_user = add_user_account(user_setting_id, name, gmail, image_url)
    token = encode_jwt({USER_ACCOUNT_ID_CONTEXT_PROPERTY: account_user._id}, 15552000)
    return Success(
        AccountUserResponse(
            token=token,
            user_setting_id=account_user.user_setting_id,
            name=account_user.name,
            image_url=image_url,
        )
    )


def login_by_google_auth_code_service(
    auth_code: str,
) -> Result[AccountUserResponse, GraphQLError]:
    # auth_codeからgmailを取得
    gmail = get_gmail_from_auth_code(auth_code)
    if gmail == None:
        return Failure(
            GraphQLError(message="Failed auth google code", extensions={"code": 401})
        )

    result_list = get_user_accounts_by_query(Q(gmail=gmail))
    # 0件の場合はエラー
    if len(result_list) < 1:
        return Failure(GraphQLError(message="Not found user", extensions={"code": 404}))

    user = result_list[0]
    token = encode_jwt({USER_ACCOUNT_ID_CONTEXT_PROPERTY: user._id}, 15552000)
    return Success(
        AccountUserResponse(
            token=token,
            user_setting_id=user.user_setting_id,
            name=user.name,
            image_url=user.image_url,
        )
    )


def get_user_account_id_from_context_dict(
    context_dict: Dict[str, str],
) -> str:
    result_opt = context_dict.get(USER_ACCOUNT_ID_CONTEXT_PROPERTY, None)
    if result_opt == None:
        raise GraphQLError(message="Failed authentication", extensions={"code": 401})
    return result_opt


def get_user_account_by_id(
    user_account_id: str,
) -> Result[AccountUserResponse, GraphQLError]:
    result_list = get_user_accounts_by_query(Q(_id=user_account_id))
    if len(result_list) < 1:
        return Failure(
            GraphQLError(message="Can not find user", extensions={"code": 401})
        )

    user = result_list[0]
    token = encode_jwt({USER_ACCOUNT_ID_CONTEXT_PROPERTY: user._id}, 15552000)
    return Success(
        AccountUserResponse(
            token=token,
            user_setting_id=user.user_setting_id,
            name=user.name,
            image_url=user.image_url,
        )
    )


def upload_icon_image_file(image_file: Upload) -> str:
    file_uploaded: UploadedFile = image_file

    # 拡張子を取得
    ext = os.path.splitext(file_uploaded.name)[1]
    # 新しくファイル名を割り振る
    new_file_name = str(uuid.uuid4())
    file_path = f"user_icon_image/{new_file_name}{ext}"

    return upload_file_gcs(file_path, file_uploaded.file)
