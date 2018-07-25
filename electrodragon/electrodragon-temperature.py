# Each measure temperature and humidity, and outputs onto serial port
# To see output, run the program, e.g.
# ampy -b 115200 -p COM5 -d 1 run electrodragon-temerature.py
#
# The Ctrl+C to exit program
#
# Open 
import utime
import machine
import dht

from machine import Pin
def main():
    led1 = Pin(16, Pin.OUT)
    d = dht.DHT11(machine.Pin(14))
    enabled = False
    while True:
        if enabled:
            led1.on()
            d.measure()
            print(d.temperature())
            print(d.humidity())
        else:
            led1.off()
        utime.sleep_ms(1000)
        enabled = not enabled

if __name__ == '__main__':
    main()
