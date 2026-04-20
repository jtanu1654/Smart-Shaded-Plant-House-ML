#include <DHT.h>
#include <Servo.h>

#define DHTPIN D1
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);
Servo shade;

int ledPin = D5;

// Simulated values
int moisture = 700;
int light = 700;
int direction = -1;

void setup() {
  Serial.begin(115200);
  dht.begin();
  shade.attach(D4);
  pinMode(ledPin, OUTPUT);

  delay(2000);
}

void loop() {

  float temp = dht.readTemperature();
  float hum = dht.readHumidity();

  if (isnan(temp) || isnan(hum)) return;

  // ---- Simulate Data ----
  moisture -= random(1, 5);

  light += direction * random(5, 15);
  if (light < 200 || light > 800)
    direction = -direction;

  light = constrain(light, 200, 800);

  // 📤 SEND DATA TO PYTHON (CSV)
  Serial.print(temp); Serial.print(",");
  Serial.print(hum); Serial.print(",");
  Serial.print(moisture); Serial.print(",");
  Serial.println(light);

  delay(1000);

  // 📥 RECEIVE ML COMMAND
  if (Serial.available()) {
    String cmd = Serial.readStringUntil('\n');

    if (cmd == "PUMP_ON") {
      Serial.println("Pump ON (ML)");
    } 
    else if (cmd == "PUMP_OFF") {
      Serial.println("Pump OFF (ML)");
    }

    if (cmd == "LED_ON") {
      digitalWrite(ledPin, HIGH);
    } 
    else if (cmd == "LED_OFF") {
      digitalWrite(ledPin, LOW);
    }

    if (cmd == "SHADE_CLOSE") {
      shade.write(90);
    } 
    else if (cmd == "SHADE_OPEN") {
      shade.write(0);
    }
  }

  delay(2000);
}

