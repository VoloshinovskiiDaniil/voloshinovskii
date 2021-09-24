import RPi.GPIO as GPIO
import time

dac = [26,19,13,6,5,11,9,10]
bits = len(dac)
levels = 2**bits

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT,initial = GPIO.LOW)

def decimal2binary(decimal):
    return[int(bit) for bit in bin(decimal)[2:]zfill(bits)]
def bin2dac(number):
    signal = decimal2binary(number)
    GPIO.OUTPUT(dac,signal)
    return signal

try:
    while True:
        for i in range (256):
            signal = bin2dac(number)
            time.sleep (0.2)
            number = number + 1
        for i in range (256):
            signal = bin2dac(number)
            time.sleep (0.2)
            number = number - 1

finally:
    GPIO.OUTPUT(dac, GPIO.LOW)
    GPIO.cleanup(dac)
            
