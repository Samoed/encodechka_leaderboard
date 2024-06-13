from io import StringIO

import pandas as pd
import markdown
import requests
from settings import get_settings


def get_readme() -> str:
    url = "https://raw.githubusercontent.com/avidale/encodechka/master/README.md"
    response = requests.get(url)
    return response.text


def get_readme_html() -> str:
    return markdown.markdown(get_readme(), extensions=['tables'])


def get_readme_df() -> pd.DataFrame:
    performance, leaderboard = pd.read_html(StringIO(get_readme_html()))
    performance = performance.set_index("model")
    leaderboard = leaderboard.set_index("model")
    df = pd.concat([performance, leaderboard], axis=1)
    return df


def update_leaderboard_table() -> None:
    df = get_readme_df()
    df.to_csv(get_settings().LEADERBOARD_FILE_PATH)
