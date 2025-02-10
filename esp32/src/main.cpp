#include <Wire.h>
#include <Adafruit_BME280.h>

Adafruit_BME280 bme;

void setup() {
  Serial.begin(115200);
  Wire.begin();
  if (!bme.begin(0x76)) {
    Serial.println("センサが見つかりません");
    while (1);
  }
}

void loop() {
  // センサーからデータを読み込む
  float temperature = bme.readTemperature();
  float pressure = bme.readPressure() / 100.0F;
  float humidity = bme.readHumidity();

  // 表示
  String message = "{";
  message += "\"temperature\":";
  message += String(temperature, 1);
  message += ",";
  // Serial.print("Temperature: ");
  // Serial.print(temperature);
  // Serial.println(" degrees C");

  message += "\"pressure\":";
  message += String(pressure, 1);
  message += ",";
  // Serial.print("Pressure: ");
  // Serial.print(pressure);
  // Serial.println(" hPa");

  message += "\"humidity\":";
  message += String(humidity, 1);
  // message += ",";
  // Serial.print("Humidity: ");
  // Serial.print(humidity);
  // Serial.println(" %");
  
  message += "}";

  Serial.println(message);

  delay(60000);
}
