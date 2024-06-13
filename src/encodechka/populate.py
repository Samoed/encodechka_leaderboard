import pandas as pd

from display.formatting import make_clickable_model
from display.utils import AutoEvalColumn
from settings import Settings


def get_leaderboard_df() -> pd.DataFrame:
    """Creates a dataframe from all the individual experiment results"""
    df = pd.read_csv(Settings().LEADERBOARD_FILE_PATH).sort_values(by="STS", ascending=False)
    df[AutoEvalColumn.is_private.name] = df["model"].apply(lambda x: "/" in x)
    df["model"] = df["model"].apply(make_clickable_model)
    return df
