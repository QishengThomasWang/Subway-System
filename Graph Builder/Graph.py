from cmath import sqrt
from numbers import Real


class Node:
    def __init__(self, id):
        self.id = id
        self.next = None

class Station:

    def __init__(self, id, latitude, longitude, n, dn, z, l, r):
        # Stores all given data on stations
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.name = n
        self.display_name = dn
        self.zone = z
        self.lines = l
        self.rail = r

class Graph:

    def __init__(self, num):
        self.V = num
        self.graph = [None] * (num+1)
        self.station_list = [None] * (num+1)

    def add_edge(self, one : int, two : int, weight : int, info : int):
        #one is first station
        #two is second station
        #weight is time
        #info is line

        #Add appropriate adjacency list information
        node = Node(two)
        node.next = self.graph[one]
        self.graph[one] = (node, weight, info)

        node = Node(one)
        node.next = self.graph[int(two)]
        self.graph[two] = (node, weight, info)

    def add_station(self, station : Station):
        self.station_list[int(station.id)] = station

    def print_AL(self):
        # Print the adjacency list, for verification purposes
        for x in range(len(self.graph)-1):
            y = self.graph[x]
            print(str(x+1) + ": ", end='')
            if y != None:
                while y[0].next != None:
                    print(str(y[0].id+1) + ", ", end='')
                    y = y[0].next
                print(y[0].id+1)
            else: print("None")

    def get_neighbours(self, target : int):
        # Find all adjacent nodes of requested node
        neighbours = set()
        x = self.graph[target]
        if x != None:
            while x[0].next != None:
                neighbours.add(x[0].id)
                x = x[0].next
            neighbours.add(x[0].id)
        return list(neighbours)

    def a_star_heuristic(self, target : int):
        # Calculates and lists all the distances from nodes to goal node for A*
        H = [None] * (self.V+1)
        for x in range(self.V+1):
            if self.station_list[x] != None:
                h = (float(self.station_list[x].longitude) - float(self.station_list[target].longitude)) ** 2
                h += (float(self.station_list[x].latitude) - float(self.station_list[target].latitude)) ** 2
                h = sqrt(h).real
                H[x] = h
        return H
