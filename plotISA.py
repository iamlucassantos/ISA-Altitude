from functionISA import calculator
from math import sqrt

altitude = []
temperature = []
density = []
pressure = []
speedSound =[]

for i in range(0,50000,50):
    altitude.append(i)
    t,p,rho = calculator(i)
    temperature.append(t)
    pressure.append(p)
    density.append(rho)
    speedSound.append(sqrt(t*1.4*287))

print(speedSound)