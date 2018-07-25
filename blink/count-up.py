# Toggles two relays and built-in LED
import utime

from machine import Pin
def main():

    print('Hello world! I can count to 100000')
    for i in range(1,100000):
        print(i)
        utime.sleep_ms(1000)

if __name__ == '__main__':
    main()
