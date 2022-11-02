from abc import ABCMeta
from Graph import *

class GraphBuilderFactory(metaclass=ABCMeta):
    def factory(self):
        """ Interface Method"""
    
class GraphBuilder(metaclass=ABCMeta):
    def build(self):
        """ Interface Method"""

class Maker(GraphBuilderFactory):
    def make(self, type : str):
        #type is form of data, currently only given london, can make more as need be.
        if type == "london":
            return London()
        else:
            print("No such graph type!")
            return None

class London(GraphBuilder):
    def build(self, file_location : str) -> Graph:

        #Determine the length of the graph for building
        reader = open(file_location + 'london.stations.csv')
        length = 0
        counter = ' '
        while counter != '':
            length += 1
            counter = reader.readline()
        graph = Graph(length-1)
        reader.close()

        #Get files open for building
        station_file = open(file_location + 'london.stations.csv')
        line_file = open(file_location + 'london.lines.csv')
        connection_file = open(file_location + 'london.connections.csv')

        #Initialize stations
        station_file.readline()
        for x in range(graph.V):
            info = station_file.readline().strip().split(',')
            if info != ['']:
                #Following is column indecies for station information
                # ID = 0
                # Latitude = 1
                # Longitude = 2
                # Name = 3
                # Display Name = 4
                # Zone = 5
                # Total Lines = 6
                # Rail = 7
                station = Station(info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7])
                graph.add_station(station)

        #Initialize Connections
        connection_file.readline()
        x = 0
        while x > -1:
            info = connection_file.readline().strip().split(',')
            if info != ['']:
                #Following is column indecies for connection information
                # station 1 = 0
                # station 2 = 1
                # line = 2
                # time = 3
                graph.add_edge(int(info[0]), int(info[1]), int(info[2]), int(info[3]))
            else: break

        return graph