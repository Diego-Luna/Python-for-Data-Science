import os
from load_csv import load


def main():
    """Test the load function with valid and invalid CSV files."""
    # * Test loading valid dataset supporting paths
    path1 = "life_expectancy_years.csv"
    path2 = "../life_expectancy_years.csv"
    path3 = "Python-2-DataTable/life_expectancy_years.csv"
    sub_path = os.path.join(
        "Python-2-DataTable", "ex00", "life_expectancy_years.csv"
    )

    target_path = None
    for p in [path1, path2, path3, sub_path]:
        if os.path.exists(p):
            target_path = p
            break

    if not target_path and os.path.exists("../life_expectancy_years.csv"):
        target_path = "../life_expectancy_years.csv"
    elif not target_path and os.path.exists("life_expectancy_years.csv"):
        target_path = "life_expectancy_years.csv"

    if target_path:
        print(f"Testing with valid path: {target_path}")
        df = load(target_path)
        if df is not None:
            print(df.head(2))

    # ! Test error cases
    print("\n--- Testing Error Cases ---")
    print("Test non-existent file:")
    load("non_existent.csv")

    print("\nTest invalid path type (int):")
    load(12345)  # type: ignore

    print("\nTest invalid file extension:")
    load("test.txt")


if __name__ == "__main__":
    main()
