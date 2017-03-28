#This code is for questions 1-4
#Just run it once and the graphs will
# appear in order

import matplotlib.pyplot as plt
import math

# functions

def dv(v0, ie):
    return (el - v0 + rm * ie)/tau_m

# variables

tau_m = 10  # membrane time constant in ms
el = -70    # leak potential
vr = -70    # reset voltage
vt = -40    # threshold
rm = 10     # membrane resistance
ie = 3.1
dt = 1      # timestep in ms
t = 1000    # total time in ms
t0 = 0

# main program
# Q2.1 simulate integrate & fire model, plot the voltage as function of time
ts = [t0]
v = [vr]

while ts[-1] < t:
    #vs = v[-1] + dv2(tau_m, el, v[-1], rm, ie, dt) * dt
    vs = v[-1] + dv(v[-1], ie) * dt

    if vs > vt:
        vs = vr

    ts.append(ts[-1] + dt)
    v.append(vs)

plt.plot(ts, v)
plt.xlabel("Time (ms)")
plt.ylabel("Voltage (mV)")
plt.title("1. Integrate & fire model simulation")
plt.show()

# Q2.2 compute analytically the minimum current ie to produce action potential
ie3 = (vt - el) / rm
print("Minimum current Ie to produce action potential: ", ie3)

# Q2.3 Simulate the neuron with ie 0.1 lower than ie3
ie4 = ie3 - 0.1
#print(ie4)

ts2 = [t0]
v2 = [vr]

while ts2[-1] < t:
    vs2 = v2[-1] + dv(v2[-1], ie4) * dt

    if vs2 > vt:
        vs2 = vr

    ts2.append(ts2[-1] + dt)
    v2.append(vs2)

plt.plot(ts2, v2)
plt.xlabel("Time (ms)")
plt.ylabel("Voltage (mV)")
plt.title("3. Integrate & fire model simulation with Ie = 2.9 nA")
plt.show()

# Q2.4 Currents ranging from 2 to 5 in steps of 0.1
ie5 = [2.0]
while ie5[-1] < 5.0:
    i = ie5[-1] + 0.1
    ie5.append(round(i, 2))

firingRate = []
for i in range(len(ie5)):
    print(ie5[i])

    ts3 = [t0]
    v3 = [vr]
    spike = 0
    while ts3[-1] < t:
        vs3 = v3[-1] + dv(v3[-1], ie5[i]) * dt

        if vs3 > vt:
            vs3 = vr
            spike += 1

        ts3.append(ts3[-1] + dt)
        v3.append(vs3)

    firingRate.append(spike)
    print(firingRate[i])

plt.plot(ie5, firingRate)
plt.xlabel("Input current (nA)")
plt.ylabel("Firing rate (Hz)")
plt.title("4. Firing rate for currents ranging from 2 nA to 5 nA")
plt.show()