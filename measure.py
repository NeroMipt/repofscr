import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt
GPIO.setmode(GPIO.BCM)
times = []
emptylist = []
leds = [21, 20, 16, 12, 7, 8, 25, 24]
weight = [128, 64, 32, 16, 8, 4, 2, 1]
dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3
troykaModule = 17
comp = 4

GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(troykaModule, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(leds, GPIO.OUT, initial=GPIO.LOW)


def d2b(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def cmp():
        sum = 0
        for value in range(8):
            signal = d2b(sum + weight[value])
            GPIO.output(dac, signal)
            time.sleep(0.01)
            if(GPIO.input(comp) == 1):
                sum += weight[value]
        return sum

try:
    while True:
        GPIO.output(troykaModule, 0)
        time.sleep(5)
        voltage = 0
        th = time.time()
        GPIO.output(troykaModule, 1)
        while voltage < 3.1:
            res = cmp()
            voltage = res / levels * maxVoltage
            emptylist.append(res)
            times.append(time.time() - th)
            print("{}, {}".format(res, voltage))
            sig = d2b(res)
            GPIO.output(leds, sig)
        tl = time.time()

        te = time.time()
        print("length:{}".format(th - te))
        print((th - te)/len(emptylist))
        plt.plot(times, emptylist)
        plt.show()
        meadata = [str(item) for item in emptylist]
        with open("data.txt", "w") as outfile:
            outfile.write("\n".join(meadata))





    


  
    
    




    
finally:
    GPIO.output(22 , 0)
    GPIO.cleanup()

