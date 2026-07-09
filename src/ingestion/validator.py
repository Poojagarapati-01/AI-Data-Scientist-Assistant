#for checking whether the uploaded file is valid.
"""
validator.py

This module validates uploaded dataset files before they are loaded.
"""

from pathlib import Path


def validate_file(uploaded_file):

    
    if uploaded_file is None:
        return False, "No file uploaded."

    file_extension = Path(uploaded_file.name).suffix.lower()

   
    if file_extension != ".csv":
        return False, "Only CSV files are supported."

    return True, "File is valid."