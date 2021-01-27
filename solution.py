import math
import numpy as np


with open('input.txt', 'r') as f:
    Lines = f.read().split('\n')

Earth = [0, 0, 0]
Wearth = Lines[0].split(" ")

Earth = np.array(Earth, dtype=float)
Wearth = np.array(Wearth, dtype=float)

Stations = Lines[2:]
list_of_stations = []

N = int(Lines[1])
N_lines = len(Stations)

if (Wearth > -10000).all() and (Wearth < 10000).all():

    if 1 <= N <= 2000 and N == N_lines:
        s = 3
        for Station in Stations:
            Station = Station.split(" ")
            Station = np.array(Station, dtype=float)

            if (Station > -10000).all() and (Station < 10000).all():
                pass
            else:
                continue
            list_of_stations.append(Station)
            s = s + 1

        Dis_from_earth = []
        i = 0
        while i < len(list_of_stations):
            sumA = list_of_stations[i] - Earth
            sumB = sumA * sumA
            Dis_from_earth.append(math.sqrt(sumB.sum()))
            i += 1

        j = 0
        Dis_from_wearth = []
        while j < len(list_of_stations):
            sumC = Wearth - list_of_stations[j]
            sumD = sumC * sumC
            Dis_from_wearth.append(math.sqrt(sumD.sum()))
            j += 1

        k = 0
        distance_differences = []
        while k < len(list_of_stations):
            diff = Dis_from_earth[k] - Dis_from_wearth[k]
            diff = abs(diff)
            distance_differences.append(diff)
            k += 1

        x = distance_differences.index(min(distance_differences))

        print(round(min(Dis_from_wearth[x], Dis_from_earth[x]), 2))
    else:
        pass
else:
    pass









