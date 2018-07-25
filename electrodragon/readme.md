## Readme

This directory contains micropython code to control an Electrodragon IoT board with mains rated relays and a built in ESP-8266.


#### Prerequisites

- Micropython has been installed on the ESP8266
- 'ampy' has been installed on the PC

#### Running the micropython scripts

To run the micropython scripts use ampy, e.g.

`ampy -p COM5 -b 115200 -d 1 run electrodragon-blink.py`

### electrodragon-blink.py

Turns on and off the two relays on the Electrodragon board.

### electrodragon-temperature.py

Each second, reads and output temperature and humidity using a DHT-11 sensor.

