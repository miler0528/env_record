this program operates like below 
- AE-BME280      get enviromental data(temperature, humidity, pressure)
- ESP32 devkitC get the data and send Serial Message via USB Serial
- Python program on PC get the Serial Messages and register them to SQL-DB using pandas