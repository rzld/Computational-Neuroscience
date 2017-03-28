import matplotlib.pyplot as plt
import math

# functions

def dv(vx, gk):
    return (el - vx + rm * ie + (rm * gk)*(ek - vx))/tau_m

def dgk(gk):
    return -gk/tau_k

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
v0 = 0

#Q6. simulation with slow potassium current
ek = -80
dg = 0.005      #conductance increase
tau_k = 200     #tau, in ms

ts = [t0]
v = [vr]
gk = [0]

while ts[-1] < t:
    vs = v[-1] + dv(v[-1], gk[-1]) * dt
    gkx = gk[-1] + dgk(gk[-1]) * dt

    if vs > vt:
        vs = vr
        gk.append(gkx + dg)
    else:
        gk.append(gkx)

    ts.append(ts[-1] + dt)
    v.append(vs)

plt.plot(ts, v)
plt.xlabel("Time (ms)")
plt.ylabel("Voltage (mV)")
plt.title("6. Integrate & fire with slow potassium current")
plt.show()