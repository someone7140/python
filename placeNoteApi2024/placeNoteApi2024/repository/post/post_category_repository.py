import sys
from typing import List
import uuid

from mongoengine import *

from placeNoteApi2024.graphql.strawberry_object import PostCategoryResponse
from placeNoteApi2024.models import PostCategory
from placeNoteApi2024.service_model.post_service_model import (
    PostCategoryQueryServiceModel,
    PostCategoryServiceModel,
)


def add_post_category(add_category: PostCategoryServiceModel) -> PostCategory:
    post_category = PostCategory(
        _id=str(uuid.uuid4()),
        create_user_account_id=add_category.user_account_id,
        name=add_category.name,
        parent_category_id=add_category.parent_category_id,
        display_order=add_category.display_order,
        memo=add_category.memo,
    )
    post_category.save()
    return post_category


def edit_post_category(
    edit_category: PostCategoryServiceModel,
) -> bool:
    result_list: List[PostCategory] = list(
        PostCategory.objects(
            (
                Q(_id=edit_category.id)
                & Q(create_user_account_id=edit_category.user_account_id)
            )
        )
    )
    if len(result_list) < 1:
        return False

    before_update_category = result_list[0]
    before_update_category.name = edit_category.name
    before_update_category.parent_category_id = edit_category.parent_category_id
    before_update_category.display_order = edit_category.display_order
    before_update_category.memo = edit_category.memo

    before_update_category.save()
    return True


def delete_category_by_id(
    category_id: str,
    user_account_id: str,
) -> bool:
    # 配下のカテゴリーの親カテゴリーをnullにする
    PostCategory.objects(
        Q(parent_category_id=category_id)
        & Q(
            create_user_account_id=user_account_id,
        )
    ).update(parent_category_id=None)

    # 自身を削除
    delete_categories_by_query(
        Q(_id=category_id)
        & Q(
            create_user_account_id=user_account_id,
        )
    )

    return True


def find_post_categories(
    user_account_id: str,
    id_filter: str | None,
    name_filter: str | None,
) -> List[PostCategoryQueryServiceModel]:
    pipeline = [
        {"$match": {"create_user_account_id": user_account_id}},
        {
            "$addFields": {"sort_field": {"$ifNull": ["$display_order", sys.maxsize]}},
        },
        {
            "$sort": {"sort_field": 1},
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
            "$project": {
                "_id": 1,
                "name": 1,
                "user_setting_id": "$user_accounts.user_setting_id",
                "parent_category_id": 1,
                "memo": 1,
                "display_order": 1,
            }
        },
    ]

    if id_filter != None:
        pipeline.insert(0, {"$match": {"_id": id_filter}})
    if name_filter != None:
        pipeline.insert(
            0, {"$match": {"name", {"$regex": name_filter, "$options": "i"}}}
        )

    return list(
        map(
            lambda c_dict: PostCategoryQueryServiceModel(**c_dict),
            list(PostCategory.objects().aggregate(pipeline)),
        )
    )


def delete_categories_by_query(query):
    PostCategory.objects(query).delete()


def find_post_categories_with_children(
    user_account_id: str,
    category_id: str,
) -> List[PostCategory]:
    list(
        PostCategory.objects(
            Q(create_user_account_id=user_account_id)
            & (Q(_id=category_id) | Q(parent_category_id=category_id))
        )
    )
