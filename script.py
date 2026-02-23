import csv
from datetime import datetime
from pathlib import Path


INPUT_DIR = Path("input")
OUTPUT_DIR = Path("output")

OUTPUT_DIR.mkdir(exist_ok=True)


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


for input_file in INPUT_DIR.glob("*.csv"):
    output_file = OUTPUT_DIR / input_file.name

    previous_timestamp = None

    with input_file.open(newline="") as infile, \
         output_file.open("w", newline="") as outfile:

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
