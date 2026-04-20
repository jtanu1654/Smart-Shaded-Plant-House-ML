import csv

input_file = "raw.txt"
output_file = "data.csv"

data_rows = []
pump = 0

with open(input_file, "r") as file:
    lines = file.readlines()

# =========================
# EXTRACT DATA
# =========================
for i in range(len(lines)):
    line = lines[i].strip()

    if "Pump ON" in line:
        pump = 1
    elif "Pump OFF" in line:
        pump = 0

    if line.startswith("Temp,Humidity"):
        values = lines[i+1].strip()
        parts = values.split(",")

        if len(parts) == 4:
            temp, hum, moisture, light = parts
            data_rows.append([float(temp), float(hum), int(moisture), int(light), pump])

# =========================
# ADD NextTemp COLUMN
# =========================
final_rows = []

for i in range(len(data_rows) - 1):
    current = data_rows[i]
    next_temp = data_rows[i+1][0]   # next row temp

    final_rows.append([
        current[0],  # Temp
        current[1],  # Humidity
        current[2],  # Moisture
        current[3],  # Light
        current[4],  # Pump
        next_temp    # NextTemp
    ])

# =========================
# WRITE CSV
# =========================
with open(output_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Temp","Humidity","Moisture","Light","Pump","NextTemp"])
    writer.writerows(final_rows)

print("CSV with NextTemp created successfully!")