from dataclasses import dataclass


@dataclass
class PostCategoryServiceModel:
    user_account_id: str
    name: str
    id: str | None = None
    parent_category_id: str | None = None
    display_order: int | None = None
    detail: str | None = None


@dataclass
class PostCategoryQueryServiceModel:
    _id: str
    user_setting_id: str
    name: str
    parent_category_id: str | None = None
    display_order: int | None = None
    detail: str | None = None
