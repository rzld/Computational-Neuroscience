# COURSEWORK 2
# by Rizaldi Tri Yanuar
# In this code:
# 1. Auto-correlations of each neuron.
# 2. Cross-correlations between pairs of neurons.


import matplotlib.pyplot as plt
import numpy


def crosscorr(na, nb):
    result = []
    for nn in range(len(na)):
        for mm in range(len(nb)):
            dif = round((nb[mm] - na[nn]) / 10000, 2)
            # print(dif)
            if interval >= dif >= -interval:
                result.append(dif)

    return result


def autocorr(nc):
    result = []
    for nn in range(len(nc)):
        for mm in range(len(nc)):
            dif = round((nc[mm] - nc[nn]) / 10000, 2)
            # print(dif)
            if interval >= dif >= -interval:
                result.append(dif)

    return result


# for loading neuron 1 - 4 and time
f = open("neuron1.csv")
neuron1 = map(lambda x: int(x.strip()), f.readlines())

f = open("neuron2.csv")
neuron2 = map(lambda x: int(x.strip()), f.readlines())

f = open("neuron3.csv")
neuron3 = map(lambda x: int(x.strip()), f.readlines())

f = open("neuron4.csv")
neuron4 = map(lambda x: int(x.strip()), f.readlines())

f = open("time.csv")
time = map(lambda x: int(x.strip()), f.readlines())

# for loading x and y
f = open("x.csv")
x_data = map(lambda x: float(x.strip()), f.readlines())

f = open("y.csv")
y_data = map(lambda x: float(x.strip()), f.readlines())

x_array = []
y_array = []
t_array = []
n1 = []
n2 = []
n3 = []
n4 = []

secs = 1

for x in x_data:
    x_array.append(x)

for y in y_data:
    y_array.append(y)

for t in time:
    t_array.append(t/secs)

for n in neuron1:
    n1.append(n/secs)

for n in neuron2:
    n2.append(n/secs)

for n in neuron3:
    n3.append(n/secs)

for n in neuron4:
    n4.append(n/secs)

interval = 1.0
bins = 0.02
step = numpy.arange(-interval, interval + bins, bins)
steps = []
for s in step:
    steps.append(float(round(s, 2)))

### Autocorrelation
n1_auto2 = autocorr(n1)
n2_auto2 = autocorr(n2)
n3_auto2 = autocorr(n3)
n4_auto2 = autocorr(n4)

plt.hist(n1_auto2, bins=50, facecolor='g', alpha=0.5)
plt.xlabel("Time interval (s)")
plt.ylabel("Number of spikes")
plt.title("Autocorrelogram of Neuron 1")
plt.show()

plt.hist(n2_auto2, bins=50, facecolor='g', alpha=0.5)
plt.xlabel("Time interval (s)")
plt.ylabel("Number of spikes")
plt.title("Autocorrelogram of Neuron 2")
plt.show()

plt.hist(n3_auto2, bins=50, facecolor='g', alpha=0.5)
plt.xlabel("Time interval (s)")
plt.ylabel("Number of spikes")
plt.title("Autocorrelogram of Neuron 3")
plt.show()

plt.hist(n4_auto2, bins=50, facecolor='g', alpha=0.5)
plt.xlabel("Time interval (s)")
plt.ylabel("Number of spikes")
plt.title("Autocorrelogram of Neuron 4")
plt.show()


### Crosscorelation
n1_cross_n2 = crosscorr(n1, n2)
n1_cross_n3 = crosscorr(n1, n3)
n1_cross_n4 = crosscorr(n1, n4)

n2_cross_n3 = crosscorr(n2, n3)
n2_cross_n4 = crosscorr(n2, n4)

n3_cross_n4 = crosscorr(n3, n4)

plt.hist(n1_cross_n2, bins=50, facecolor='r', alpha=1.0)
plt.xlabel("Time interval (s)")
plt.ylabel("Number of spikes")
plt.title("Crosscorrelogram of Neuron 1 & 2")
plt.show()

plt.hist(n1_cross_n3, bins=50, facecolor='r', alpha=1.0)
plt.xlabel("Time interval (s)")
plt.ylabel("Number of spikes")
plt.title("Crosscorrelogram of Neuron 1 & 3")
plt.show()

plt.hist(n1_cross_n4, bins=50, facecolor='r', alpha=1.0)
plt.xlabel("Time interval (s)")
plt.ylabel("Number of spikes")
plt.title("Crosscorrelogram of Neuron 1 & 4")
plt.show()

plt.hist(n2_cross_n3, bins=50, facecolor='r', alpha=1.0)
plt.xlabel("Time interval (s)")
plt.ylabel("Number of spikes")
plt.title("Crosscorrelogram of Neuron 2 & 3")
plt.show()

plt.hist(n2_cross_n4, bins=50, facecolor='r', alpha=1.0)
plt.xlabel("Time interval (s)")
plt.ylabel("Number of spikes")
plt.title("Crosscorrelogram of Neuron 2 & 4")
plt.show()

plt.hist(n3_cross_n4, bins=50, facecolor='r', alpha=1.0)
plt.xlabel("Time interval (s)")
plt.ylabel("Number of spikes")
plt.title("Crosscorrelogram of Neuron 3 & 4")
plt.show()