from dataclasses import dataclass


@dataclass
class PostCategoryServiceModel:
    id: str | None
    user_account_id: str
    name: str
    parent_category_id: str | None
    display_order: int | None
    memo: str | None
