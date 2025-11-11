# Version: 1.0
# Purpose: Pairwise comparison of % assignments from FeatureCounts in 3 panels.
# Feature: Calculates % from raw counts using Genetype Total alignments.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re

def extract_count(value):
    """Extracts integer from string like '37551633 (15.3%)'."""
    if pd.isna(value):
        return None
    match = re.search(r"(\d+)", str(value).replace(',', ''))
    return int(match.group(1)) if match else None

def plot_featurecount_comparison(tsv_file):
    df = pd.read_csv(tsv_file, sep='\t')

    # Extract numeric values
    df["Assigned FeatureCounts"] = df["Gene ID  Successfully assigned alignments"].apply(extract_count)
    df["Unassigned_NoFeatures"] = df["Unassigned_NoFeatures"].apply(lambda x: extract_count(x) if "Unassigned_NoFeatures" in df.columns else None)
    df["Unassigned_Ambiguity"] = df["Unassigned_Ambiguity"].apply(lambda x: extract_count(x) if "Unassigned_Ambiguity" in df.columns else None)
    df["Genetype Total alignments"] = df["Genetype Total alignments"].apply(extract_count)

    # Drop rows with missing values
    df = df.dropna(subset=["Processed status Simplified",
                           "Assigned FeatureCounts",
                           "Unassigned_NoFeatures",
                           "Unassigned_Ambiguity",
                           "Genetype Total alignments"])

    # Calculate %s
    df["% Assigned"] = df["Assigned FeatureCounts"] / df["Genetype Total alignments"] * 100
    df["% Unassigned_NoFeatures"] = df["Unassigned_NoFeatures"] / df["Genetype Total alignments"] * 100
    df["% Unassigned_Ambiguity"] = df["Unassigned_Ambiguity"] / df["Genetype Total alignments"] * 100

    # Custom color
    custom_palette = {
        "Processed": "tab:blue",
        "Stalled": "tab:orange"
    }

    # Create subplot
    fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharex=True)

    sns.stripplot(data=df, x="Processed status Simplified", y="% Assigned",
                  palette=custom_palette, jitter=True, size=8, ax=axes[0])
    axes[0].set_title("% Assigned")
    axes[0].set_ylabel("Percent")
    axes[0].set_xlabel("")

    sns.stripplot(data=df, x="Processed status Simplified", y="% Unassigned_NoFeatures",
                  palette=custom_palette, jitter=True, size=8, ax=axes[1])
    axes[1].set_title("% Unassigned: No Features")
    axes[1].set_ylabel("Percent")
    axes[1].set_xlabel("")

    sns.stripplot(data=df, x="Processed status Simplified", y="% Unassigned_Ambiguity",
                  palette=custom_palette, jitter=True, size=8, ax=axes[2])
    axes[2].set_title("% Unassigned: Ambiguity")
    axes[2].set_ylabel("Percent")
    axes[2].set_xlabel("Processed Status")

    plt.suptitle("FeatureCounts Assignment Breakdown by Sample Type", fontsize=14)
    sns.despine()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    input = "stalled_samples_featurecounts_summary.txt"
    plot_featurecount_comparison(input)
