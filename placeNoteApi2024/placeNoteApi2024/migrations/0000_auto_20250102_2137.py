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
    CreateEmbedded('~UrlInfo'),
    CreateEmbedded('~UrlDetail'),
    CreateDocument('PostCategory', collection='post_categories'),
    CreateDocument('Post', collection='posts'),
    CreateDocument('UserAccount', collection='user_accounts'),
    CreateDocument('PostPlace', collection='post_places'),
    CreateField('~UrlInfo', 'image_url', choices=None, db_field='image_url', default=None,
        max_length=None, min_length=None, null=False, primary_key=False, regex=None,
        required=False, sparse=False, type_key='StringField', unique=False, unique_with=None),
    CreateField('~UrlInfo', 'site_name', choices=None, db_field='site_name', default=None,
        max_length=None, min_length=None, null=False, primary_key=False, regex=None,
        required=False, sparse=False, type_key='StringField', unique=False, unique_with=None),
    CreateField('~UrlInfo', 'title', choices=None, db_field='title', default=None,
        max_length=None, min_length=None, null=False, primary_key=False, regex=None,
        required=False, sparse=False, type_key='StringField', unique=False, unique_with=None),
    CreateField('~UrlDetail', 'url', choices=None, db_field='url', default=None,
        max_length=None, min_length=None, null=False, primary_key=False, regex=None,
        required=True, sparse=False, type_key='StringField', unique=False, unique_with=None),
    CreateField('~UrlDetail', 'url_info', choices=None, db_field='url_info', default=None,
        null=False, primary_key=False, required=False, sparse=False, target_doctype='~UrlInfo',
        type_key='EmbeddedDocumentField', unique=False, unique_with=None),
    CreateField('~UrlDetail', 'url_type', choices=None, db_field='url_type', default=None,
        max_length=None, min_length=None, null=False, primary_key=False, regex=None,
        required=True, sparse=False, type_key='StringField', unique=False, unique_with=None),
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
    CreateField('PostCategory', 'detail', choices=None, db_field='detail', default=None,
        max_length=None, min_length=None, null=False, primary_key=False, regex=None,
        required=False, sparse=False, type_key='StringField', unique=False, unique_with=None),
    CreateField('PostCategory', 'display_order', choices=None, db_field='display_order',
        default=None, max_value=None, min_value=None, null=False, primary_key=False,
        required=False, sparse=False, type_key='IntField', unique=False, unique_with=None),
    CreateField('PostCategory', 'create_user_account_id', choices=None,
        db_field='create_user_account_id', default=None, max_length=None, min_length=None,
        null=False, primary_key=False, regex=None, required=True, sparse=False,
        type_key='StringField', unique=False, unique_with=None),
    CreateField('Post', 'auto_id_0', choices=None, db_field='_auto_id_0', default=None,
        null=False, primary_key=False, required=False, sparse=False, type_key='ObjectIdField',
        unique=False, unique_with=None),
    CreateField('Post', 'category_id_list', choices=None, db_field='category_id_list',
        default=[], max_length=None, null=False, primary_key=False, required=False,
        sparse=False, type_key='ListField', unique=False, unique_with=None),
    CreateField('Post', 'place_id', choices=None, db_field='place_id', default=None,
        max_length=None, min_length=None, null=False, primary_key=False, regex=None,
        required=True, sparse=False, type_key='StringField', unique=False, unique_with=None),
    CreateField('Post', 'title', choices=None, db_field='title', default=None,
        max_length=None, min_length=None, null=False, primary_key=False, regex=None,
        required=True, sparse=False, type_key='StringField', unique=False, unique_with=None),
    CreateField('Post', 'post_date', choices=None, db_field='post_date', default=None,
        null=False, primary_key=False, required=True, sparse=False, type_key='DateTimeField',
        unique=False, unique_with=None),
    CreateField('Post', 'detail', choices=None, db_field='detail', default=None,
        max_length=None, min_length=None, null=False, primary_key=False, regex=None,
        required=False, sparse=False, type_key='StringField', unique=False, unique_with=None),
    CreateField('Post', 'url_list', choices=None, db_field='url_list', default=[],
        max_length=None, null=False, primary_key=False, required=False, sparse=False,
        type_key='ListField', unique=False, unique_with=None),
    CreateField('Post', 'is_open', choices=None, db_field='is_open', default=None,
        null=False, primary_key=False, required=True, sparse=False, type_key='BooleanField',
        unique=False, unique_with=None),
    CreateField('Post', 'visited_date', choices=None, db_field='visited_date', default=None,
        null=False, primary_key=False, required=True, sparse=False, type_key='DateTimeField',
        unique=False, unique_with=None),
    CreateField('Post', 'create_user_account_id', choices=None,
        db_field='create_user_account_id', default=None, max_length=None, min_length=None,
        null=False, primary_key=False, regex=None, required=True, sparse=False,
        type_key='StringField', unique=False, unique_with=None),
    CreateField('UserAccount', 'auto_id_0', choices=None, db_field='_auto_id_0',
        default=None, null=False, primary_key=False, required=False, sparse=False,
        type_key='ObjectIdField', unique=False, unique_with=None),
    CreateField('UserAccount', 'name', choices=None, db_field='name', default=None,
        max_length=None, min_length=None, null=False, primary_key=False, regex=None,
        required=True, sparse=False, type_key='StringField', unique=False, unique_with=None),
    CreateField('UserAccount', 'password', choices=None, db_field='password', default=None,
        max_length=None, min_length=None, null=False, primary_key=False, regex=None,
        required=False, sparse=False, type_key='StringField', unique=False, unique_with=None),
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
    CreateField('UserAccount', 'user_setting_id', choices=None, db_field='user_setting_id',
        default=None, max_length=None, min_length=None, null=False, primary_key=False,
        regex=None, required=True, sparse=False, type_key='StringField', unique=True,
        unique_with=None),
    CreateField('PostPlace', 'auto_id_0', choices=None, db_field='_auto_id_0', default=None,
        null=False, primary_key=False, required=False, sparse=False, type_key='ObjectIdField',
        unique=False, unique_with=None),
    CreateField('PostPlace', 'url', choices=None, db_field='url', default=None,
        max_length=None, min_length=None, null=False, primary_key=False, regex=None,
        required=False, sparse=False, type_key='StringField', unique=False, unique_with=None),
    CreateField('PostPlace', 'name', choices=None, db_field='name', default=None,
        max_length=None, min_length=None, null=False, primary_key=False, regex=None,
        required=True, sparse=False, type_key='StringField', unique=False, unique_with=None),
    CreateField('PostPlace', 'category_id_list', choices=None, db_field='category_id_list',
        default=[], max_length=None, null=False, primary_key=False, required=False,
        sparse=False, type_key='ListField', unique=False, unique_with=None),
    CreateField('PostPlace', 'prefecture_code', choices=None, db_field='prefecture_code',
        default=None, max_length=None, min_length=None, null=False, primary_key=False,
        regex=None, required=False, sparse=False, type_key='StringField', unique=False,
        unique_with=None),
    CreateField('PostPlace', 'lon_lat', choices=None, db_field='lon_lat', default=[],
        max_length=None, null=False, primary_key=False, required=False, sparse=False,
        type_key='ListField', unique=False, unique_with=None),
    CreateField('PostPlace', 'detail', choices=None, db_field='detail', default=None,
        max_length=None, min_length=None, null=False, primary_key=False, regex=None,
        required=False, sparse=False, type_key='StringField', unique=False, unique_with=None),
    CreateField('PostPlace', 'address', choices=None, db_field='address', default=None,
        max_length=None, min_length=None, null=False, primary_key=False, regex=None,
        required=False, sparse=False, type_key='StringField', unique=False, unique_with=None),
    CreateField('PostPlace', 'create_user_account_id', choices=None,
        db_field='create_user_account_id', default=None, max_length=None, min_length=None,
        null=False, primary_key=False, regex=None, required=True, sparse=False,
        type_key='StringField', unique=False, unique_with=None),
    CreateIndex('PostCategory', 'name_1', fields=[('name', pymongo.ASCENDING)],
        collation={'locale': 'ja'}),
    CreateIndex('PostCategory', 'parent_category_id_1', fields=[('parent_category_id',
        pymongo.ASCENDING)]),
    CreateIndex('PostCategory', 'create_user_account_id_1',
        fields=[('create_user_account_id', pymongo.ASCENDING)]),
    CreateIndex('Post', 'title_1', fields=[('title', pymongo.ASCENDING)],
        collation={'locale': 'ja'}),
    CreateIndex('Post', 'visited_date_1', fields=[('visited_date', pymongo.ASCENDING)]),
    CreateIndex('Post', 'create_user_account_id_1', fields=[('create_user_account_id',
        pymongo.ASCENDING)]),
    CreateIndex('Post', 'place_id_1', fields=[('place_id', pymongo.ASCENDING)]),
    CreateIndex('Post', 'category_id_list_1', fields=[('category_id_list',
        pymongo.ASCENDING)]),
    CreateIndex('Post', 'post_date_1', fields=[('post_date', pymongo.ASCENDING)]),
    CreateIndex('UserAccount', 'name_1', fields=[('name', pymongo.ASCENDING)],
        collation={'locale': 'ja'}),
    CreateIndex('UserAccount', 'user_setting_id_1', fields=[('user_setting_id',
        pymongo.ASCENDING)], sparse=False, unique=True),
    CreateIndex('UserAccount', 'email_1_gmail_1', fields=[('email', pymongo.ASCENDING),
        ('gmail', pymongo.ASCENDING)], sparse=False, unique=True),
    CreateIndex('PostPlace', 'name_1', fields=[('name', pymongo.ASCENDING)],
        collation={'locale': 'ja'}),
    CreateIndex('PostPlace', 'lon_lat_2dsphere', fields=[('lon_lat', pymongo.GEOSPHERE)]),
    CreateIndex('PostPlace', 'create_user_account_id_1', fields=[('create_user_account_id',
        pymongo.ASCENDING)]),
    CreateIndex('PostPlace', 'address_1', fields=[('address', pymongo.ASCENDING)],
        collation={'locale': 'ja'}),
    CreateIndex('PostPlace', 'category_id_list_1', fields=[('category_id_list',
        pymongo.ASCENDING)]),
    CreateIndex('PostPlace', 'prefecture_code_1', fields=[('prefecture_code',
        pymongo.ASCENDING)]),
]