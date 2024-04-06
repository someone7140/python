import strawberry


@strawberry.type
class GetAccountUserByTokenResponse:
    name: str
    user_setting_id: str


@strawberry.type
class GoogleAuthCodeVerifyResponse:
    token: str


@strawberry.type
class AddAccountUserResponse:
    token: str
    user_setting_id: str
    name: str
