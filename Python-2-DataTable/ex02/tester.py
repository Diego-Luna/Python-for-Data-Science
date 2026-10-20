import os
from aff_pop import parse_pop
from load_csv import load


def test_parse_pop():
    """Unit tests for parse_pop function."""
    print("Running parse_pop unit tests...")
    test_cases = [
        ('29M', 29000000.0),
        ('500k', 500000.0),
        ('1.5B', 1500000000.0),
        ('42', 42.0),
        (100, 100.0),
        (None, 0.0)
    ]
    for val, expected in test_cases:
        result = parse_pop(val)
        assert result == expected, (
            f"Failed for {val}: got {result}, expected {expected}"
        )
    print("All parse_pop tests passed successfully!")


def test_data_filtering():
    """Test data loading and country filtering for France and Belgium."""
    print("Testing data loading and filtering...")
    path = "population_total.csv"
    if not os.path.exists(path):
        path = os.path.join(
            os.path.dirname(__file__), "..", "population_total.csv"
        )

    df = load(path)
    assert df is not None, "Failed to load population_total.csv"

    countries = ['France', 'Belgium']
    df_filtered = df[df['country'].isin(countries)]
    assert len(df_filtered) == 2, f"Expected 2 rows, got {len(df_filtered)}"

    found_countries = df_filtered['country'].tolist()
    for c in countries:
        assert c in found_countries, f"Country {c} not found in filtered data"
    print("Data loading and filtering tests passed successfully!")


def main():
    """Run all tests for exercise 02."""
    test_parse_pop()
    test_data_filtering()
    print("All tests passed successfully!")


if __name__ == "__main__":
    main()
