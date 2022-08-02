# Authors:  Drew Conway <drew.conway@nyu.edu>, Aric Hagberg <hagberg@lanl.gov>

from collections import defaultdict

import matplotlib.pyplot as plt
import networkx as nx
import numpy
from scipy.cluster import hierarchy
from scipy.spatial import distance


def create_hc(G):
    """Creates hierarchical cluster of graph G from distance matrix"""
    path_length = nx.all_pairs_shortest_path_length(G)
    distances = numpy.zeros((len(G), len(G)))
    for u, p in path_length:
        for v, d in p.items():
            distances[u][v] = d
    # Create hierarchical cluster
    Y = distance.squareform(distances)
    Z = hierarchy.complete(Y)  # Creates HC using farthest point linkage
    # This partition selection is arbitrary, for illustrive purposes
    membership = list(hierarchy.fcluster(Z, t=1.15))
    # Create collection of lists for blockmodel
    partition = defaultdict(list)
    for n, p in zip(list(range(len(G))), membership):
        partition[p].append(n)
    return list(partition.values())


if __name__ == '__main__':
    G = nx.read_edgelist("hartford_drug.edgelist")

    # Extract largest connected component into graph H
    H = next(nx.connected_component_subgraphs(G))
    # Makes life easier to have consecutively labeled integer nodes
    H = nx.convert_node_labels_to_integers(H)
    # Create parititions with hierarchical clustering
    partitions = create_hc(H)
    # Build blockmodel graph
    BM = nx.quotient_graph(H, partitions, relabel=True)

    # Draw original graph
    pos = nx.spring_layout(H, iterations=100)
    plt.subplot(211)
    nx.draw(H, pos, with_labels=False, node_size=10)

    # Draw block model with weighted edges and nodes sized by number of internal nodes
    node_size = [BM.nodes[x]['nnodes'] * 10 for x in BM.nodes()]
    edge_width = [(2 * d['weight']) for (u, v, d) in BM.edges(data=True)]
    # Set positions to mean of positions of internal nodes from original graph
    posBM = {}
    for n in BM:
        xy = numpy.array([pos[u] for u in BM.nodes[n]['graph']])
        posBM[n] = xy.mean(axis=0)
    plt.subplot(212)
    nx.draw(BM, posBM, node_size=node_size,
            width=edge_width, with_labels=False)
    plt.axis('off')
    plt.show()
