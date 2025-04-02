#!/usr/bin/env python3
import csv
import os
import logging
import argparse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

EXPECTED_HEADERS = [
    'symbol',
    'price',
    'price_change',
    'price_percent_change'
]

def validate_headers(headers):
    for expected_header in EXPECTED_HEADERS:
        assert expected_header in headers, f"Missing header: {expected_header}"
    return True

def normalize_csv(input_file):
    assert isinstance(input_file, str)
    assert os.path.exists(input_file)

    base_name, extension = os.path.splitext(input_file)
    output_file = f"{base_name}_norm{extension}"

    normalized_rows = []
    with open(input_file, newline='', encoding='utf-8') as csv_in:
        reader = csv.DictReader(csv_in)
        headers = reader.fieldnames
        logger.info(f"Found headers: {headers}")
        validate_headers(headers)
        for row in reader:
            normalized_row = { key: row[key].strip() for key in EXPECTED_HEADERS }
            normalized_rows.append(normalized_row)

    with open(output_file, 'w', newline='', encoding='utf-8') as csv_out:
        writer = csv.DictWriter(csv_out, fieldnames=EXPECTED_HEADERS)
        writer.writeheader()
        writer.writerows(normalized_rows)

    assert os.path.exists(output_file)
    logger.info(f"Normalized CSV created: {output_file}")
    return output_file

def main():
    parser = argparse.ArgumentParser(description="Normalize a raw CSV file of stock data")
    parser.add_argument("input_file", help="Path to the raw CSV file")
    args = parser.parse_args()
    
    logger.info(f"Starting normalization for {args.input_file}")
    output_file = normalize_csv(args.input_file)
    logger.info(f"Normalization complete. Output file: {output_file}")

if __name__ == '__main__':
    main()
