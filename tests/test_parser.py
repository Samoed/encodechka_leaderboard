import pandas as pd
import pytest
from src.encodechka import parser


@pytest.mark.vcr
def test_parser():
    df = parser.get_readme_df()
    assert isinstance(df, pd.DataFrame)
    assert df.shape[1] == 16