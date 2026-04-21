import pandas as pd
import matplotlib.pyplot as plt

# LOAD DATA
data = pd.read_csv("predictions.csv")

# GRAPH 1: BAR GRAPH (Pump Count)
plt.figure()

pump_counts = data['Pump'].value_counts()

plt.bar(pump_counts.index.astype(str), pump_counts.values)
plt.xlabel("Pump (0=OFF, 1=ON)")
plt.ylabel("Count")
plt.title("Pump ON vs OFF Count")

# GRAPH 2: LINE GRAPH (Temperature Trend) 
plt.figure()

plt.plot(data['PredictedTemp'])
plt.xlabel("Time")
plt.ylabel("Predicted Temperature")
plt.title("Temperature Prediction Over Time")

# GRAPH 3: LINE GRAPH (Moisture Trend)
plt.figure()

plt.plot(data['Moisture'])
plt.xlabel("Time")
plt.ylabel("Moisture")
plt.title("Moisture Variation Over Time")

# GRAPH 4: LINE GRAPH (Light Trend)
plt.figure()

plt.plot(data['Light'])
plt.xlabel("Time")
plt.ylabel("Light")
plt.title("Light Variation Over Time")

# SHOW ALL GRAPHS
plt.show()
