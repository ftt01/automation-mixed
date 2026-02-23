import csv
from datetime import datetime

INPUT_FILE = "input.csv"
OUTPUT_FILE = "output.csv"


def build_insert_row(timestamp_str):
    # Remove quotes if present
    timestamp_str = timestamp_str.strip('"')

    dt = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")

    year = dt.strftime("%Y")
    doy = dt.strftime("%j")      # Day of year (001–366)
    hhmm = dt.strftime("%H%M")
    hour = dt.strftime("%H")
    minute = dt.strftime("%M")

    return ["", "", "1000", year, doy, hhmm, hour, minute]


with open(INPUT_FILE, newline="") as infile, \
     open(OUTPUT_FILE, "w", newline="") as outfile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    previous_timestamp = None

    for row in reader:
        if not row:
            continue

        current_timestamp = row[0]

        if previous_timestamp is not None and current_timestamp != previous_timestamp:
            insert_row = build_insert_row(current_timestamp)
            writer.writerow(insert_row)

        writer.writerow(row)
        previous_timestamp = current_timestamp
