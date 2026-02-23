import csv
from datetime import datetime
from pathlib import Path
import sys

def build_insert_row(timestamp_str):
    timestamp_str = timestamp_str.strip('"')
    dt = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
    return [
        "", "",
        "1000",
        dt.strftime("%Y"),
        dt.strftime("%j"),
        dt.strftime("%H%M"),
        dt.strftime("%H"),
        dt.strftime("%M"),
    ]


def process_file(input_path, output_path):
    previous_timestamp = None

    with open(input_path, newline="") as infile, open(output_path, "w", newline="") as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            if not row:
                continue

            current_timestamp = row[0]

            if previous_timestamp and current_timestamp != previous_timestamp:
                writer.writerow(build_insert_row(current_timestamp))

            writer.writerow(row)
            previous_timestamp = current_timestamp


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    process_file(input_file, output_file)