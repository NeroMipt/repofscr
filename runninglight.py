import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [21, 20, 16, 12, 7, 8, 25, 24]
aux = [22, 23, 27, 18, 15, 14, 3, 2]

for pin in leds:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin , 1)
for pin in aux:
    GPIO.setup(pin, GPIO.IN)
while True:
    for pin in range(8):
        GPIO.output(leds[pin], GPIO.input(aux[pin]))

GPIO.cleanup()



