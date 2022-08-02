import sys

import matplotlib.pyplot as plt
import networkx as nx 

G = nx.grid_2d_graph(5, 5)
try:
    nx.write_adjlist(G, sys.stdout)
except TypeError:
    nx.write_adjlist(G, sys.stdout.buffer)

nx.write_edgelist(G, path="grid.edgelist", delimiter=":")
H = nx.read_edgelist(path="grid.edgelist", delimiter=":")

nx.draw(H)
plt.show()