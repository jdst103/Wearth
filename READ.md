
Zambi is on winter vacation, and he has decided to go to the planet Wearth. The only way of traveling through space is
by using the aliens' teleportation machines. Zambia can teleport directly from planet Earth to the planet Wearth, but it is
really risky. The aliens haven't perfected their teleportation machine. The greater the distance of traveling the bigger is risk.
Because of this, the aliens have built more teleportation stations all throughout space. Teleporting through consecutive
teleportation stations lowers the risk.
Zambi wants to go to the planet Wearth using the path where the teleportations are as short as possible - the path where
the longest teleportation on it is minimized.
Zambi opened http://www.space-net.spc and found a list of all the space teleportation stations. He decided to use the
least risky path, as described above.
Help Zambi find the safest path from Earth to the planet Zearth: the path where the longest distance he has to teleport is
minimized.
INPUT:
The first line of the standard input contains three real numbers, each from the interval [-10000.00, 10000.00], representing
the 3D coordinates of the planet Zearth. The next line contains a number N, corresponding to the number of teleportation
stations in space (1<=N<=2000). Each of the next N lines contains three real numbers each from the interval [-10000.00,
10000.00], representing the 3D coordinates for each station.
Note: The 3D coordinates of Earth are (0.0, 0.0, 0.0). On the planets Earth and Zearth there are teleportation stations, too.
OUTPUT:
To the standard output write one real number to 2 decimal places, representing the maximum distance of the safest path on
 Zambi's way to Zearth.

OUTPUT:
To the standard output write one real number to 2 decimal places, representing the maximum distance of the safest path on
Zambi's way to Wearth.
Input (stdin):
2.00 2.00 4.00
4
0.00 0.00 2.00
0.00 2.00 2.00
2.00 0.00 0.00
0.00 0.00 2.00

Output (stdout):
2.83

Additional example:
Input:
2.00 2.00 2.00
3
1.00 1.00 1.00
1.00 2.00 2.00
2.00 2.00 1.00
Output:
1.73