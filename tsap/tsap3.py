import RPi.GPIO as GPIO

aux = 0 # Тут должны быть номера портов aux

GPIO.setmode(GPIO.BCM)
GPIO.setup(aux, GPIO.OUT)
p = GPIO.PWM(aux,1000)
p.start(0)

try:
    while True:
        inputStr = input("Enter a float number between 0 and 100('q' to exit)")
        if inputStr.isdigit():
            number = float(inputStr)
            if number > 100 :
                print("The number is too large")
                continue
            p.ChangeDutyCycle (number)
        elif inputStr == 'q':
            break
        else:
            print("Enter a positive float number")
            continue
finally:
    p.stop()
    GPIO.cleanup(aux)