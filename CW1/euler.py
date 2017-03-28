#import numpy as np
from matplotlib import pyplot as plt
import math

t0 = 0
t1 = 3
dt = 0.1
f0 = 0

#n = int(((t1-t0)/dt) + 1)

#t = np.linspace(t0, t1, n)

#f = np.zeros([n])

ts = [t0]
fs = [f0]
while ts[-1]<t1:
    f = dt*(fs[-1]**2 - 3*fs[-1] + math.exp(-ts[-1])) + fs[-1]

    ts.append(ts[-1]+dt)
    fs.append(f)

plt.plot(ts, fs)
plt.xlabel("Value of f")
plt.ylabel("Value of t")
plt.title("Differential equation with Euler's method")
plt.show()