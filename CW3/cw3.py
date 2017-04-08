import matplotlib.pyplot as plt
import math

# functions
def dv(v0, ie):
    return (el - v0 + rm * ie)/tau_m

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