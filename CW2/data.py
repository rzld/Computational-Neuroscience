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

t_max = max(t_array)
t_min = min(t_array)
t_range = int(t_max - t_min)
print(t_max)
print(t_min)
print(t_range)
full_time = []
t_temp = t_min

for i in range(0, t_range):
    full_time.append(t_temp)
    t_temp += 1

n1_time = numpy.zeros(t_range)

for n_index in range(len(n1)):
    for t_index in range(len(full_time)):
        if n1[n_index] == full_time[t_index]:
            n1_time[t_index] = 1


print(len(n1_time))

#plot
plt.plot(full_time, n1_time)
plt.xlabel("Time")
plt.ylabel("Neuron 1 Spikes")
plt.title("Times when Neuron 1 spikes")
plt.show()