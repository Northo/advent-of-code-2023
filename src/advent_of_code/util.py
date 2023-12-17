import requests
from pydantic_settings import BaseSettings, SettingsConfigDict


class Session(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    session_cookie: str = "secret_session_cookie"


def _input_file_url(day: int) -> str:
    return f"https://adventofcode.com/2023/day/{day}/input"


def _get_input_text(day: int, session_cookie: str) -> str:
    """Retrieve the input of day."""
    return requests.get(
        url=_input_file_url(day),
        cookies={"session": session_cookie},
    ).text


def get_input_text(day: int) -> str:
    return _get_input_text(
        day,
        session_cookie=Session().session_cookie,
    )
