import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
G.add_node("a")
G.add_nodes_from(["b","c"])

G.add_edge(1,2)
edge = ("d", "e")
G.add_edge(*edge)
edge = ("a", "b")
G.add_edge(*edge)

G.add_edges_from([("a","c"),("c","d"), ("a",1), (1,"d"), ("a",2)])

print("Nodes of graph: ")
print(G.nodes())
print("Edges of graph: ")
print(G.edges())

nx.draw(G)
plt.savefig("simple_path.png") # save as png
plt.show() # display