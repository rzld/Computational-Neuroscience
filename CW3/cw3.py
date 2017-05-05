import matplotlib.pyplot as plt
import math
import numpy
import random


# functions
def dv(v0, iex):
    return (v_rest - v0 + rm * iex)/tau_m


def ist(vx, tx, gs):
    #st = (tx * math.exp(-tx/tau_s))/(tau_s * math.exp(-1))
    st = (tx * math.exp(-tx / tau_s))
    return gs * st * (vx - e_s)


def ist2(vx, st, gs):
    #st = (tx * math.exp(-tx/tau_s))/(tau_s * math.exp(-1))
    return gs * st * (vx - e_s)


def ds(sy):
    return -sy/tau_s

# variables
v_rest = -65                # resting potential
v_th = -50                  # spike threshold
v_reset = -65               # reset voltage
rm = 100                    # resistance
mem_cap = 0.1               # membrane capacitance
tau_m = 10                  # time constant in ms
N = 40                      # number of incoming synapses
tau_s = 2                   # decay time constant in ms
dt = 1                      # time step in ms
t = 200000                  # time in ms (200 or 300 secs)
r_init = 10                 # average initial firing rate in Hz
e_s = 0                     # reversal potential in mV
# STDP model parameters
a_plus = 0.1                # in nS
a_minus = 0.12              # in nS
tau_plus = 20               # in ms
tau_minus = 20              # in ms

STDP_mode = True            # STDP mode switch

#integrate and fire
ts = [0]
v = [v_reset]
s = [0]
peak_cond = 2.0             # peak conductance in nanoSiemens
spike_in_neuron = numpy.zeros(N)
recent_pre_spike = numpy.zeros(N)
recent_post_spike = 0

#ie = (v_th - v_rest) / rm

while ts[-1] < t:
    isx = []
    ie = 0
    #presynaptic neurons
    for i in range(N):
        # poisson process
        g_syn = random.uniform(0.0, peak_cond)

        if 1.0 > r_init * dt > g_syn:
            spike_in_neuron[i] += 1
            recent_pre_spike[i] = ts[-1]
        else:
            recent_pre_spike[i] = recent_pre_spike[i-1]

        delta_t = recent_post_spike - recent_pre_spike[i]
        if delta_t > 0:
            g_syn = g_syn + a_plus * math.exp(-abs(delta_t)/tau_plus)
        elif delta_t <= 0:
            g_syn = g_syn - a_minus * math.exp(-abs(delta_t)/tau_minus)

        #sx = s[-1] + ds(s[-1]) * dt
        is_ = ist2(v[-1], s[-1], g_syn)
        ie += is_

    #postsynaptic neurons
    vs = v[-1] + dv(v[-1], ie) * dt
    sx = s[-1] + ds(s[-1]) * dt

    if vs > v_th:
        vs = v_reset
        s.append(sx + 1)
        recent_post_spike = ts[-1]
    else:
        s.append(sx)

    ts.append(ts[-1] + dt)
    v.append(vs)

plt.plot(ts, v)
plt.xlabel("Time (ms)")
plt.ylabel("Voltage (mV)")
plt.title("1. Integrate & fire model simulation")
plt.show()

#Question 1
strength = 2           # initial synapse strenth in nS ... wij?
