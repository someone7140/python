from typing import List
import uuid

from mongoengine import *

from placeNoteApi2024.graphql.strawberry_object import PostCategoryResponse
from placeNoteApi2024.models import PostPlace
from placeNoteApi2024.repository.post_category_repository import (
    find_post_categories_with_children,
)
from placeNoteApi2024.service_model.post_service_model import (
    PostPlaceQueryServiceModel,
    PostPlaceServiceModel,
)


def add_post_place(add_place: PostPlaceServiceModel) -> PostPlace:
    post_place = PostPlace(
        _id=str(uuid.uuid4()),
        create_user_account_id=add_place.user_account_id,
        name=add_place.name,
        address=add_place.address,
        lon_lat=add_place.get_lon_lat_array(),
        prefecture_code=add_place.prefecture_code,
        category_id_list=add_place.category_id_list,
        detail=add_place.detail,
        url=add_place.url,
    )
    post_place.save()
    return post_place


def edit_post_place(edit_place: PostPlaceServiceModel) -> bool:
    result_list: List[PostPlace] = list(
        PostPlace.objects(
            (
                Q(_id=edit_place.id)
                & Q(create_user_account_id=edit_place.user_account_id)
            )
        )
    )
    if len(result_list) < 1:
        return False

    update_place = result_list[0]
    update_place.name = edit_place.name
    update_place.address = edit_place.address
    update_place.lon_lat = edit_place.get_lon_lat_array()
    update_place.prefecture_code = edit_place.prefecture_code
    update_place.category_id_list = edit_place.category_id_list
    update_place.detail = edit_place.detail
    update_place.url_list = edit_place.url_list
    update_place.save()

    return True


def find_post_places(
    user_account_id: str,
    id_filter: str | None,
    category_filter: str | None,
    name_filter: str | None,
) -> List[PostPlaceQueryServiceModel]:
    pipeline = [
        {"$match": {"create_user_account_id": user_account_id}},
        {
            "$sort": {"name": 1},
        },
        {
            "$lookup": {
                "from": "user_accounts",
                "localField": "create_user_account_id",
                "foreignField": "_id",
                "as": "user_accounts",
            }
        },
        {
            "$lookup": {
                "from": "post_categories",
                "localField": "category_id_list",
                "foreignField": "_id",
                "as": "post_categories",
            }
        },
        {"$unwind": "$user_accounts"},
        {"$limit": 200},
        {
            "$project": {
                "_id": 1,
                "name": 1,
                "user_setting_id": "$user_accounts.user_setting_id",
                "address": 1,
                "lon_lat": 1,
                "prefecture_code": 1,
                "category_id_list": 1,
                "detail": 1,
                "url_list": 1,
            }
        },
    ]

    if id_filter != None:
        pipeline.insert(0, {"$match": {"_id": id_filter}})
    if name_filter != None:
        pipeline.insert(
            0, {"$match": {{"name": {"$regex": name_filter, "$options": "i"}}}}
        )
    if category_filter != None:
        # category_filterがあった場合は対象の子も含めてcategory_idをリスト化
        category_id_list = list(
            map(
                lambda c: c._id,
                find_post_categories_with_children(user_account_id, category_filter),
            )
        )
        pipeline.append(
            {
                "$match": {
                    "post_categories.id": {"$elemMatch": {"$in": category_id_list}},
                }
            }
        )

    return list(
        map(
            lambda c_dict: PostPlaceQueryServiceModel(**c_dict),
            list(PostPlace.objects().aggregate(pipeline)),
        )
    )


def delete_place_by_id(
    place_id: str,
    user_account_id: str,
) -> bool:
    PostPlace.objects(
        Q(_id=place_id)
        & Q(
            create_user_account_id=user_account_id,
        )
    ).delete()

    return True
