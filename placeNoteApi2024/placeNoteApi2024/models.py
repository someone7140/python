from mongoengine import Document, fields


class UserAccount(Document):
    _id = fields.StringField(required=True)
    name = fields.StringField(required=True)
    user_setting_id = fields.StringField(unique=True, required=True)
    gmail = fields.StringField()
    email = fields.StringField(unique_with="gmail")
    password = fields.StringField()
    image_url = fields.StringField()
    meta = {"collection": "user_accounts"}


class PostCategory(Document):
    _id = fields.StringField(required=True)
    name = fields.StringField(required=True)
    create_user_account_id = fields.StringField(required=True)
    parent_category_id = fields.StringField()
    display_order = fields.IntField()
    detail = fields.StringField()
    meta = {
        "collection": "post_categories",
        "indexes": ["create_user_account_id", "parent_category_id"],
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
    url_list = fields.ListField(fields.StringField())
    meta = {
        "collection": "post_places",
        "indexes": [
            "create_user_account_id",
            "prefecture_code",
            "category_id_list",
            [("lon_lat", "2dsphere")],
        ],
    }
