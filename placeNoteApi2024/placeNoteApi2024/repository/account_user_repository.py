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


def get_user_accounts_by_query(query) -> List[UserAccount]:
    return list(UserAccount.objects(query))
