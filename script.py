import csv
from datetime import datetime
from pathlib import Path

def build_insert_row(timestamp_str):
    timestamp_str = timestamp_str.strip('"')
    dt = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
    return [
        "", "",
        "1000",
        dt.strftime("%Y"),   # A = year
        dt.strftime("%j"),   # B = DOY
        dt.strftime("%H%M"), # C = HHmm
        dt.strftime("%H"),   # D = HH
        dt.strftime("%M"),   # E = mm
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

def main():
    input_dir = Path("input")
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    for file_path in input_dir.glob("*.csv"):
        output_file = output_dir / file_path.name
        print(f"Processing {file_path} → {output_file}")
        process_file(file_path, output_file)

if __name__ == "__main__":
    main()