import os
import matplotlib.pyplot as plt
from load_csv import load


def main() -> None:
    """Load life expectancy data, filter France, and plot projections."""
    # * Find dataset path
    path = "life_expectancy_years.csv"
    if not os.path.exists(path):
        path = os.path.join(
            os.path.dirname(__file__), "..", "life_expectancy_years.csv"
        )

    df = load(path)
    if df is None:
        print("Error: Could not load life_expectancy_years.csv")
        return

    # * Filter for France country data
    france_row = df[df['country'] == 'France']
    if france_row.empty:
        print("Error: Country 'France' not found in dataset.")
        return

    # * Extract years and life expectancy values
    years = [
        int(col) for col in df.columns
        if col.isdigit() and 1800 <= int(col) <= 2100
    ]
    years_str = [str(y) for y in years]
    life_expectancy = france_row[years_str].values[0]

    # * Plot data
    plt.plot(years, life_expectancy)
    plt.title('France Life expectancy Projections')
    plt.xlabel('Year')
    plt.ylabel('Life expectancy')
    plt.xticks(range(1800, 2100, 40))
    plt.yticks(range(30, 100, 10))
    plt.show()


if __name__ == "__main__":
    main()
