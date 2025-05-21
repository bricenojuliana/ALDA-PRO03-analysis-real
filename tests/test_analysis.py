import pandas as pd
from src.analysis import get_descriptive_stats, compute_correlations, group_mean_by_category

def test_get_descriptive_stats():
    df = pd.DataFrame({
        "a": [1, 2, 3],
        "b": [4, 5, 6],
    })
    desc = get_descriptive_stats(df)
    assert "a" in desc.columns
    assert "b" in desc.columns

def test_compute_correlations():
    df = pd.DataFrame({
        "x": [1, 2, 3],
        "y": [2, 4, 6],
        "z": [3, 6, 9],
    })
    corrs = compute_correlations(df, target="z")
    assert "x" in corrs.index or "y" in corrs.index

def test_group_mean_by_category():
    df = pd.DataFrame({
        "cat": ["A", "B", "A", "B"],
        "val": [1, 2, 3, 4],
    })
    grouped = group_mean_by_category(df, "cat", "val")
    assert list(grouped.columns) == ["cat", "val"]
    assert grouped.shape == (2, 2)
