import sys
from typing import List
import uuid

from mongoengine import *

from placeNoteApi2024.models import PostCategory
from placeNoteApi2024.service_model.post_service_model import PostCategoryServiceModel


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
    before_update_category.update(
        name=edit_category.name,
        parent_category_id=edit_category.parent_category_id,
        display_order=edit_category.display_order,
        memo=edit_category.memo,
    )
    return True


def delete_category_by_id(
    category_id: str,
    user_account_id: str,
) -> bool:
    # 配下のカテゴリーを削除
    delete_categories_by_query(
        Q(parent_category_id=category_id)
        & Q(
            create_user_account_id=user_account_id,
        )
    )
    # 自身を削除
    delete_categories_by_query(
        Q(_id=category_id)
        & Q(
            create_user_account_id=user_account_id,
        )
    )

    return True


def find_post_categories(
    user_account_id: str, name_filter: str | None
) -> List[PostCategory]:
    pipeline = [
        {"$match": {"create_user_account_id": user_account_id}},
        {
            "$addFields": {"sort_field": {"$ifNull": ["$display_order", sys.maxsize]}},
        },
        {
            "$sort": {"sort_field": 1},
        },
        {
            "$project": {
                "_id": 1,
                "name": 1,
                "create_user_account_id": 1,
                "parent_category_id": 1,
                "memo": 1,
                "display_order": 1,
            }
        },
    ]
    if name_filter != None:
        pipeline.insert(
            0, {"$match": {"name", {"$regex": name_filter, "$options": "i"}}}
        )

    return list(
        map(
            lambda c_dict: PostCategory(**c_dict),
            list(PostCategory.objects().aggregate(pipeline)),
        )
    )


def delete_categories_by_query(query):
    PostCategory.objects(query).delete()
