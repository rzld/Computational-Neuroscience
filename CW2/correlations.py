import math
import matplotlib.pyplot as plt
import numpy

def crosscorr(na, nb):
    result = numpy.correlate(na, nb, "Full")
    return result[math.floor(result.size/2):]

def autocorr(nc):
    result = numpy.zeros(len(steps))
    for nn in range(len(nc)):
        for mm in range(len(nc)):
            dif = round((nc[mm] - nc[nn]) / 10000, 2)
            # print(dif)
            if interval >= dif >= -interval:
                # print(dif)
                for y in range(len(steps)):
                    if dif == steps[y]:
                        result[y] += 1

    return result

def convert_neuron(time_int, na):
    ii = 0
    result = numpy.zeros(len(time_int))
    while ii < len(na):
        for j in range(dt):
            if ii < len(na):
                result[math.floor(ii/dt)] += na[ii]
                ii += 1
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

# t_max = max(t_array)
# t_min = min(t_array)
# t_range = int(t_max - t_min)
# t_delta = (t_max - t_min) / t_range
# print(t_max)
# print(t_min)
# #print(t_range)
# #print(t_delta)
# full_time = []
# t_temp = t_min
#
# for i in range(0, t_range):
#     full_time.append(math.floor(t_temp))
#     t_temp += 1
#
# n1_time = numpy.zeros(t_range)
# n2_time = numpy.zeros(t_range)
# n3_time = numpy.zeros(t_range)
# n4_time = numpy.zeros(t_range)
#
# for t_index in range(len(full_time)):
#     for n_index in range(len(n1)):
#         if math.floor(n1[n_index]) == full_time[t_index]:
#             n1_time[t_index] += 1
#     for n_index in range(len(n2)):
#         if math.floor(n2[n_index]) == full_time[t_index]:
#             n2_time[t_index] += 1
#     for n_index in range(len(n3)):
#         if math.floor(n3[n_index]) == full_time[t_index]:
#             n3_time[t_index] += 1
#     for n_index in range(len(n4)):
#         if math.floor(n4[n_index]) == full_time[t_index]:
#             n4_time[t_index] += 1

#plot: firing rate per second
# plt.plot(full_time, n1_time)
# plt.xlabel("Time (s)")
# plt.ylabel("Firing rate (Spikes/s)")
# plt.title("Neuron 1 Firing Rate per Second")
# plt.show()
#
# plt.plot(full_time, n2_time)
# plt.xlabel("Time (s)")
# plt.ylabel("Firing rate (Spikes/s)")
# plt.title("Neuron 2 Firing Rate per Second")
# plt.show()
#
# plt.plot(full_time, n3_time)
# plt.xlabel("Time (s)")
# plt.ylabel("Firing rate (Spikes/s)")
# plt.title("Neuron 3 Firing Rate per Second")
# plt.show()
#
# plt.plot(full_time, n4_time)
# plt.xlabel("Time (s)")
# plt.ylabel("Firing rate (Spikes/s)")
# plt.title("Neuron 4 Firing Rate per Second")
# plt.show()

### PLOT POSITION
# x_time = numpy.zeros(t_range)
# y_time = numpy.zeros(t_range)
#
# for t_index in range(len(t_array)):
#     for t2_index in range(len(full_time)):
#         if math.floor(t_array[t_index]) == full_time[t2_index]:
#             x_time[t2_index] = x_array[t_index]
#             y_time[t2_index] = y_array[t_index]
#
# x_n1 = numpy.zeros(t_range)
# y_n1 = numpy.zeros(t_range)
# x_n2 = numpy.zeros(t_range)
# y_n2 = numpy.zeros(t_range)
# x_n3 = numpy.zeros(t_range)
# y_n3 = numpy.zeros(t_range)
# x_n4 = numpy.zeros(t_range)
# y_n4 = numpy.zeros(t_range)
#
# for index in range(t_range):
#     if n1_time[index] > 0:
#         x_n1[index] = x_time[index]
#         y_n1[index] = y_time[index]
#     if n2_time[index] > 0:
#         x_n2[index] = x_time[index]
#         y_n2[index] = y_time[index]
#     if n3_time[index] > 0:
#         x_n3[index] = x_time[index]
#         y_n3[index] = y_time[index]
#     if n4_time[index] > 0:
#         x_n4[index] = x_time[index]
#         y_n4[index] = y_time[index]

# plt.plot(x_array, y_array)
# plt.plot(x_n1, y_n1, 'ro')
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.title("Neuron 1 Spikes Position")
# plt.show()
#
# plt.plot(x_array, y_array)
# plt.plot(x_n2, y_n2, 'ro')
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.title("Neuron 2 Spikes Position")
# plt.show()
#
# plt.plot(x_array, y_array)
# plt.plot(x_n3, y_n3, 'ro')
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.title("Neuron 3 Spikes Position")
# plt.show()
#
# plt.plot(x_array, y_array)
# plt.plot(x_n4, y_n4, 'ro')
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.title("Neuron 4 Spikes Position")
# plt.show()

## converting the neurons to certain time interval
# dt = 100     # time interval in seconds
# time_interval = []
#
# t_temp = 0
# max_interval = (math.floor(t_max) - math.floor(t_min))
# while t_temp < math.floor(max_interval):
#     time_interval.append(t_temp)
#     t_temp += dt
#
# n1_compact = convert_neuron(time_interval, n1_time)
# n2_compact = convert_neuron(time_interval, n2_time)
# n3_compact = convert_neuron(time_interval, n3_time)
# n4_compact = convert_neuron(time_interval, n4_time)

