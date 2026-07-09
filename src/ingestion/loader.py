##for reading datasets
import pandas as pd
def load_csv(uploaded_file):
    try:
        df = pd.read_csv(uploaded_file)
        return df
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return None