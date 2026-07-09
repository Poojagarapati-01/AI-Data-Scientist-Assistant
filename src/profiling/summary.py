import pandas as pd

def get_dataset_summary(df):
    """
    Generate a summary of the uploaded dataset.
    """

    summary = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "missing_values": df.isnull().sum().sum(),
        "duplicates": df.duplicated().sum(),
        "numerical_columns": len(df.select_dtypes(include=["number"]).columns),
        "categorical_columns": len(df.select_dtypes(include=["object", "category"]).columns),
        "memory_usage": f"{df.memory_usage(deep=True).sum() / 1024:.2f} KB"
    }

    return summary