# print(len(time_interval))
# print(len(n1_compact))
#
# n1_auto2 = numpy.zeros(len(time_interval))
#
# for ii in range(len(n1_compact)):
#     for jj in range(len(n1_compact)):
#         timedif = time_interval[jj] - time_interval[ii]
#         if timedif == 0:
#             n1_auto2[timedif] += n1_compact[ii]
#         else:
#             n1_auto2[jj-ii] += n1_compact[ii]
#             n1_auto2[jj-ii] += n1_compact[jj]
#
# print(n1_auto2)

interval = 1.0
bins = 0.02
step = numpy.arange(-interval, interval + bins, bins)
steps = []
for s in step:
    steps.append(float(round(s, 2)))

n1_auto2 = autocorr(n1)
n2_auto2 = autocorr(n2)
n3_auto2 = autocorr(n3)
n4_auto2 = autocorr(n4)

y_pos = numpy.arange(len(steps))
plt.bar(y_pos, n1_auto2, align='center', alpha=0.5)
plt.xticks(y_pos, steps)
plt.xlabel("dt (s)")
plt.ylabel("Number of spikes")
plt.title("Auto-corelation of Neuron 1")
plt.show()

plt.plot(n1_auto2)
plt.show()
plt.plot(n2_auto2)
plt.show()
plt.plot(n3_auto2)
plt.show()
plt.plot(n4_auto2)
plt.show()



### Auto-correlation
# n1_auto = autocorr(n1_compact)
# n2_auto = autocorr(n2_compact)
# n3_auto = autocorr(n3_compact)
# n4_auto = autocorr(n4_compact)
#
# ### Cross-corelation
# n1_cross_n2 = crosscorr(n1_compact, n2_compact)
# n1_cross_n3 = crosscorr(n1_compact, n3_compact)
# n1_cross_n4 = crosscorr(n1_compact, n4_compact)
#
# n2_cross_n3 = crosscorr(n2_compact, n3_compact)
# n2_cross_n4 = crosscorr(n2_compact, n4_compact)
#
# n3_cross_n4 = crosscorr(n3_compact, n4_compact)
#
# ## Plots
# y_pos = numpy.arange(len(time_interval))

# plt.bar(y_pos, n1_auto, align='center', alpha=0.5)
# plt.xticks(y_pos, time_interval)
# plt.xlabel("dt (s)")
# plt.ylabel("Number of spikes")
# plt.title("Auto-corelation of Neuron 1")
# plt.show()
#
# plt.bar(y_pos, n2_auto, align='center', alpha=0.5)
# plt.xticks(y_pos, time_interval)
# plt.xlabel("dt (s)")
# plt.ylabel("Number of spikes")
# plt.title("Auto-corelation of Neuron 2")
# plt.show()
#
# plt.bar(y_pos, n3_auto, align='center', alpha=0.5)
# plt.xticks(y_pos, time_interval)
# plt.xlabel("dt (s)")
# plt.ylabel("Number of spikes")
# plt.title("Auto-corelation of Neuron 3")
# plt.show()
#
# plt.bar(y_pos, n4_auto, align='center', alpha=0.5)
# plt.xticks(y_pos, time_interval)
# plt.xlabel("dt (s)")
# plt.ylabel("Number of spikes")
# plt.title("Auto-corelation of Neuron 4")
# plt.show()
#
# plt.bar(y_pos, n1_cross_n2, align='center', alpha=0.5)
# plt.xticks(y_pos, time_interval)
# plt.xlabel("dt (s)")
# plt.ylabel("Number of spikes")
# plt.title("Cross-corelation between Neuron 1 & 2")
# plt.show()
#
# plt.bar(y_pos, n1_cross_n3, align='center', alpha=0.5)
# plt.xticks(y_pos, time_interval)
# plt.xlabel("dt (s)")
# plt.ylabel("Number of spikes")
# plt.title("Cross-corelation between Neuron 1 & 3")
# plt.show()
#
# plt.bar(y_pos, n1_cross_n4, align='center', alpha=0.5)
# plt.xticks(y_pos, time_interval)
# plt.xlabel("dt (s)")
# plt.ylabel("Number of spikes")
# plt.title("Cross-corelation between Neuron 1 & 4")
# plt.show()
#
# plt.bar(y_pos, n2_cross_n3, align='center', alpha=0.5)
# plt.xticks(y_pos, time_interval)
# plt.xlabel("dt (s)")
# plt.ylabel("Number of spikes")
# plt.title("Cross-corelation between Neuron 2 & 3")
# plt.show()
#
# plt.bar(y_pos, n2_cross_n4, align='center', alpha=0.5)
# plt.xticks(y_pos, time_interval)
# plt.xlabel("dt (s)")
# plt.ylabel("Number of spikes")
# plt.title("Cross-corelation between Neuron 2 & 4")
# plt.show()
#
# plt.bar(y_pos, n3_cross_n4, align='center', alpha=0.5)
# plt.xticks(y_pos, time_interval)
# plt.xlabel("dt (s)")
# plt.ylabel("Number of spikes")
# plt.title("Cross-corelation between Neuron 3 & 4")
# plt.show()