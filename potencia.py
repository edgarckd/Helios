from locale import currency
from typing import Concatenate
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


voltage = np.linspace(0,35,350)
#print(len(current))
current = np.concatenate((11*np.ones(10*30), np.zeros(10*5)) )
potencia = 11*voltage*current / max(voltage*current)
potencia_del_resistor = current**2 * 0.005
plt.plot(voltage, potencia_del_resistor)
plt.plot(voltage, potencia)
plt.plot(voltage,current)
plt.xlabel('Voltage v')
plt.ylabel('Current I')
plt.savefig('save.jpeg')