# find route between cities

import sys
import time
from queue import PriorityQueue

# function to print
def print_path(path_length, route):
    print(f"distance: {path_length} km\nroute:")
    for i in range(len(route) - 1):
        possible_vals = city_dict[route[i]]
        for j in range(len(possible_vals)):
            current = possible_vals[j]
            if current[0] == route[i + 1]:
                length = int(current[1])
                break
        print(f"{route[i]} to {route[i + 1]}, {length} km")

#incorrect format
if len(sys.argv) != 4:
    print("Error: Not the correct number of inputs")
    sys.exit(-1)

# get the starting info
text_file = sys.argv[1]
start_city = sys.argv[2]
end_city = sys.argv[3]

# open the file
f = open(text_file)

# make a graph of the nodes
city_dict = {}
for line in f:
    if line != "END OF INPUT":
        ind_line = line.split()
        if ind_line[0] in city_dict:
            city_dict[ind_line[0]].append([ind_line[1], ind_line[2]])
        if ind_line[1] in city_dict:
            city_dict[ind_line[1]].append([ind_line[0], ind_line[2]])
        if (ind_line[0] not in city_dict):
            city_dict[ind_line[0]] = [[ind_line[1], ind_line[2]]]
        if (ind_line[1] not in city_dict):
            city_dict[ind_line[1]] = [[ind_line[0], ind_line[2]]]
    else:
        break


# base cases
if (start_city not in city_dict) or (end_city not in city_dict):
    print("error: city not included in the input")
    sys.exit(-1)    
elif (start_city == end_city):
    print("distance: 0 km\nroute:\nnone")
    sys.exit()

count = 1
lengths = []

# fringe queue
fringe = PriorityQueue()

fringe.put((0, start_city, [start_city])) # put in the start city

#implements uniform cost search
start = time.time()
while fringe.qsize() > 0:
    zeroeth = fringe.get()
    dist = zeroeth[0]
    curr_city = zeroeth[1]
    path = zeroeth[2]
    
    # ends loop
    if curr_city == end_city:
        print_path(dist, path)
        sys.exit()

    values = city_dict[zeroeth[1]]

    for i in range(len(values)):
        new_val = int(values[i][1]) + zeroeth[0]
        fringe.put((new_val, values[i][0], path + [values[i][0]])) # adds the current path as well
        count += 1

    # no path
    if time.time() - start > 5:
        print("distance: infinity\nroute:\nnone")
        sys.exit()