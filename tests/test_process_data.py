import pandas as pd
from src.load_data import load_csv
from src.process_data import clean_and_prepare

def test_clean_and_prepare_structure():
    df = load_csv("data/social_media_vs_productivity.csv")
    cleaned_df = clean_and_prepare(df)

    assert isinstance(cleaned_df, pd.DataFrame)
    assert not cleaned_df.isnull().any().any()

    # Check dtypes
    assert cleaned_df['uses_focus_apps'].dtype == bool
    assert cleaned_df['gender'].dtype.name == 'category'
