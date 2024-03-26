from mongoengine_migrate.actions import *
import pymongo

# Existing data processing policy
# Possible values are: strict, relaxed
policy = "strict"

# Names of migrations which the current one is dependent by
dependencies = [
]

# Action chain
actions = [
    CreateDocument('UserAccount', collection='user_accounts'),
    CreateField('UserAccount', 'user_setting_id', choices=None, db_field='user_setting_id',
        default=None, max_length=None, min_length=None, null=False, primary_key=False,
        regex=None, required=True, sparse=False, type_key='StringField', unique=True,
        unique_with=None),
    CreateField('UserAccount', 'email', choices=None, db_field='email', default=None,
        max_length=None, min_length=None, null=False, primary_key=False, regex=None,
        required=False, sparse=False, type_key='StringField', unique=True,
        unique_with=['gmail']),
    CreateField('UserAccount', 'gmail', choices=None, db_field='gmail', default=None,
        max_length=None, min_length=None, null=False, primary_key=False, regex=None,
        required=True, sparse=False, type_key='StringField', unique=False, unique_with=None),
    CreateField('UserAccount', 'auto_id_0', choices=None, db_field='_auto_id_0',
        default=None, null=False, primary_key=False, required=False, sparse=False,
        type_key='ObjectIdField', unique=False, unique_with=None),
    CreateField('UserAccount', 'password', choices=None, db_field='password', default=None,
        max_length=None, min_length=None, null=False, primary_key=False, regex=None,
        required=False, sparse=False, type_key='StringField', unique=False, unique_with=None),
    CreateField('UserAccount', 'name', choices=None, db_field='name', default=None,
        max_length=None, min_length=None, null=False, primary_key=False, regex=None,
        required=True, sparse=False, type_key='StringField', unique=False, unique_with=None),
    CreateField('UserAccount', 'image_url', choices=None, db_field='image_url',
        default=None, max_length=None, min_length=None, null=False, primary_key=False,
        regex=None, required=False, sparse=False, type_key='StringField', unique=False,
        unique_with=None),
    CreateIndex('UserAccount', 'email_1_gmail_1', fields=[('email', pymongo.ASCENDING),
        ('gmail', pymongo.ASCENDING)], sparse=False, unique=True),
    CreateIndex('UserAccount', 'user_setting_id_1', fields=[('user_setting_id',
        pymongo.ASCENDING)], sparse=False, unique=True),
]