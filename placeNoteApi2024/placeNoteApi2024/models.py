from mongoengine import (
    Document,
    EmbeddedDocument,
    EmbeddedDocumentField,
    fields,
)


class UserAccount(Document):
    _id = fields.StringField(required=True)
    name = fields.StringField(required=True)
    user_setting_id = fields.StringField(unique=True, required=True)
    gmail = fields.StringField()
    email = fields.StringField(unique_with="gmail")
    password = fields.StringField()
    image_url = fields.StringField()
    meta = {
        "collection": "user_accounts",
        "indexes": [{"fields": ["name"], "collation": {"locale": "ja"}}],
    }


class PostCategory(Document):
    _id = fields.StringField(required=True)
    name = fields.StringField(required=True)
    create_user_account_id = fields.StringField(required=True)
    parent_category_id = fields.StringField()
    display_order = fields.IntField()
    detail = fields.StringField()
    meta = {
        "collection": "post_categories",
        "indexes": [
            "create_user_account_id",
            "parent_category_id",
            {"fields": ["name"], "collation": {"locale": "ja"}},
        ],
    }


class PostPlace(Document):
    _id = fields.StringField(required=True)
    name = fields.StringField(required=True)
    create_user_account_id = fields.StringField(required=True)
    address = fields.StringField()
    lon_lat = fields.ListField(fields.FloatField())
    prefecture_code = fields.StringField()
    category_id_list = fields.ListField(fields.StringField())
    detail = fields.StringField()
    url = fields.StringField()
    meta = {
        "collection": "post_places",
        "indexes": [
            "create_user_account_id",
            "prefecture_code",
            "category_id_list",
            [("lon_lat", "2dsphere")],
            {"fields": ["name"], "collation": {"locale": "ja"}},
            {"fields": ["address"], "collation": {"locale": "ja"}},
        ],
    }


class UrlInfo(EmbeddedDocument):
    title = fields.StringField()
    image_url = fields.StringField()
    site_name = fields.StringField()


class UrlDetail(EmbeddedDocument):
    url = fields.StringField(required=True)
    url_type = fields.StringField(required=True)
    url_info = EmbeddedDocumentField(UrlInfo)


class Post(Document):
    _id = fields.StringField(required=True)
    title = fields.StringField(required=True)
    create_user_account_id = fields.StringField(required=True)
    place_id = fields.StringField(required=True)
    visited_date = fields.DateTimeField(required=True)
    post_date = fields.DateTimeField(required=True)
    is_open = fields.BooleanField(required=True)
    category_id_list = fields.ListField(fields.StringField())
    detail = fields.StringField()
    url_list = fields.ListField(EmbeddedDocumentField(UrlDetail))
    meta = {
        "collection": "posts",
        "indexes": [
            "create_user_account_id",
            "place_id",
            "visited_date",
            "post_date",
            "category_id_list",
            {"fields": ["title"], "collation": {"locale": "ja"}},
        ],
    }
