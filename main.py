import argparse

from analyzer import analyze_code
from export.exporter import export_to_json, export_to_csv
from log_config import setup_logging


def main():
    setup_logging()
    parser = argparse.ArgumentParser(description="Analyze Python code for code smells.")
    parser.add_argument('-i', '--input', type=str, required=True, help="Path of the Python file to analyze.")
    parser.add_argument('-o', '--output', choices=['json', 'csv'], required=True, help="Output format (json or csv).")
    args = parser.parse_args()

    metrics_data = analyze_code(args.input)

    output_file = args.input + '_metrics.' + args.output
    if args.output == 'json':
        export_to_json(metrics_data, output_file)
    elif args.output == 'csv':
        export_to_csv(metrics_data, output_file)


if __name__ == "__main__":
    main()
