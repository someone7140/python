import datetime
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
    detail: str | None


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
    url: str | None = None
    address: str | None = None
    lat_lon: LatLonResponse | None = None
    prefecture_code: str | None = None
    detail: str | None = None


@strawberry.type
class PostUrlInfo:
    title: str
    image_url: str | None
    site_name: str | None


@strawberry.type
class PostUrl:
    url: str
    url_type: str
    url_info: PostUrlInfo | None
    embed_html: str | None


@strawberry.type
class PostPlaceInfo:
    id: str
    name: str
    prefecture_code: str | None = None
    url: str | None = None
    address: str | None = None
    lat_lon: LatLonResponse | None = None


@strawberry.type
class PostResponse:
    id: str
    user_setting_id: str
    title: str
    visited_date: datetime.datetime
    is_open: bool
    post_place: PostPlaceInfo
    category_id_list: List[str]
    url_list: List[PostUrl]
    detail: str | None = None
