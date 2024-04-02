from datetime import datetime, timedelta
from typing import Dict
from zoneinfo import ZoneInfo

import jwt

from placeNoteApi2024.settings import ENV, TIME_ZONE


def encode_jwt(payload_dict: Dict, exp_after_seconds: int) -> str:
    payload_dict["exp"] = datetime.now(ZoneInfo(TIME_ZONE)) + timedelta(
        seconds=exp_after_seconds
    )
    jwt_token = jwt.encode(
        payload_dict,
        key=ENV.get_value("JWT_SECRET"),
        algorithm=ENV.get_value("JWT_ALGORITHM"),
    )

    return jwt_token


def decode_jwt(jwt_token: str) -> Dict | None:
    try:
        return jwt.decode(
            jwt_token,
            key=ENV.get_value("JWT_SECRET"),
            algorithms=ENV.get_value("JWT_ALGORITHM"),
        )
    except Exception:
        return None
