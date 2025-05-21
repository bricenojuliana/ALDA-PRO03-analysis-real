import pytest
import pandas as pd
from src.load_data import load_csv

def test_load_csv_success():
    df = load_csv("data/social_media_vs_productivity.csv")
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert "actual_productivity_score" in df.columns

def test_load_csv_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_csv("data/non_existent.csv")

def test_load_csv_missing_columns(tmp_path):
    # Crea un archivo CSV temporal con columnas incompletas
    file = tmp_path / "incomplete.csv"
    file.write_text("age,gender\n25,Male")

    with pytest.raises(ValueError):
        load_csv(str(file))
