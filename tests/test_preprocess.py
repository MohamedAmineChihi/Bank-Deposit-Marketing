import pandas as pd
from soprasteria.inventory import MARKETING_COLUMNS


def test_preprocess_socio_eco_df():
    pass


def test_preproces_marketing_df():
    # With
    from soprasteria.preprocess import preproces_marketing_df

    marketing_df = pd.DataFrame(
        {
            MARKETING_COLUMNS.education: ["  education 1  ", "  education 2"],
            MARKETING_COLUMNS.job: ["   job 1", "   job     2"],
            "float_column": [1, 2],
        },
        dtype=str,
    )

    expected_output = pd.DataFrame(
        {
            MARKETING_COLUMNS.education: ["education 1", "education 2"],
            MARKETING_COLUMNS.job: ["job 1", "job     2"],
            "float_column": ["1", "2"],
        },
        dtype=str,
    )
    # When
    output = preproces_marketing_df(marketing_df)

    # Then
    pd.testing.assert_frame_equal(expected_output, output)
