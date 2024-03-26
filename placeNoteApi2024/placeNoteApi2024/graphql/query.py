import graphene

from placeNoteApi2024.graphql.graphene_object import GetAccountUserByTokenResponse


class PlaceNoteQuery(graphene.ObjectType):
    get_account_user_by_token = graphene.Field(
        GetAccountUserByTokenResponse, token=graphene.String(required=True)
    )

    def resolve_get_account_user_by_token(parent, info, token):
        return GetAccountUserByTokenResponse(name=token, user_setting_id="aaaa")
