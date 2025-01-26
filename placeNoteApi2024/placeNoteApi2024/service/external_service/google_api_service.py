import os
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from google.cloud import storage
from google.cloud.storage.bucket import Bucket
from google.oauth2 import service_account

from placeNoteApi2024.settings import BASE_DIR, ENV


def get_gmail_from_auth_code(
    auth_code: str,
) -> str | None:
    try:
        flow = Flow.from_client_secrets_file(
            os.path.join(BASE_DIR, ENV.get_value("GOOGLE_CREDENTIAL_PATH")),
            scopes=[
                "openid",
                "https://www.googleapis.com/auth/userinfo.profile",
                "https://www.googleapis.com/auth/userinfo.email",
            ],
            redirect_uri=ENV.get_value("FRONTEND_DOMAIN"),
        )
        flow.fetch_token(code=auth_code)
        credentials = flow.credentials

        user_info = (
            build("oauth2", "v2", credentials=credentials).userinfo().get().execute()
        )
        return user_info["email"]
    except Exception as e:
        return None


def get_gcs_bucket() -> Bucket:
    credential = service_account.Credentials.from_service_account_file(
        ENV.get_value("GCS_KEY_PATH")
    )
    storage_client = storage.Client(
        project=ENV.get_value("GOOGLE_PROJECT_ID"), credentials=credential
    )
    bucket = storage_client.bucket(ENV.get_value("GCS_BUCKET"))
    return bucket
