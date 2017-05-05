# COURSEWORK 2
# by Rizaldi Tri Yanuar
# In this code:
# 1. Firing rates of each neuron
# 2. Positions where each neuron fired spikes.


import math
import matplotlib.pyplot as plt
import numpy


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

secs = 10000

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

t_max = max(t_array)
t_min = min(t_array)
t_range = int(t_max - t_min)
t_delta = (t_max - t_min) / t_range
print(t_max)
print(t_min)
#print(t_range)
#print(t_delta)
full_time = []
t_temp = t_min

for i in range(0, t_range):
    full_time.append(math.floor(t_temp))
    t_temp += 1

n1_time = numpy.zeros(t_range)
n2_time = numpy.zeros(t_range)
n3_time = numpy.zeros(t_range)
n4_time = numpy.zeros(t_range)

for t_index in range(len(full_time)):
    for n_index in range(len(n1)):
        if math.floor(n1[n_index]) == full_time[t_index]:
            n1_time[t_index] += 1
    for n_index in range(len(n2)):
        if math.floor(n2[n_index]) == full_time[t_index]:
            n2_time[t_index] += 1
    for n_index in range(len(n3)):
        if math.floor(n3[n_index]) == full_time[t_index]:
            n3_time[t_index] += 1
    for n_index in range(len(n4)):
        if math.floor(n4[n_index]) == full_time[t_index]:
            n4_time[t_index] += 1

#plot: firing rate per second
plt.plot(full_time, n1_time)
plt.xlabel("Time (s)")
plt.ylabel("Firing rate (Spikes/s)")
plt.title("Neuron 1 Firing Rate per Second")
plt.show()

plt.plot(full_time, n2_time)
plt.xlabel("Time (s)")
plt.ylabel("Firing rate (Spikes/s)")
plt.title("Neuron 2 Firing Rate per Second")
plt.show()

plt.plot(full_time, n3_time)
plt.xlabel("Time (s)")
plt.ylabel("Firing rate (Spikes/s)")
plt.title("Neuron 3 Firing Rate per Second")
plt.show()

plt.plot(full_time, n4_time)
plt.xlabel("Time (s)")
plt.ylabel("Firing rate (Spikes/s)")
plt.title("Neuron 4 Firing Rate per Second")
plt.show()

### PLOT POSITION
x_time = numpy.zeros(t_range)
y_time = numpy.zeros(t_range)

for t_index in range(len(t_array)):
    for t2_index in range(len(full_time)):
        if math.floor(t_array[t_index]) == full_time[t2_index]:
            x_time[t2_index] = x_array[t_index]
            y_time[t2_index] = y_array[t_index]

x_n1 = numpy.zeros(t_range)
y_n1 = numpy.zeros(t_range)
x_n2 = numpy.zeros(t_range)
y_n2 = numpy.zeros(t_range)
x_n3 = numpy.zeros(t_range)
y_n3 = numpy.zeros(t_range)
x_n4 = numpy.zeros(t_range)
y_n4 = numpy.zeros(t_range)

for index in range(t_range):
    if n1_time[index] > 0:
        x_n1[index] = x_time[index]
        y_n1[index] = y_time[index]
    if n2_time[index] > 0:
        x_n2[index] = x_time[index]
        y_n2[index] = y_time[index]
    if n3_time[index] > 0:
        x_n3[index] = x_time[index]
        y_n3[index] = y_time[index]
    if n4_time[index] > 0:
        x_n4[index] = x_time[index]
        y_n4[index] = y_time[index]

plt.plot(x_array, y_array)
plt.plot(x_n1, y_n1, 'ro')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Neuron 1 Spikes Position")
plt.show()

plt.plot(x_array, y_array)
plt.plot(x_n2, y_n2, 'ro')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Neuron 2 Spikes Position")
plt.show()

plt.plot(x_array, y_array)
plt.plot(x_n3, y_n3, 'ro')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Neuron 3 Spikes Position")
plt.show()

plt.plot(x_array, y_array)
plt.plot(x_n4, y_n4, 'ro')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Neuron 4 Spikes Position")
plt.show()