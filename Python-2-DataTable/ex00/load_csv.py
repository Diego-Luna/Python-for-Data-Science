import os
import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """Load a CSV file into a pandas DataFrame and return it."""
    # ! Validate path type and existence
    if not isinstance(path, str):
        print("Error: path must be a string")
        return None
    if not os.path.exists(path):
        print(f"Error: file '{path}' does not exist")
        return None
    if not path.lower().endswith('.csv'):
        print(f"Error: file '{path}' is not a CSV file")
        return None

    try:
        # * Load the dataset using pandas
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except Exception as e:
        print(f"Error: {e}")
        return None
