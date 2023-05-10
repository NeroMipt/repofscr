
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator)
levels = 2**8
maxVoltage = 3.3


with open("settings.txt", "r") as settings:
    tmp = [float(i) for i in settings.read().split("\n")]

data_array = np.loadtxt("data.txt", dtype=int)

data_array = data_array / levels * maxVoltage

t = np.arange(0, 898)
t = t * 0.011
fig, ax = plt.subplots(figsize=(8, 5), dpi=400)

ax.set_title('Процесс заряда и разряда конденсатора в RC-цепочке')
ax.set_xlabel('Время, с')
ax.set_ylabel('Напряжение, В')
ax.axis([0, 10, 0, 3.3])


ax.xaxis.set_minor_locator(MultipleLocator(0.5))
ax.yaxis.set_minor_locator(MultipleLocator(0.5))
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(1))
ax.plot(t, data_array, marker='o', markevery = 150, label='V(t)', color='orange', linewidth=1, linestyle='-')
ax.text(6, 2.3, r'Время заряда = 4,21 с')
ax.text(6, 1.3, r'Время разряда = 5,65 с')
ax.legend()
ax.grid(True, which='minor', linewidth=1)
ax.grid(True, which='major', linewidth=2)
fig.savefig("test.png")
plt.show()