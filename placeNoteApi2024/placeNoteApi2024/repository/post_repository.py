import datetime
from typing import List
import uuid

from dacite import from_dict
from mongoengine import *

from placeNoteApi2024.models import Post, PostPlace, UrlDetail, UrlInfo
from placeNoteApi2024.repository.post_category_repository import (
    find_post_categories_with_children_by_ids,
)
from placeNoteApi2024.service_model.post_service_model import (
    PostQueryServiceModel,
    UrlServiceModel,
)


def add_post(
    user_account_id: str,
    title: str,
    place_id: str,
    visited_date: datetime.datetime,
    is_open: bool,
    category_id_list: List[str],
    detail: str | None,
    url_service_model_list: List[UrlServiceModel],
) -> Post:
    post = Post(
        _id=str(uuid.uuid4()),
        title=title,
        create_user_account_id=user_account_id,
        place_id=place_id,
        visited_date=visited_date,
        post_date=datetime.datetime.now(datetime.timezone.utc),
        is_open=is_open,
        category_id_list=category_id_list,
        detail=detail,
        url_list=get_url_list_for_db_model(url_service_model_list),
    )
    post.save()
    return post


def edit_post(
    user_account_id: str,
    id: str,
    title: str,
    place_id: str,
    visited_date: datetime.datetime,
    is_open: bool,
    category_id_list: List[str],
    detail: str | None,
    url_service_model_list: List[UrlServiceModel],
) -> bool:
    result_list: List[Post] = list(
        Post.objects((Q(_id=id) & Q(create_user_account_id=user_account_id)))
    )
    if len(result_list) < 1:
        return False

    update_post = result_list[0]
    update_post.title = title
    update_post.place_id = place_id
    update_post.visited_date = visited_date
    update_post.is_open = is_open
    update_post.category_id_list = category_id_list
    update_post.detail = detail
    update_post.url_list = get_url_list_for_db_model(url_service_model_list)
    update_post.save()

    return True


def delete_post_by_id(
    post_id: str,
    user_account_id: str,
) -> bool:
    PostPlace.objects(
        Q(_id=post_id)
        & Q(
            create_user_account_id=user_account_id,
        )
    ).delete()

    return True


def get_url_list_for_db_model(url_service_model_list: List[UrlServiceModel]):
    return list(
        map(
            lambda url_model: UrlDetail(
                url=url_model.url,
                url_type=url_model.url_type.value,
                url_info=(
                    UrlInfo(
                        title=url_model.url_info.title,
                        image_url=url_model.url_info.image_url,
                        site_name=url_model.url_info.site_name,
                    )
                    if url_model.url_info != None
                    else None
                ),
                embed_html=url_model.embed_html,
            ),
            url_service_model_list,
        )
    )


def find_posts(
    user_account_id: str | None,
    id_filter: str | None,
    category_ids_filter: List[str] | None,
    place_id_filter: str | None,
    is_open_only: bool,
    is_order_post_date: bool,
    limit: int,
) -> List[PostQueryServiceModel]:
    pipeline = [
        {
            "$sort": (
                {"post_date": -1} if is_order_post_date else {"visited_date": -1}
            ),
        },
        {
            "$lookup": {
                "from": "user_accounts",
                "localField": "create_user_account_id",
                "foreignField": "_id",
                "as": "user_accounts",
            }
        },
        {"$unwind": "$user_accounts"},
        {
            "$lookup": {
                "from": "post_places",
                "localField": "place_id",
                "foreignField": "_id",
                "as": "post_place",
            }
        },
        {"$unwind": "$post_place"},
        {
            "$lookup": {
                "from": "post_categories",
                "localField": "category_id_list",
                "foreignField": "_id",
                "as": "post_categories",
            }
        },
        {"$limit": limit},
        {
            "$project": {
                "_id": 1,
                "title": 1,
                "user_setting_id": "$user_accounts.user_setting_id",
                "place": "$post_place",
                "is_open": 1,
                "visited_date": 1,
                "post_date": 1,
                "category_id_list": 1,
                "detail": 1,
                "url_list": 1,
            }
        },
    ]

    if id_filter != None:
        pipeline.insert(0, {"$match": {"_id": id_filter}})
    if place_id_filter != None:
        pipeline.insert(0, {"$match": {"place_id": place_id_filter}})
    if is_open_only:
        pipeline.insert(0, {"$match": {"is_open": True}})
    if user_account_id != None:
        pipeline.insert(0, {"$match": {"create_user_account_id": user_account_id}})
    if category_ids_filter != None:
        # category_filterがあった場合は対象の子も含めてcategory_idをリスト化
        category_id_list = list(
            map(
                lambda c: c._id,
                find_post_categories_with_children_by_ids(
                    user_account_id, category_ids_filter
                ),
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
            lambda c_dict: from_dict(data_class=PostQueryServiceModel, data=c_dict),
            list(Post.objects().aggregate(pipeline)),
        )
    )
