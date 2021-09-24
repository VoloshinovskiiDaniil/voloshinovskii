import RPi.GPIO as GPIO

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
        inputStr = input("Enter a number between 0 and 255 ('q' to exit)")
        if inputStr isdigit():
            number = int(inputStr)
            if number > levels:
                print("The number is too large")
                continue
            signal = bin2dac(number)

        elif inputStr == 'q':
            break
        else:
            print("Enter a positive integer number")
            continue
finally:
    GPIO.OUTPUT(dac, GPIO.LOW)
    GPIO.cleanup(dac)
            
            


	

