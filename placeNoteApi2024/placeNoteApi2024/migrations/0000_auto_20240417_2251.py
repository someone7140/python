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
    CreateDocument('PostCategory', collection='post_categories'),
    CreateField('UserAccount', 'user_setting_id', choices=None, db_field='user_setting_id',
        default=None, max_length=None, min_length=None, null=False, primary_key=False,
        regex=None, required=True, sparse=False, type_key='StringField', unique=True,
        unique_with=None),
    CreateField('UserAccount', 'auto_id_0', choices=None, db_field='_auto_id_0',
        default=None, null=False, primary_key=False, required=False, sparse=False,
        type_key='ObjectIdField', unique=False, unique_with=None),
    CreateField('UserAccount', 'password', choices=None, db_field='password', default=None,
        max_length=None, min_length=None, null=False, primary_key=False, regex=None,
        required=False, sparse=False, type_key='StringField', unique=False, unique_with=None),
    CreateField('UserAccount', 'name', choices=None, db_field='name', default=None,
        max_length=None, min_length=None, null=False, primary_key=False, regex=None,
        required=True, sparse=False, type_key='StringField', unique=False, unique_with=None),
    CreateField('UserAccount', 'gmail', choices=None, db_field='gmail', default=None,
        max_length=None, min_length=None, null=False, primary_key=False, regex=None,
        required=True, sparse=False, type_key='StringField', unique=False, unique_with=None),
    CreateField('UserAccount', 'email', choices=None, db_field='email', default=None,
        max_length=None, min_length=None, null=False, primary_key=False, regex=None,
        required=False, sparse=False, type_key='StringField', unique=True,
        unique_with=['gmail']),
    CreateField('UserAccount', 'image_url', choices=None, db_field='image_url',
        default=None, max_length=None, min_length=None, null=False, primary_key=False,
        regex=None, required=False, sparse=False, type_key='StringField', unique=False,
        unique_with=None),
    CreateField('PostCategory', 'create_user_account_id', choices=None,
        db_field='create_user_account_id', default=None, max_length=None, min_length=None,
        null=False, primary_key=False, regex=None, required=True, sparse=False,
        type_key='StringField', unique=False, unique_with=None),
    CreateField('PostCategory', 'auto_id_0', choices=None, db_field='_auto_id_0',
        default=None, null=False, primary_key=False, required=False, sparse=False,
        type_key='ObjectIdField', unique=False, unique_with=None),
    CreateField('PostCategory', 'name', choices=None, db_field='name', default=None,
        max_length=None, min_length=None, null=False, primary_key=False, regex=None,
        required=True, sparse=False, type_key='StringField', unique=False, unique_with=None),
    CreateField('PostCategory', 'parent_category_id', choices=None,
        db_field='parent_category_id', default=None, max_length=None, min_length=None,
        null=False, primary_key=False, regex=None, required=False, sparse=False,
        type_key='StringField', unique=False, unique_with=None),
    CreateField('PostCategory', 'display_order', choices=None, db_field='display_order',
        default=None, max_value=None, min_value=None, null=False, primary_key=False,
        required=False, sparse=False, type_key='IntField', unique=False, unique_with=None),
    CreateField('PostCategory', 'memo', choices=None, db_field='memo', default=None,
        max_length=None, min_length=None, null=False, primary_key=False, regex=None,
        required=False, sparse=False, type_key='StringField', unique=False, unique_with=None),
    CreateIndex('UserAccount', 'email_1_gmail_1', fields=[('email', pymongo.ASCENDING),
        ('gmail', pymongo.ASCENDING)], sparse=False, unique=True),
    CreateIndex('UserAccount', 'user_setting_id_1', fields=[('user_setting_id',
        pymongo.ASCENDING)], sparse=False, unique=True),
    CreateIndex('PostCategory', 'parent_category_id_1', fields=[('parent_category_id',
        pymongo.ASCENDING)]),
    CreateIndex('PostCategory', 'create_user_account_id_1',
        fields=[('create_user_account_id', pymongo.ASCENDING)]),
]