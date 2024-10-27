import datetime
from typing import List
import uuid

from mongoengine import *

from placeNoteApi2024.models import Post, UrlDetail, UrlInfo
from placeNoteApi2024.service_model.post_service_model import UrlServiceModel


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
        is_open=is_open,
        category_id_list=category_id_list,
        detail=detail,
        url_list=list(
            map(
                lambda url_model: UrlDetail(
                    url_id=url_model.url_id,
                    url=url_model.url,
                    url_type=url_model.url_type,
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
        ),
    )
    post.save()
    return post
