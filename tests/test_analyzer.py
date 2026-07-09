import pandas as pd

from src.profiling.analyzer import (
    detect_missing_values,
    detect_duplicates,
    get_numerical_columns,
    get_categorical_columns,
    detect_constant_columns,
    detect_high_cardinality,
)

df = pd.DataFrame(
    {
        "Age": [20, None, 25, 20],
        "Salary": [50000, 60000, None, 50000],
        "City": ["Delhi", "Mumbai", "Delhi", "Delhi"],
        "Country": ["India", "India", "India", "India"],
        "Employee_ID": ["E001", "E002", "E003", "E004"],
    }
)


def test_missing_values():
    assert detect_missing_values(df) == {"Age": 1, "Salary": 1}


def test_duplicates():
    assert detect_duplicates(df) == 0


def test_numerical_columns():
    assert get_numerical_columns(df) == ["Age", "Salary"]


def test_categorical_columns():
    assert get_categorical_columns(df) == [
        "City",
        "Country",
        "Employee_ID",
    ]


def test_constant_columns():
    assert detect_constant_columns(df) == ["Country"]


def test_high_cardinality():
    assert detect_high_cardinality(df) == ["Employee_ID"]