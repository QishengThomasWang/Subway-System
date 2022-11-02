import time
from Graph import Graph


class AStar:

    def __call__(self, graph : Graph, start : int, stop : int):
        start_time = time.time()

        # Required resources for running algorithm
        OPEN = set([start])
        CLOSE = set([])
        h = graph.a_star_heuristic(start)
        self.comparisons = 0
        length = 0

        # Dictionary for distance to nodes
        distances = {}
        distances[start] = 0

        # Dictionary for adjacent nodes
        adjancencies = {}
        adjancencies[start] = start

        # Check all nodes connected
        while len(OPEN) > 0:
            n = None

            # Select closes to goal node
            for x in OPEN:
                if (n == None) or (distances[x] + h[x] < distances[n] + h[n]):
                    n = x
                self.comparisons += 1
            
            # If no nodes to select, no path
            if n == None:
                print("NO PATH")
                return self.comparisons()

            # If you've reached the goal, generate the path
            if n == stop:
                self.path = []

                while adjancencies[n] != n:
                    self.path.append(n)
                    n = adjancencies[n]

                self.path.append(start)

                self.path.reverse()

                end_time = time.time()
                total_time = end_time-start_time
                print('A* found the following path with a length of ' + str(distances[stop]) +' in ' + str(total_time) + 's.')
                print(self.get_path())
                return (self.get_comparisons(), total_time)
            
            # Add all neighbours not in OPEN to OPEN
            for m in graph.get_neighbours(n):

                if m not in OPEN and m not in CLOSE:
                    OPEN.add(m)
                    adjancencies[m] = n
                    distances[m] = distances[n] + graph.graph[m][1]
                else:
                    if distances[m] > distances[n] + graph.graph[m][1]:
                        distances[m] = distances[n] + graph.graph[m][1]
                        adjancencies[m] = n

                        if m in CLOSE:
                            CLOSE.remove(m)
                            OPEN.add(m)
                    self.comparisons += 1
                self.comparisons += 1

            OPEN.remove(n)
            CLOSE.add(n)

        print("NO PATH")
        return self.comparisons()

    def get_path(self):
        return self.path

    def get_comparisons(self) -> int:
        return self.comparisons
