import strawberry


@strawberry.type
class GoogleAuthCodeVerifyResponse:
    token: str


@strawberry.type
class AccountUserResponse:
    token: str
    user_setting_id: str
    name: str


@strawberry.type
class PostCategoryResponse:
    id: str
    user_setting_id: str
    name: str
    parent_category_id: str | None
    display_order: int | None
    memo: str | None
