# Smart Shaded Plant House using Machine Learning

This project presents an IoT-based smart agriculture system designed for **tomato cultivation**. It integrates sensors, NodeMCU (ESP8266), and a **Random Forest Machine Learning model** to automate irrigation, lighting, and shading.

The system monitors environmental conditions in real-time and makes intelligent decisions to maintain optimal plant growth.


## Project Structure
project.ino → Final Arduino code (ML communication)
dataset.ino → Data collection from sensors
data.py → Convert raw data into CSV format
model.py → Machine Learning model + Arduino integration
graph.py → Generate graphs for analysis


##  Features

-  Temperature & Humidity Monitoring (DHT11)
-  Smart Irrigation System (ML-based Pump Control)
-  Automatic LED Control (Low Light Conditions)
-  Smart Shading using Servo Motor
-  Machine Learning Predictions (Random Forest)
-  Data Visualization using Graphs
-  Real-time Arduino ↔ Python Communication


##  Machine Learning

### Models Used:
- **Random Forest Classifier**
  - Predicts: Pump ON / OFF

- **Random Forest Regressor**
  - Predicts: Future Temperature

### Input Features:
- Temperature  
- Humidity  
- Soil Moisture  
- Light Intensity  


## Hardware Used

- NodeMCU (ESP8266)
- DHT11 Sensor
- Servo Motor (Shading)
- LED (Lighting)
- Soil Moisture Sensor
- UV / Light Sensor


##  System Workflow
Sensors → Arduino → Python ML Model → Prediction → Actuators

##  How to Run

### Step 1: Data Collection
Upload the following code to NodeMCU:
dataset.ino
Collect sensor data.


### Step 2: Convert to CSV
Run:
```bash
python data.py
```


### Step 3: Run ML Model + Arduino Integration
Run:
```bash
python model.py
```


### Step 4: Run Final Arduino Control Code
Run:
```bash
project.ino
```

### Step 5: Generate Graphs
Run:
```bash
python graph.py
```

##  Results

- Irrigation Accuracy: ~85%  
- Temperature Prediction Error (MAE): ~0.04  

### Automated Control Achieved:
- Pump (Irrigation)  
- LED (Lighting)  
- Servo Motor (Shading)  
- Fan (Temperature Control)

## Authors

- Nancy Sakhiya  
- Tanushree Jatia  
- Sunita Choudhary  
- Sanju Rana  
