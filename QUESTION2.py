import networkx as nx
import random
import matplotlib.pyplot as plt

#question 2_a
def deg_centrality(G):
    #returns normalized deg centarlity for each node
    n = G.number_of_nodes()
    return {node: degree / (n - 1) for node, degree in G.degree()} 

def betweenness_centrality(G):
    nodes = list(G.nodes())
    n = len(nodes)

    betweenness_centrality = {node: 0 for node in nodes}

    for i in range(n):
        for j in range(i + 1, n):
            s = nodes[i]
            t = nodes[j]

            paths = list(nx.all_shortest_paths(G, s, t))

            for path in paths:
                for node in path[1:-1]: #i =/= s or t
                        betweenness_centrality[node] += 1 / len(path)
                        
    normalization = 2 / ((n - 1) * (n - 2))

    return {
        node: value * normalization
        for node, value in betweenness_centrality.items()
    }


def closeness_centrality(G):
    n = G.number_of_nodes()
    return {
        node: (n - 1) / sum(nx.single_source_shortest_path_length(G, node).values()) for node in G.nodes()
    }
    
# assert all(
#     abs(closeness_centrality(G)[node] -
#         nx.closeness_centrality(G)[node]) < 1e-9
#     for node in G.nodes()
# )

G = nx.gnp_random_graph(22, 0.3)

my_bc = betweenness_centrality(G)
nx_bc = nx.betweenness_centrality(G)

assert all(
    abs(my_bc[node] - nx_bc[node]) < 1e-9
    for node in G.nodes()
)  