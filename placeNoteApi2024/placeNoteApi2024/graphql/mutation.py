import graphene
from returns.pipeline import is_successful

from placeNoteApi2024.controller.account_user_controller import (
    add_account_user_by_google,
)
from placeNoteApi2024.graphql.graphene_object import AddAccountUserResponse


class AddAccountUserByGoogleMutation(graphene.Mutation):
    class Arguments:
        user_setting_id = graphene.String(required=True)
        name = graphene.String(required=True)
        gmail = graphene.String(required=True)

    # The class attributes define the response of the mutation
    response = graphene.Field(AddAccountUserResponse)

    @classmethod
    def mutate(cls, root, info, user_setting_id, name, gmail):
        result = add_account_user_by_google(user_setting_id, name, gmail)

        if is_successful(result):
            return AddAccountUserByGoogleMutation(response=result.unwrap())
        else:
            return result.failure()


class PlaceNoteMutation(graphene.ObjectType):
    add_account_user_by_google = AddAccountUserByGoogleMutation.Field()
