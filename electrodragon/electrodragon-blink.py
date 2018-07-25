# Toggles two relays and built-in LED
import utime

from machine import Pin
def main():
    relay1 = Pin(12, Pin.OUT)
    relay2 = Pin(13, Pin.OUT)
    led1 = Pin(16, Pin.OUT)
    enabled = False
    while True:
        if enabled:
            relay1.off()
            utime.sleep_ms(100)
            relay2.on()
            led1.on()
            print('off')
        else:
            relay1.on()
            utime.sleep_ms(100)
            relay2.off()
            led1.off()
            print('on')
        utime.sleep_ms(1000)
        enabled = not enabled

if __name__ == '__main__':
    main()
