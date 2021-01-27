import math
import numpy as np

'''File handling: opens 'inputq1.txt' file and using f.read reads contents of file.
Then split the content by lines in a list.
e.g
['2.00 2.00 2.00', '3', '1.00 1.00 1.00', '1.00 2.00 2.00', '2.00 2.00 1.00']
'''
with open('inputQ1.txt', 'r') as f:
    Lines = f.read().split('\n')

'''Defining Zearth Coordinates slicing from the first line on the file.
Currently a string, splitting values into a list'''
Earth = [0, 0, 0]
Zearth = Lines[0].split(" ")

# Wearth has to be between -10,000 and 10,000
'''Converting Earth and Zearth as a array'''
Earth = np.array(Earth, dtype=float)
Zearth = np.array(Zearth, dtype=float)

Stations = Lines[2:]
list_of_stations = []

'''
Converting string to int
'''
N = int(Lines[1])
N_lines = len(Stations)

# print(Wearth)# Wearth has to be between -10,000 and 10,000
if (Zearth > -10000).all() and (Zearth < 10000).all():
    if 1 <= N <= 2000 and N == N_lines:
            #N has to be within 1 and 2000

'''Appending station coordinates (type=string) into a empty list as a array.'''
# Stations  has to be between -10,000 and 10,000
 s = 3
        for Station in Stations:
            Station = Station.split(" ")
            Station = np.array(Station, dtype=float)
            if (Station > -10000).all() and (Station < 10000).all():
                pass
            else:
                # print(f"The coordinates for the Teleportation station '{Station}' on line {s} is out of bounds.\n "
                #             f"Teleportation station coordinates has to be between -10,000 and 10,000 :)\n")
                continue
            list_of_stations.append(Station)
            s = s + 1

'''finding magnitude of vector from each station to Earth. appending these magnitude into a empty list'''
        Dis_from_earth = []
        i = 0
        while i < len(list_of_stations):
            sumA = list_of_stations[i] - Earth
            sumB = sumA * sumA
            Dis_from_earth.append(math.sqrt(sumB.sum()))
            i += 1

'''finding magnitude of vector from each station to Wearth. appending these magnitude into a empty list'''
        j = 0
        Dis_from_Zearth = []
        while j < len(list_of_stations):
            sumC = Zearth - list_of_stations[j]
            sumD = sumC * sumC
            Dis_from_Zearth.append(math.sqrt(sumD.sum()))
            j += 1

 '''finding smallest distance difference between distance to earth and distance to Wearth and appending to list'''
        k = 0
        distance_differences = []
        while k < len(list_of_stations):
            diff = Dis_from_earth[k] - Dis_from_Zearth[k]
            diff = abs(diff)
            distance_differences.append(diff)
            k += 1

 '''Finding index number for the minimum distance in list of distance_differences. This index number will specify
        which teleportation station as the safest path to take'''
        x = distance_differences.index(min(distance_differences))

  '''prints the minimum distance of the safest path between the distance from Earth to the teleportation station
        and, the teleportation station to Zearth rounded to 2 decimal places'''
        print(round(min(Dis_from_Zearth[x], Dis_from_earth[x]), 2))
    else:
        print(f"N = {N}. To be able to continue working out the safest path from Earth to the planet Wearth:"
              ****f" 'N' has to be between 1 and 2000 \nand, 'N' is equal to the number of stations on the list.\n")
else:
    print(f"Sorry.. The coordinates for Zearth '{Zearth}' is out of bounds. Zearth coordinates has to be between -10,000 and 10,000 :)")


References:
https://www.youtube.com/watch?v=Uh2ebFW8OYM
---------------------

