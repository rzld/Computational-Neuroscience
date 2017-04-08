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
    n2.append(n)

for n in neuron3:
    n3.append(n)

for n in neuron4:
    n4.append(n)

#print(len(x_array))
#print(len(y_array))
#print(len(t_array))
#print(len(n1))
#print(len(n2))
#print(len(n3))
#print(len(n4))

n1_time = numpy.zeros(len(t_array))

for n_index in range(len(n1)):
    for t_index in range(len(t_array)):
        if n1[n_index] == t_array[t_index]:
            n1_time[t_index] = 1


print(len(n1_time))

#plot
plt.plot(t_array, n1_time)
plt.xlabel("Time")
plt.ylabel("Neuron 1 Spikes")
plt.title("Times when Neuron 1 spikes")
plt.show()