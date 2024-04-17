import strawberry


@strawberry.type
class GoogleAuthCodeVerifyResponse:
    token: str


@strawberry.type
class AccountUserResponse:
    token: str
    user_setting_id: str
    name: str
