import pandas as pd
import os

def get_descriptive_stats(df: pd.DataFrame) -> pd.DataFrame:
    """
    Returns descriptive statistics of the numerical variables.
    """
    return df.describe()

def compute_correlations(df: pd.DataFrame, target: str = "actual_productivity_score") -> pd.Series:
    """
    Calculates correlations between the target and other numerical variables.
    """
    numeric_df = df.select_dtypes(include=['number'])
    corr_series = numeric_df.corr()[target].drop(labels=[target])
    return corr_series.sort_values(ascending=False)

def group_mean_by_category(df: pd.DataFrame, category: str, value: str) -> pd.DataFrame:
    """
    Groups by a categorical column and shows the mean of a numerical variable.
    """
    return df.groupby(category)[value].mean().sort_values(ascending=False).reset_index()


if __name__ == "__main__":
    # Ensure output folder
    os.makedirs("outputs", exist_ok=True)

    # Load dataset
    df = pd.read_csv("data/social_media_vs_productivity.csv")

    # Run analysis
    desc_stats = get_descriptive_stats(df)
    correlations = compute_correlations(df)
    grouped_means = group_mean_by_category(df, category="job_type", value="actual_productivity_score")

    # Save results to .txt file
    output_path = "outputs/analysis_summary.txt"
    with open(output_path, "w") as f:
        f.write("=== Descriptive statistics ===\n")
        f.write(desc_stats.to_string())
        f.write("\n\n=== Correlations with actual productivity (actual_productivity_score) ===\n")
        f.write(correlations.to_string())
        f.write("\n\n=== Average actual productivity by job type (job_type) ===\n")
        f.write(grouped_means.to_string(index=False))

    print(f"✅ Result saved in {output_path}")
