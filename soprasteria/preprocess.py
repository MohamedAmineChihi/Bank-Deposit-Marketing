import pandas as pd
from soprasteria.inventory import COLUMNS, MARKETING_COLUMNS


def preprocess_socio_eco_df(socio_eco_df: pd.DataFrame) -> pd.DataFrame:
    # Convert the 'date' column to datetime
    socio_eco_df[COLUMNS.date] = pd.to_datetime(
        socio_eco_df[COLUMNS.date], dayfirst=True
    )

    # Handling the missing values
    socio_eco_df = socio_eco_df.replace("???", float("nan"))

    # Convert columns to numeric
    socio_eco_df[COLUMNS.variation_emploi] = pd.to_numeric(
        socio_eco_df[COLUMNS.variation_emploi]
    )
    socio_eco_df[COLUMNS.indice_prix] = pd.to_numeric(socio_eco_df[COLUMNS.indice_prix])
    socio_eco_df[COLUMNS.indice_consommateur] = pd.to_numeric(
        socio_eco_df[COLUMNS.indice_consommateur]
    )

    # Filling the `tx_var_emploi` NaN with trimestrial data extrapolation
    missing_map = {4: -0.1, 8: -0.2, 9: -0.2, 20: -3, 21: -3}
    socio_eco_df[COLUMNS.variation_emploi].fillna(missing_map, inplace=True)

    # Perform linear interpolation to the rest of the missing Values
    socio_eco_df.interpolate(method="linear", inplace=True)

    return socio_eco_df


def preproces_marketing_df(marketing_df: pd.DataFrame) -> pd.DataFrame:
    columns_to_modify = [MARKETING_COLUMNS.education, MARKETING_COLUMNS.job]

    for column in columns_to_modify:
        marketing_df[column] = marketing_df[column].astype(str)
        marketing_df[column] = marketing_df[column].str.strip()

    return marketing_df
