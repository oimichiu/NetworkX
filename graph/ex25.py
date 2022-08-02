import networkx as nx 
from networkx.generators.atlas import graph_atlas_g

atlas = graph_atlas_g()[0:20]

for G in atlas:
    print("graph %s has %d nodes with %d edges"
            % (G.name, nx.number_of_nodes(G), nx.number_of_edges(G)))
    A = nx.nx_agraph.to_agraph(G)
    A.graph_attr['label'] = G.name
    # set default node attributes
    A.node_attr['color'] = 'red'
    A.node_attr['style'] = 'filled'
    A.node_attr['shape'] = 'circle'
    A.write(G.name + '.dot')