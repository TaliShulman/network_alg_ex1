import networkx as nx
import random
import matplotlib.pyplot as plt

#question 1_a
def create_ws_graph(n, k, p) :
    G = nx.Graph()
    G.add_nodes_from(range(n))
    
    #add k edges to each vertice
    for i in range(n):
        for j in range(1, k // 2 + 1):
            G.add_edge(i, (i + j) % n)
            
                 
    for i in range(n):
        for j in range(1, k // 2 + 1):
            v = (i + j) % n

            if random.random() < p:
                candidates = [
                    node for node in range(n)
                    if node != i and not G.has_edge(i, node)
                ]

                if candidates:
                    new_node = random.choice(candidates)
                    G.remove_edge(i, v)
                    G.add_edge(i, new_node)
                    
    return G

#question 1_b
def calc_clustering_coeff(G):
    #c_i = 2* #numb of edges between the neighbors) / k_i * (k_i -1)
    coefficients = []

    for node in G.nodes():
        neighbors = list(G.neighbors(node))
        k = len(neighbors)

        if k < 2:
            coefficients.append(0)
            continue

        subgraph = G.subgraph(neighbors)
        e = subgraph.number_of_edges()

        c_i = (2 * e) / (k * (k - 1))
        coefficients.append(c_i)

    return sum(coefficients) / len(coefficients)


#test for q_1b
# G = create_ws_graph(20, 4, 0.3)

# my_coeff = calc_clustering_coeff(G)
# nx_coeff = nx.average_clustering(G)

# print("My coefficient:", my_coeff)
# print("NetworkX coefficient:", nx_coeff)


#delete later

# call the function here
# G = create_ws_graph(10, 4, 0.2)
# print(G.number_of_nodes())
# print(G.number_of_edges())  
# print(G.nodes())
# print(G.edges())

# def test_ws_graph():
#     n = 10
#     k = 4

#     # p = 0: regular ring lattice
#     G = create_ws_graph(n, k, 0)

#     assert G.number_of_nodes() == n
#     assert G.number_of_edges() == n * k // 2

#     # Every node should have degree k
#     assert all(degree == k for _, degree in G.degree())

#     assert nx.is_connected(G)

#     print("Test 1 passed: p=0")

#     # p = 1: rewiring is attempted for every original edge
#     G = create_ws_graph(n, k, 1)

#     assert G.number_of_nodes() == n
#     assert G.number_of_edges() == n * k // 2

#     assert nx.number_of_selfloops(G) == 0

#     print("Test 2 passed: p=1")

#     print("All tests passed!")
    
# test_ws_graph()   

# def draw_ws_graph(G, title):
#     pos = nx.circular_layout(G)

#     nx.draw(
#         G,
#         pos,
#         with_labels=True,
#         node_color="lightblue",
#         node_size=600,
#         edge_color="gray",
#         font_size=10
#     )

#     plt.title(title)
    
# n = 20
# k = 4

# # Initial ring lattice (p = 0)
# G1 = create_ws_graph(n, k, 0)

# # Graph after rewiring (p = 0.3)
# G2 = create_ws_graph(n, k, 0.3)

# plt.figure(figsize=(12, 5))

# plt.subplot(1, 2, 1)
# draw_ws_graph(G1, "Before rewiring (p=0)")

# plt.subplot(1, 2, 2)
# draw_ws_graph(G2, "After rewiring (p=0.3)")

# plt.tight_layout()
# plt.show()  