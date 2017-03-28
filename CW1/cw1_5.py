#Code for Question 5 coupled neurons
#Before running the code, make sure to set the correct
# ist function and plot title according to
# which neurons (excitatory/inhibitory) to use


import matplotlib.pyplot as plt
import math
import random

# functions
def ist(es, V, sx):
    return rm_gs * sx * (es - V)

def dv(V, ist):
    return (el - V + ist + rm_ie)/tau_m

def ds(s):
    return -s/tau_s

#variables
tau_m = 20
el = -70
vr = -80
vt = -54
rm_ie = 18
rm_gs = 0.15
p = 0.5
tau_s = 10
es1 = 0         #excitatory
es2 = -80       #inhibitory
v01 = random.uniform(vr, vt)
v02 = random.uniform(vr, vt)
dt = 1
t = 1000

#main program
#Q5. simulate two neurons with parameters above
#    and with es = 0 & es = 80
ts = [0]
stx = [0]
v1 = [v01]
v2 = [v02]
s1 = [0]
s2 = [0]

print(v01, v02)

while ts[-1] < t:
    #neuron 1
    ist_1 = ist(es1, v1[-1], s1[-1])             #Q5 excitatory
    #ist_1 = ist(es2, v1[-1], s1[-1])            #Q5 inhibitory

    v1x = v1[-1] + dv(v1[-1], ist_1) * dt
    s1x = s1[-1] + ds(s1[-1]) * dt

    #neuron 2
    ist_2 = ist(es1, v2[-1], s2[-1])             #Q5 excitatory
    #ist_2 = ist(es2, v2[-1], s2[-1])            #Q5 inhibitory

    v2x = v2[-1] + dv(v2[-1], ist_2) * dt
    s2x = s2[-1] + ds(s2[-1]) * dt

    if v1x > vt:
        v1x = vr
        s2.append(s2x+p)
    else:
        s2.append(s2x)

    if v2x > vt:
        v2x = vr
        s1.append(s1x+p)
    else:
        s1.append(s1x)

    ts.append(ts[-1] + dt)
    v1.append(v1x)
    v2.append(v2x)

plt.plot(ts, v1)
plt.plot(ts, v2)
plt.xlabel("Time (ms)")
plt.ylabel("Voltage (mV)")
plt.title("5. Two neurons simulation (excitatory)")
#plt.title("5. Two neurons simulation (inhibitory)")
plt.legend(['Neuron 1', 'Neuron 2'], loc='upper right')
plt.show()