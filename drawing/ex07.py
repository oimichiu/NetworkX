import matplotlib.pyplot as plt 
import networkx as nx 

try:
    import pygraphviz
    from networkx.drawing.nx_agraph import graphviz_layout
except ImportError:
    try:
        import pydot
        from networkx.drawing.nx_pydot import graphviz_layout
    except ImportError:
        raise ImportError("This example need Graphviz and either"
                        "PyGraphviz or pydot")

G = nx.balanced_tree(3, 5)
pos = graphviz_layout(G, prog='twopi', args='')
plt.figure(figsize=(8,8))
nx.draw(G, pos, node_size=20, aplha=0.5, node_color="blue", with_labels=False)
plt.axis('equal')
plt.show()