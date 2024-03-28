import strawberry

from placeNoteApi2024.graphql.strawberry_object import GetAccountUserByTokenResponse


@strawberry.type
class PlaceNoteQuery:
    @strawberry.field
    def get_account_user_by_token(self, token: str) -> GetAccountUserByTokenResponse:
        return GetAccountUserByTokenResponse(name=token, user_setting_id="aaaa")
