import os
import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def main():
    """Load income and life expectancy datasets, merge for 1900, and plot."""
    # * Load datasets using load_csv
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

    if income_df is None or life_df is None:
        print("Error: Failed to load one or both datasets.")
        return

    # ! Extract country and 1900 columns, renaming for clarity
    try:
        income_1900 = income_df[['country', '1900']].copy()
        income_1900.rename(columns={'1900': 'gdp'}, inplace=True)

        life_1900 = life_df[['country', '1900']].copy()
        life_1900.rename(
            columns={'1900': 'life_expectancy'},
            inplace=True
        )

        # * Merge datasets on 'country' and drop NaN values
        merged_df = pd.merge(income_1900, life_1900, on='country')
        merged_df.dropna(inplace=True)

        # * Convert gdp and life_expectancy to numeric, coercing errors
        merged_df['gdp'] = pd.to_numeric(
            merged_df['gdp'],
            errors='coerce'
        )
        merged_df['life_expectancy'] = pd.to_numeric(
            merged_df['life_expectancy'],
            errors='coerce'
        )
        merged_df.dropna(inplace=True)

    except Exception as e:
        print(f"Error processing data: {e}")
        return

    # * Create scatter plot
    plt.scatter(
        merged_df['gdp'],
        merged_df['life_expectancy'],
        alpha=0.7,
        edgecolor='k'
    )

    # * Set title and labels according to instructions
    plt.title('1900')
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life Expectancy')

    # * Configure log scale and ticks for X and Y axes
    plt.xscale('log')
    plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
    plt.yticks(range(20, 60, 5))

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
