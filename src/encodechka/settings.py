import os

from huggingface_hub import HfApi
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # TOKEN: str
    OWNER: str = "Samoed"
    REPO_ID: str = f"{OWNER}/Encodechka"
    QUEUE_REPO: str = f"{OWNER}/requests"
    RESULTS_REPO: str = f"{OWNER}/results"
    CACHE_PATH: str = "."
    EVAL_REQUESTS_PATH: str = os.path.join(CACHE_PATH, "eval-queue")
    EVAL_RESULTS_PATH: str = os.path.join(CACHE_PATH, "eval-results")
    EVAL_REQUESTS_PATH_BACKEND: str = os.path.join(CACHE_PATH, "eval-queue-bk")
    EVAL_RESULTS_PATH_BACKEND: str = os.path.join(CACHE_PATH, "eval-results-bk")
    ENCODECHKA_URL: str = "https://raw.githubusercontent.com/avidale/encodechka/master/README.md"
    LEADERBOARD_FILE_PATH: str = os.path.join(CACHE_PATH, "leaderboard.csv")


def get_settings():
    return Settings()


# API = HfApi(token=get_settings().TOKEN)
