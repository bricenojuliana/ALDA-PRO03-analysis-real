import pandas as pd
from src.load_data import load_csv

def clean_and_prepare(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and transforms the data:
    - Converts booleans and categoricals.
    - Fills or removes nulls.
    - Ensures no missing values remain.

    Args:
        df (pd.DataFrame): Original data.

    Returns:
        pd.DataFrame: Cleaned and ready-to-analyze data.
    """
    df = df.copy()

    # Convert to appropriate types
    bool_cols = ['uses_focus_apps', 'has_digital_wellbeing_enabled']
    df[bool_cols] = df[bool_cols].astype(bool)

    categorical_cols = ['gender', 'job_type', 'social_platform_preference']
    for col in categorical_cols:
        df[col] = df[col].astype('category')

    # Remove rows with critical nulls
    df.dropna(subset=['daily_social_media_time', 'actual_productivity_score'], inplace=True)

    # Fill specific optional null values
    df.fillna({
        'coffee_consumption_per_day': 0,
        'breaks_during_work': df['breaks_during_work'].median()
    }, inplace=True)

    # Fill remaining numeric nulls with median
    num_cols = df.select_dtypes(include='number').columns
    for col in num_cols:
        if df[col].isnull().any():
            df[col].fillna(df[col].median(), inplace=True)

    # Fill remaining categorical nulls with mode
    cat_cols = df.select_dtypes(include='category').columns
    for col in cat_cols:
        if df[col].isnull().any():
            df[col].fillna(df[col].mode()[0], inplace=True)



    return df

if __name__ == "__main__":
    path = "data/social_media_vs_productivity.csv"
    df_raw = load_csv(path)
    df_clean = clean_and_prepare(df_raw)

    print("✅ Data cleaned successfully")
    print(f"Final shape: {df_clean.shape}")
    print("Columns with remaining nulls:")
    print(df_clean.isnull().sum()[df_clean.isnull().sum() > 0])
