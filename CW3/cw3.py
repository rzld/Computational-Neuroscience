import matplotlib.pyplot as plt
import math

# functions
def dv(v0, ie):
    return (v_rest - v0 + rm * ie)/tau_m

# variables
v_rest = -65                # resting potential
v_th = -50                  # spike threshold
v_reset = -65               # reset voltage
rm = 100                    # resistance
mem_cap = 0.1               # membrane capacitance
tau_m = 10                  # time constant in ms
N = 40                      # number of incoming synapses
tau_syn = 2                 # decay time constant in ms
dt = 1                      # time step in ms
t = 200000                  # time in ms (200 or 300 secs)
r = 10                      # average firing rate in Hz
# STDP model parameters
a_plus = 0.1                # in nS
a_minus = 0.12              # in nS
tau_plus = 20               # in ms
tau_minus = 20              # in ms

STDP_mode = True            # STDP mode switch

#integrate and fire
ts = [0]
v = [v_reset]

ie = (v_th - v_rest) / rm

while ts[-1] < t:
    vs = v[-1] + dv(v[-1], ie) * dt
    if vs > v_th:
        vs = v_reset

    ts.append(ts[-1] + dt)
    v.append(vs)

plt.plot(ts, v)
plt.xlabel("Time (ms)")
plt.ylabel("Voltage (mV)")
plt.title("1. Integrate & fire model simulation")
plt.show()

#Question 1
strength = 2           # initial synapse strenth in nS ... wij?
