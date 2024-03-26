import graphene


class GetAccountUserByTokenResponse(graphene.ObjectType):
    name = graphene.String()
    user_setting_id = graphene.String()


class AddAccountUserResponse(graphene.ObjectType):
    token = graphene.String()
