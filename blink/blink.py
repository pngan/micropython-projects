import utime

from machine import Pin
def main():
    led = Pin(2, Pin.OUT)
    led2 = Pin(16, Pin.OUT)
    enabled = False
    while True:
        if enabled:
            led.off()
            led2.on()
            print('off')
        else:
            led.on()
            led2.off()
            print('on')
        utime.sleep_ms(1000)
        enabled = not enabled

if __name__ == '__main__':
    main()
