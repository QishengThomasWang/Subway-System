from json.encoder import INFINITY
import time
from Graph import *
from PriorityQueue import PriorityQueue

class Dijkstra:

    def __call__(self, graph : Graph, s : int, e : int):
        start_time = time.time()
        
        # Required resources to run algortihm
        self.graph = graph
        self.distTo = [INFINITY] * (self.graph.V+1)
        self.edgeTo = [None] * (self.graph.V+1)
        self.pq = PriorityQueue()
        self.e = e
        self.s = s
        self.comparisons = 0

        self.distTo[self.s] = 0

        # Begin algorithm at start node
        self.pq.insert(self.s)
        self.pq.insert(0)
        while not self.pq.isEmpty():
            self.relax(self.pq.deleteMin())

        # Output
        end_time = time.time()
        total_time = end_time-start_time
        print('Djikstra\'s found the following path with a length of ' + str(self.distTo[self.e]) + ' in ' + str(total_time) +'s.')
        print(self.get_path())
        return (self.get_comparisons(), total_time)

    # def relax(self, v : int):
    #     e = self.graph.graph[v]
    #     if self.graph.graph[e] != None:
    #         w = self.graph.graph[e]
    #         while w[0].next != None:
    #             if self.distTo[w[0].id] > self.distTo[v] + w[1]:
    #                 self.distTo[w[0].id] = self.distTo[v] + w[1]
    #                 self.edgeTo[w[0].id] = e
    #                 if not self.pq.contains(w[0].id):
    #                     self.pq.insert(w[0].id)
    #             w = w[0].next
    #         if self.distTo[w[0].id] > self.distTo[v] + w[1]:
    #                 self.distTo[w[0].id] = self.distTo[v] + w[1]
    #                 self.edgeTo[w[0].id] = e
    #                 if not self.pq.contains(w[0].id):
    #                     self.pq.insert(w[0].id)
    
    def relax(self, v : int):
        # Textbook implementation of Dijkstra's algorithm
        e = self.graph.graph[v]
        while e != None:
            w = e[0].id
            if self.distTo[w] > self.distTo[v] + e[1]:
                self.distTo[w] = self.distTo[v] + e[1]
                self.edgeTo[w] = v
                if not self.pq.contains(w):
                    self.pq.insert(w)
            e = e[0].next
            self.comparisons += 1
    
    def get_path(self):
        # For output
        path = [self.e]
        n = self.e
        while n != self.s:
            path.append(self.edgeTo[n])
            n = self.edgeTo[n]
        path.reverse()
        return path

    def get_comparisons(self):
        return self.comparisons