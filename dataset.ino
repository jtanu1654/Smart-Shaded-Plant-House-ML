#include <DHT.h>
#include <Servo.h>

#define DHTPIN D1
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);
Servo shade;

// Actuator pins
int ledPin = D5;   // LED moved to D5

// Simulated variables
int moisture = 700;
int light = 700;
int direction = -1;

void setup() {
  Serial.begin(115200);
  dht.begin();

  shade.attach(D4);   // SERVO on D6
  pinMode(ledPin, OUTPUT);

  randomSeed(analogRead(0));
}

void loop() {

  // ---- Real Sensor ----
  float temp = dht.readTemperature();
  float hum = dht.readHumidity();

  // ---- Simulate Soil Moisture ----
  moisture -= random(1, 5);

  // ---- Simulate Light (Day-Night Cycle) ----
  light += direction * random(5, 15);
  if (light < 200 || light > 800) {
    direction = -direction;
  }
  light = constrain(light, 200, 800);

  // ---- Irrigation (SIMULATED) ----
  if (moisture < 500) {
    Serial.println("Action: Pump ON (Simulated)");
    moisture += random(20, 40);
  } else {
    Serial.println("Action: Pump OFF");
  }

  // ---- Temperature Control (SIMULATED FAN) ----
  if (temp > 30) {
    Serial.println("Action: Fan ON (Simulated)");
  } else {
    Serial.println("Action: Fan OFF");
  }

  // ---- Shading Control (SERVO REAL) ----
  if (light > 600) {
    shade.write(90);
    Serial.println("Action: Shade CLOSED (Servo)");
  } else {
    shade.write(0);
    Serial.println("Action: Shade OPEN (Servo)");
  }

  // ---- LED Control (REAL) ----
  if (light < 300) {
    digitalWrite(ledPin, HIGH);
    Serial.println("Action: LED ON");
  } else {
    digitalWrite(ledPin, LOW);
    Serial.println("Action: LED OFF");
  }

  // ---- Display Values ----
  Serial.println("Temp,Humidity,Moisture,Light");
  Serial.print(temp); Serial.print(",");
  Serial.print(hum); Serial.print(",");
  Serial.print(moisture); Serial.print(",");
  Serial.println(light);

  delay(2000);
}