import pandas as pd
import os

def load_csv(filepath: str) -> pd.DataFrame:
    """
    Loads and validates the CSV file.

    Args:
        filepath (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data.
    """
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"File not found at: {filepath}")

    df = pd.read_csv(filepath)

    expected_columns = [
        'age', 'gender', 'job_type', 'daily_social_media_time', 'social_platform_preference',
        'number_of_notifications', 'work_hours_per_day', 'perceived_productivity_score',
        'actual_productivity_score', 'stress_level', 'sleep_hours', 'screen_time_before_sleep',
        'breaks_during_work', 'uses_focus_apps', 'has_digital_wellbeing_enabled',
        'coffee_consumption_per_day', 'days_feeling_burnout_per_month',
        'weekly_offline_hours', 'job_satisfaction_score'
    ]

    missing = [col for col in expected_columns if col not in df.columns]
    if missing:
        raise ValueError(f"Missing columns in the dataset: {missing}")

    return df

if __name__ == "__main__":
    path = "data/social_media_vs_productivity.csv"
    df = load_csv(path)
    print("✅ Dataset loaded successfully")
    print(f"Shape: {df.shape}")
    print("First rows:")
    print(df.head())