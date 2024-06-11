import pandas as pd


def extract(filename):
    return pd.read_csv(filename)


def clean(df: pd.DataFrame) -> pd.DataFrame:
    new = df.dropna()
    no_duplicates = new.drop_duplicates()
    return no_duplicates


def transform(df: pd.DataFrame) -> pd.DataFrame:
    # Escape double quotes in STRING type values where needed
    string_columns = ["industry_code", "industry_name", "rme_size_grp", "variable", "unit"]
    for column in string_columns:
        df[column] = df[column].str.replace('"', '""')

    # Fill empty values with Double Quotes for all columns
    df.fillna('', inplace=True)

    # Transform year value into timestamp object for the first moment of that year
    df['year'] = pd.to_datetime(df['year'].astype(str), format='%Y').astype(int) / 10 ** 9
    return df
