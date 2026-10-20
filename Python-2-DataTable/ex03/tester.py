import os
import pandas as pd
from load_csv import load


def main():
    """Test loading both datasets and merging for year 1900."""
    # * Load datasets
    income_path = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    if not os.path.exists(income_path):
        income_path = os.path.join(
            os.path.dirname(__file__), "..",
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        )

    life_path = "life_expectancy_years.csv"
    if not os.path.exists(life_path):
        life_path = os.path.join(
            os.path.dirname(__file__), "..", "life_expectancy_years.csv"
        )

    income_df = load(income_path)
    life_df = load(life_path)

    # ! Check if datasets loaded successfully
    if income_df is None or life_df is None:
        print("Test failed: Could not load datasets.")
        return

    # * Extract 'country' and '1900' columns
    income_1900 = income_df[['country', '1900']].copy()
    income_1900.rename(columns={'1900': 'gdp'}, inplace=True)

    life_1900 = life_df[['country', '1900']].copy()
    life_1900.rename(columns={'1900': 'life_expectancy'}, inplace=True)

    # * Merge on 'country' and drop NaNs
    merged_df = pd.merge(income_1900, life_1900, on='country')
    merged_df.dropna(inplace=True)

    print(f"Merged dataset shape for 1900: {merged_df.shape}")

    # * Verify merged length > 100
    assert len(merged_df) > 100, "Merged length is not greater than 100"
    print("Test passed: Merged length is greater than 100.")
    print("All tests passed successfully!")


if __name__ == "__main__":
    main()
