import strawberry


@strawberry.type
class GetAccountUserByTokenResponse:
    name: str
    user_setting_id: str


@strawberry.type
class AddAccountUserResponse:
    token: str
