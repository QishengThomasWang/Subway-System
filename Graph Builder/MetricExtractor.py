from Graph import Graph
import matplotlib.pyplot as plt


class createGraph:

    def __init__(self, graph : Graph):
        self.graph = graph

    def create_axis(self):
        # Straight forward extraction of node degrees
        # Then display as a graph
        degree = []
        x_axis = []
        y_axis = []
        for x in range(len(self.graph.graph) - 1):
            temp = []
            y = self.graph.graph[x]
            if y != None:
                while y[0].next != None:
                    variable = int(y[0].id)
                    temp.append(variable)
                    y = y[0].next
                variable = int(y[0].id)
                temp.append(variable)
                degree.append(len(temp))

        for i in range(1, max(degree) + 1):
            x_axis.append(i)

        for i in range(1, max(degree) + 1):
            count = 0
            for j in range(len(degree) + 1):
                if degree[j - 1] == i:
                    count += 1
            y_axis.append(count)

        return[x_axis,y_axis]

    def make_plot(self): 
        axis = self.create_axis()
        plt.xlabel('degrees')         
        plt.ylabel('number of nodes')   
        plt.bar(axis[0],axis[1])
        plt.show()