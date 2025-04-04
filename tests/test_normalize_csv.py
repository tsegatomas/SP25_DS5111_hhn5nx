import sys
import os

# Add the repository root to sys.path so that the 'bin' package can be found.
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if repo_root not in sys.path:
    sys.path.insert(0, repo_root)

from bin.normalize_csv import normalize_csv

def test_normalize_csv_output_file_exists():
    # Provide a sample CSV file for testing.
    input_file = "sample_data/ygainers.csv"
    output_file = normalize_csv(input_file)
    assert os.path.exists(output_file), "Normalized output file was not created"

def test_normalize_csv_contains_expected_headers():
    input_file = "sample_data/ygainers.csv"
    output_file = normalize_csv(input_file)
    with open(output_file, 'r', encoding='utf-8') as f:
        content = f.read()
    for header in ["symbol", "price", "price_change", "price_percent_change"]:
        assert header in content, f"Header '{header}' not found in normalized CSV"
