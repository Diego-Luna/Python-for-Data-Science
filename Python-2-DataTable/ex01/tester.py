import os
from load_csv import load


def main() -> None:
    """Test data loading, France row existence, and column count."""
    # * Test loading dataset
    path = "life_expectancy_years.csv"
    if not os.path.exists(path):
        path = os.path.join(
            os.path.dirname(__file__), "..", "life_expectancy_years.csv"
        )

    df = load(path)
    assert df is not None, "Dataset failed to load."
    print("Dataset loaded successfully.")

    # * Verify France row existence
    france_row = df[df['country'] == 'France']
    assert not france_row.empty, "France row not found."
    print("France row found successfully.")

    # * Verify 301 year columns (1800 to 2100 inclusive)
    years = [
        col for col in df.columns
        if col.isdigit() and 1800 <= int(col) <= 2100
    ]
    print(f"Number of year columns found: {len(years)}")
    assert len(years) == 301, f"Expected 301 year columns, found {len(years)}"
    print("All tests passed successfully!")


if __name__ == "__main__":
    main()
