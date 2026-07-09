"""
analyzer.py

This module analyzes the uploaded dataset and provides
basic insights for the AI Data Scientist Assistant.
"""

import pandas as pd


def detect_missing_values(df):
    """
    Returns a dictionary of columns that contain missing values.
    """

    missing = df.isnull().sum()
    missing = missing[missing > 0]

    return missing.to_dict()


def detect_duplicates(df):
    """
    Returns the number of duplicate rows.
    """

    return int(df.duplicated().sum())


def get_numerical_columns(df):
    """
    Returns a list of numerical columns.
    """

    return df.select_dtypes(include=["number"]).columns.tolist()


def get_categorical_columns(df):
    """
    Returns a list of categorical columns.
    """

    return df.select_dtypes(
        include=["object", "category", "string"]
    ).columns.tolist()


def detect_constant_columns(df):
    """
    Returns columns having only one unique value.
    """

    constant_columns = []

    for column in df.columns:

        if df[column].nunique() == 1:
            constant_columns.append(column)

    return constant_columns


def detect_high_cardinality(df, threshold=0.90):
    """
    Returns categorical columns having a high ratio
    of unique values.

    threshold = unique values / total rows
    """

    high_cardinality = []

    categorical_columns = get_categorical_columns(df)

    for column in categorical_columns:

        ratio = df[column].nunique() / len(df)

        if ratio >= threshold:
            high_cardinality.append(column)

    return high_cardinality