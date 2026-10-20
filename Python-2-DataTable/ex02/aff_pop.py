import os
import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def parse_pop(val: str | float | int) -> float:
    """Parse population string with suffix (k, M, B) into a float."""
    # ! Handle missing or already numeric values
    if pd.isna(val):
        return 0.0
    if isinstance(val, (int, float)):
        return float(val)

    val_str = str(val).strip().upper()
    multiplier = 1.0

    # * Check for standard population suffixes
    if val_str.endswith('K'):
        multiplier = 1e3
        val_str = val_str[:-1]
    elif val_str.endswith('M'):
        multiplier = 1e6
        val_str = val_str[:-1]
    elif val_str.endswith('B'):
        multiplier = 1e9
        val_str = val_str[:-1]

    try:
        return float(val_str) * multiplier
    except ValueError:
        # ? Fallback for invalid formatting
        return 0.0


def main():
    """Load population data, filter France, Belgium, and plot."""
    # * Find dataset path robustly
    path = "population_total.csv"
    if not os.path.exists(path):
        path = os.path.join(
            os.path.dirname(__file__), "..", "population_total.csv"
        )

    # * Load the population dataset
    df = load(path)
    if df is None:
        print("Error: Could not load population dataset.")
        return

    # * Ensure 'country' column exists
    if 'country' not in df.columns:
        print("Error: 'country' column not found in dataset.")
        return

    # * Filter for France and Belgium
    countries = ['France', 'Belgium']
    df_filtered = df[df['country'].isin(countries)]
    if df_filtered.empty:
        print("Error: France or Belgium not found in dataset.")
        return

    # * Extract years available in columns (excluding 'country')
    year_cols = [c for c in df.columns if c != 'country']
    years_int = []
    for col in year_cols:
        try:
            years_int.append(int(col))
        except ValueError:
            continue

    # * Filter years between 1800 and 2050 inclusive
    valid_years = [y for y in years_int if 1800 <= y <= 2050]
    valid_year_cols = [str(y) for y in valid_years]

    for country in countries:
        c_row = df_filtered[df_filtered['country'] == country]
        if c_row.empty:
            continue

        pop_values = []
        for y_col in valid_year_cols:
            val = c_row[y_col].values[0]
            pop_values.append(parse_pop(val))

        # * Assign colors: Belgium (tab:blue), France (tab:green)
        color = 'tab:blue' if country == 'Belgium' else 'tab:green'
        plt.plot(valid_years, pop_values, label=country,
                 color=color, linewidth=2)

    # * Configure plot appearance
    plt.title('Population Projections')
    plt.xlabel('Year')
    plt.xticks(range(1800, 2051, 40))

    plt.ylabel('Population')
    plt.yticks([20e6, 40e6, 60e6], ['20M', '40M', '60M'])

    plt.legend(loc='lower right')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
