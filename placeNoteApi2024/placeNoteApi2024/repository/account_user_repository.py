from typing import List
import uuid

from mongoengine import *

from placeNoteApi2024.models import UserAccount


def add_user_account(
    user_setting_id: str, name: str, gmail: str | None, image_url: str | None
) -> UserAccount:
    user_account = UserAccount(
        _id=str(uuid.uuid4()),
        user_setting_id=user_setting_id,
        name=name,
        gmail=gmail,
        image_url=image_url,
    )
    user_account.save()
    return user_account


def update_account_user(
    user_account_id: str,
    user_setting_id: str,
    name: str,
    image_url: str | None,
) -> bool:
    result_list = get_user_accounts_by_query(Q(_id=user_account_id))
    if len(result_list) < 1:
        return False

    update_user = result_list[0]
    update_user.user_setting_id = user_setting_id
    update_user.name = name
    if image_url != None:
        update_user.image_url = image_url
    update_user.save()

    return True


def get_user_accounts_by_query(query) -> List[UserAccount]:
    return list(UserAccount.objects(query))
