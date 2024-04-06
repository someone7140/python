import os
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build

from placeNoteApi2024.settings import BASE_DIR, ENV


def get_gmail_from_auth_code(
    auth_code: str,
) -> str | None:
    try:
        flow = Flow.from_client_secrets_file(
            os.path.join(BASE_DIR, ENV.get_value("GOOGLE_SECRETS_PATH")),
            scopes=[
                "openid",
                "https://www.googleapis.com/auth/contacts.readonly",
                "https://www.googleapis.com/auth/userinfo.profile",
                "https://www.googleapis.com/auth/calendar",
                "https://www.googleapis.com/auth/userinfo.email",
                "https://www.googleapis.com/auth/drive.apps.readonly",
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
