import csv
import os
from datetime import datetime

INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

for filename in os.listdir(INPUT_FOLDER):
    if not filename.endswith(".csv"):
        continue

    input_path = os.path.join(INPUT_FOLDER, filename)
    output_path = os.path.join(OUTPUT_FOLDER, filename)

    with open(input_path, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    new_lines = []
    prev_date = None

    for line in lines:
        date_str = line.split(",")[0].replace('"','')
        dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        if prev_date != dt.date():
            # Insert row before date change
            doy = dt.timetuple().tm_yday
            hhmm = dt.strftime("%H%M")
            hh = dt.strftime("%H")
            mm = dt.strftime("%M")
            new_lines.append(f',,1000,{dt.year},{doy},{hhmm},{hh},{mm}')
        new_lines.append(line)
        prev_date = dt.date()

    with open(output_path, "w", newline="") as f:
        f.write("\n".join(new_lines))