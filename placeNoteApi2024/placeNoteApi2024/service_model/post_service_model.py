from dataclasses import dataclass
from typing import List

from placeNoteApi2024.graphql.strawberry_object import LatLon, LatLonResponse


@dataclass
class PostCategoryServiceModel:
    user_account_id: str
    name: str
    id: str | None = None
    parent_category_id: str | None = None
    display_order: int | None = None
    memo: str | None = None


@dataclass
class PostCategoryQueryServiceModel:
    _id: str
    user_setting_id: str
    name: str
    parent_category_id: str | None = None
    display_order: int | None = None
    memo: str | None = None


@dataclass
class PostPlaceServiceModel:
    user_account_id: str
    name: str
    category_id_list: List[str]
    url_list: List[str]
    id: str | None = None
    address: str | None = None
    lat_lon: LatLon | None = None
    prefecture_code: str | None = None
    detail: str | None = None

    def get_lon_lat_array(self):
        return [self.lat_lon.lon, self.lat_lon.lat] if self.lat_lon != None else None


@dataclass
class PostPlaceQueryServiceModel:
    _id: str
    user_setting_id: str
    name: str
    category_id_list: List[str]
    url_list: List[str]
    id: str | None = None
    address: str | None = None
    lon_lat: List[float] | None = None
    prefecture_code: str | None = None
    detail: str | None = None

    def get_lat_lon_object(self):
        return (
            LatLonResponse(lat=self.lon_lat[1], lon=self.lon_lat[0])
            if self.lon_lat != None
            else None
        )
