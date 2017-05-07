#Question 2

import matplotlib.pyplot as plt
import math
import numpy
import random


# functions
def dv(v0, iex):
    return (v_rest - v0 + rm * iex)/tau_m


def dv2(v0, istx, iex):
    return (v_rest - v0 + istx + rm * iex)/tau_m


def ist(vx, tx, gs):
    #st = (tx * math.exp(-tx/tau_s))/(tau_s * math.exp(-1))
    st = (tx * math.exp(-tx / tau_s))
    return gs * st * (vx - e_s)


def ist2(vx, st, gs):
    #st = (tx * math.exp(-tx/tau_s))/(tau_s * math.exp(-1))
    return gs * st * (e_s - vx)


def ist3(gs, v0, st):
    return rm * gs * st * (e_s - v0)


def ds(sy):
    return -sy/tau_s


def ds2(tx):
    return math.exp(-tx/tau_s)

# variables
v_rest = -65                # resting potential
v_th = -50                  # spike threshold
v_reset = -65               # reset voltage
rm = 100                    # resistance
mem_cap = 0.1               # membrane capacitance (C, in nF)
tau_m = 10                  # time constant in ms
N = 40                      # number of incoming synapses
tau_s = 2                   # decay time constant in ms
dt = 1                      # time step in ms
t = 200000                  # time in ms (200 or 300 secs)
#r_init = 15                 # average initial firing rate in Hz | Q1 = 15
e_s = 0                     # reversal potential in mV
# STDP model parameters
a_plus = 0.1                # in nS
a_minus = 0.12              # in nS
tau_plus = 20               # in ms
tau_minus = 20              # in ms

STDP_mode = True            # STDP mode switch

#integrate and fire

input_fr = [10]
while input_fr[-1] < 20:
    x_ = input_fr[-1] + 1
    input_fr.append(x_)

frate_per_input = numpy.zeros(len(input_fr))

print(input_fr)

for a in range(len(input_fr)):
    ts = [0]
    v = [v_reset]
    s = [0]
    s2 = numpy.zeros(N)
    peak_cond = 2.0  # peak conductance in nanoSiemens
    spike_in_neuron = numpy.zeros(N)
    recent_pre_spike = numpy.zeros(N)
    recent_post_spike = 0
    g_syn = numpy.zeros(N)
    isx = numpy.zeros(N)
    g_update = numpy.zeros(N)
    post_spike = numpy.zeros(t)

    steady_g_syn = numpy.zeros((10000, N))
    r_init = input_fr[a]
    #ie = (v_th - v_rest) / rm
    for i in range(N):
        #g_syn[i] = random.uniform(0.0, peak_cond)
        if STDP_mode:
            g_syn[i] = random.uniform(0.0, peak_cond)
        else:
            g_syn[i] = 0.069            #Question 1 w/o STDP

    while ts[-1] < t:
        ie = 0
        #presynaptic neurons
        for i in range(N):
            # sx = s[-1] + ds(s[-1]) * dt
            isx[i] = ist2(v[-1], s2[i], g_syn[i])
            # is_ = ist(v[-1], ts[-1], g_syn)
            # print(isx[i])
            ie += isx[i]

            # poisson process
            rand_num = random.uniform(0, r_init*2)

            if r_init * dt > rand_num:
                spike_in_neuron[i] += 1
                recent_pre_spike[i] = ts[-1]
                s2[i] += 1
                #print("spike!")
            else:
                s2[i] = ds2(ts[-1])

            #update
            if STDP_mode:
                delta_t = recent_post_spike - recent_pre_spike[i]

                if delta_t > 0:
                    g_update[i] = a_plus * math.exp(-abs(delta_t)/tau_plus)
                elif delta_t <= 0:
                    g_update[i] = -a_minus * math.exp(-abs(delta_t)/tau_minus)

                g_syn[i] += g_update[i]

                if g_syn[i] < 0:
                    g_syn[i] = 0
                if g_syn[i] > 2.0:
                    g_syn[i] = 2.0

        if ts[-1] > t - 10000:
            steady_g_syn[ts[-1]-(t-10000)][i] += g_syn[i]

        #print(ie)

        #postsynaptic neurons
        vs = v[-1] + dv(v[-1], ie) * dt
        #sx = s[-1] + ds(s[-1]) * dt
        sx = ds2(ts[-1])
        #print(sx)

        if vs > v_th:
            vs = v_reset
            s.append(s[-1] + 1)
            recent_post_spike = ts[-1]
            post_spike[ts[-1]] += 1
        else:
            s.append(sx)

        #print(vs)

        ts.append(ts[-1] + dt)
        v.append(vs)

    g_avg = numpy.mean(g_syn)
    print(g_avg)

    seconds_ = int(t/1000)
    post_spike_avg = numpy.zeros(seconds_)

    for i in range(len(post_spike)):
        post_spike_avg[math.floor(i/1000)] += post_spike[i]

    frate_avg = 0
    for j in range(10):
        frate_avg += post_spike_avg[seconds_-1-j]

    frate_avg /= 10
    print(frate_avg)

    steady_gsyn_2 = numpy.zeros((10, N))
    #steady_gsyn_avg

    for i in range(10000):
        for j in range(N):
            steady_gsyn_2[math.floor(i/1000)][j] += steady_g_syn[i][j]

    frate_per_input[a] = frate_avg

    if r_init == 10 or r_init == 20:
        plt.hist(g_syn, bins=50, facecolor='r', alpha=1.0)
        plt.xlabel("Weight")
        plt.ylabel("Frequency")
        plt.title("Steady-State Synaptic Weights Distribution")
        plt.show()

        plt.plot(g_syn)
        plt.xlabel("Synapse")
        plt.ylabel("Weight")
        plt.title("Steady-State Synaptic Weights for Each Synapse")
        plt.show()

        plt.plot(steady_gsyn_2)
        plt.xlabel("Time (s)")
        plt.ylabel("Weight")
        plt.title("Steady-State Synaptic Weights for the last 10 seconds")
        plt.show()

plt.plot(input_fr, frate_per_input)
plt.xlabel("Input Firing Rate")
plt.ylabel("Average Output Firing Rate")
plt.title("Firing Rate - Output vs Input")
plt.show()