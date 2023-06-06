from soprasteria.inventory import MARKETING_COLUMNS
import pandas as pd
from dataclasses import astuple


def get_marketing_columns_info(marketing_df: pd.DataFrame) -> list[pd.Series]:
    column_infos = [
        marketing_df[col].value_counts(dropna=False)
        for col in astuple(MARKETING_COLUMNS)
    ]

    return column_infos
