import argparse
from pathlib import Path
import pdfplumber
import csv
from tqdm import tqdm
from typing import List, Optional


def extract_tables(pdf_path: Path, output_dir: Path) -> None:
    tables: List[Optional[List[List[str]]]] = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in tqdm(pdf.pages, desc="Extracting tables"):
            table: Optional[List[List[str]]] = page.extract_table()
            if table:
                tables.append(table)

    if tables:
        output_dir.mkdir(parents=True, exist_ok=True)
        for i, table in enumerate(tqdm(tables, desc="Saving tables")):
            output_file: Path = output_dir / f"extracted_table_{i}.csv"
            with open(output_file, "w", newline="") as csv_file:
                writer: csv.writer = csv.writer(csv_file)
                for row in table:
                    writer.writerow(row)


def main() -> None:
    # Set up argument parsing
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="Extract tables from a PDF and save them as CSV files."
    )
    parser.add_argument("pdf_path", type=Path, help="Path to the PDF file.")
    parser.add_argument(
        "output_dir", type=Path, help="Directory where CSV files will be saved."
    )

    args: argparse.Namespace = parser.parse_args()

    extract_tables(args.pdf_path, args.output_dir)


if __name__ == "__main__":
    main()
