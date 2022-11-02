from Dijkstra import *
from GraphBuilder import *
from AStar import *
import matplotlib.pyplot as plt
import numpy as np

# Generate the Graph
factory = Maker()
graph_builder = factory.make('london')
graph = graph_builder.build('_dataset/')

# For labeling the metric graph
path_names = ['Long', 'Mid', 'Short']

# Benchmarked paths
paths = []
paths.append([1,152]) #longest path
paths.append([1,281]) #normal path
paths.append([1,52]) #single edge

# Algorithms for calling
dijkstra = Dijkstra()
astar = AStar()

# Lists for storing algorithm results
dijkstra_comparison_results = []
astar_comparison_results = []

# Calls for benchmarking algorithms
for x in paths:
    dijkstra_comparison_results.append(dijkstra(graph, x[0], x[1])[0])
    astar_comparison_results.append(astar(graph, x[0], x[1])[0])

# PLotting benchmark graph
X = np.arange(3)
fig = plt.figure()
ax = fig.add_axes([0.12, 0.12, 0.88, 0.88])
ax.bar(X + 0.00, dijkstra_comparison_results, color = 'b', width = 0.25, edgecolor = 'grey', label = 'Dijkstra')
ax.bar(X + 0.25, astar_comparison_results, color = 'r', width = 0.25, edgecolor = 'grey', label = 'A*')
plt.xlabel('Path', fontweight = 'bold', fontsize = 10)
plt.ylabel('Total Comparisons', fontweight = 'bold', fontsize = 10)
plt.xticks([r + 0.25 for r in range(len(dijkstra_comparison_results))], path_names)
plt.title('Comparisons for Shortest Path')
for i in range(len(dijkstra_comparison_results)):
    plt.text(i - 0.1, dijkstra_comparison_results[i] + 100, dijkstra_comparison_results[i])
    plt.text(i + 0.2, astar_comparison_results[i] + 100, astar_comparison_results[i])
plt.legend()
plt.show()