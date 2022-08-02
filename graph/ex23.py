import sys 

import matplotlib.pyplot as plt 
from networkx import nx 

n = 10  # 10 nodes
m = 20  # 20 edges

G = nx.gnm_random_graph(n, m)

# some properties
print("node degree clustering")
for v in nx.nodes(G):
    print('%s %d % f' % (v, nx.degree(G, v), nx.clustering(G, v)))

# print the adjacency list to terminal
try:
    nx.write_adjlist(G, sys.stdout)
except TypeError:   # Python 3.x
    nx.write_adjlist(G, sys.stdout.buffer)

nx.draw(G, with_labels=True)
plt.show()
