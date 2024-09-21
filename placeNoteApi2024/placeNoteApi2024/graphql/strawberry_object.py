from typing import List
import strawberry


@strawberry.type
class GoogleAuthCodeVerifyResponse:
    token: str


@strawberry.type
class AccountUserResponse:
    token: str
    user_setting_id: str
    name: str
    image_url: str | None


@strawberry.type
class PostCategoryResponse:
    id: str
    user_setting_id: str
    name: str
    parent_category_id: str | None
    display_order: int | None
    memo: str | None


@strawberry.input
class LatLon:
    lat: float
    lon: float


@strawberry.type
class LatLonResponse:
    lat: float
    lon: float


@strawberry.type
class PostPlaceResponse:
    id: str
    user_setting_id: str
    name: str
    category_id_list: List[str]
    url_list: List[str]
    address: str | None = None
    lat_lon: LatLonResponse | None = None
    prefecture_code: str | None = None
    detail: str | None = None
