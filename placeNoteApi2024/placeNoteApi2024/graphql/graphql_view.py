from typing import Any
from django.http import HttpRequest, HttpResponse
from strawberry.django.views import GraphQLView

from placeNoteApi2024.service.jwt_service import decode_jwt

USER_ACCOUNT_ID_CONTEXT_PROPERTY = "user_account_id"


class PlaceNoteGraphQLView(GraphQLView):
    def get_context(self, request: HttpRequest, response: HttpResponse) -> Any:
        bearer_token: str = request.headers.get("Authorization", None)
        # 認証されてない場合はダミーのdictを返す
        if bearer_token == None or len(bearer_token.split(" ")) < 2:
            return {"dummy": "dummy"}

        decode_result = decode_jwt(bearer_token.split(" ")[1])
        if decode_result == None:
            return {"dummy": "dummy"}
        else:
            return {
                USER_ACCOUNT_ID_CONTEXT_PROPERTY: decode_result[
                    USER_ACCOUNT_ID_CONTEXT_PROPERTY
                ]
            }
