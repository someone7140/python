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
