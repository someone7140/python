from mongoengine import *
from graphql import GraphQLError
from returns.result import Result, Failure

from placeNoteApi2024.service.account_user_service import (
    add_account_user_by_google_service,
)
from placeNoteApi2024.graphql.graphene_object import AddAccountUserResponse


def add_account_user_by_google(
    user_setting_id: str,
    name: str,
    gmail: str,
) -> Result[AddAccountUserResponse, GraphQLError]:
    try:
        return add_account_user_by_google_service(user_setting_id, name, gmail)
    except Exception as e:
        return Failure(GraphQLError(message=str(e), extensions={"code": 500}))
