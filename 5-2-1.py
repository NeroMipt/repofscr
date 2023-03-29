import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)


weight = [128, 64, 32, 16, 8, 4, 2, 1]
dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3
troykaModule = 17
comp = 4

GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(troykaModule, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)



def d2b(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

try:
    while True:
        sum = 0
        for value in range(8):
            signal = d2b(sum + weight[value])
            GPIO.output(dac, signal)
            time.sleep(0.01)
            if(GPIO.input(comp) == 1):
                sum += weight[value]
        sig = d2b(sum)
        voltage = sum / levels * maxVoltage
        print("{}, {}, {}".format(sum, sig, voltage))


  
    
    




    
finally:
    GPIO.output(22 , 0)
    GPIO.cleanup()

