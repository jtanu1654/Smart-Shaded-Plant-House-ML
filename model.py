import serial
import pandas as pd
import csv
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

# ======================
# LOAD DATA
# ======================
data = pd.read_csv("data.csv")

X = data[['Temp','Humidity','Moisture','Light']]
y_irrigation = data['Pump']
y_temp = data['NextTemp']

# ======================
# TRAIN MODELS
# ======================
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X, y_irrigation)

reg = RandomForestRegressor(n_estimators=100, random_state=42)
reg.fit(X, y_temp)

print("✅ ML Model Ready")

# ======================
# CREATE CSV FILE FOR SAVING
# ======================
file = open("predictions.csv", "w", newline="")
writer = csv.writer(file)

writer.writerow(["Temp","Humidity","Moisture","Light","Pump","PredictedTemp"])

# ======================
# SERIAL CONNECTION
# ======================
ser = serial.Serial('COM5', 115200)   # change if needed

# ======================
# LIVE LOOP
# ======================
while True:
    try:
        line = ser.readline().decode().strip()

        # Skip invalid lines
        if not line or "," not in line:
            continue

        values = list(map(float, line.split(',')))

        sample = pd.DataFrame([values],
                              columns=['Temp','Humidity','Moisture','Light'])

        # 🔮 Predictions
        pump = clf.predict(sample)[0]
        temp_pred = reg.predict(sample)[0]

        print("\nData:", values)
        print("Predicted Temp:", round(temp_pred, 2))

        # 💧 Pump
        if pump == 1:
            ser.write(b'PUMP_ON\n')
            print("Pump ON")
        else:
            ser.write(b'PUMP_OFF\n')
            print("Pump OFF")

        # 💡 LED
        if values[3] < 300:
            ser.write(b'LED_ON\n')
        else:
            ser.write(b'LED_OFF\n')

        # 🌤️ Shade
        if values[3] > 600:
            ser.write(b'SHADE_CLOSE\n')
        else:
            ser.write(b'SHADE_OPEN\n')

        # ======================
        # SAVE TO CSV 🔥
        # ======================
        writer.writerow([
            values[0], values[1], values[2], values[3],
            pump, round(temp_pred, 2)
        ])
        file.flush()

    except Exception as e:
        print("Error:", e)