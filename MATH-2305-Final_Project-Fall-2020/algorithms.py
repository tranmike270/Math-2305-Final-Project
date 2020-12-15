# Michael Tran
# MATH 2305
# Final Project (Prims Algorithm)


from drawing import show_weighted_graph, draw_subtree
from functions import prims_initialize, min_prims_edge, is_spanning, cost, E


def prims_algorithm(G, starting_vertex, userChoice, draw = False, detail = False):
     """
     Returns minimum spanning subtree of graph 'G'. Displays every iteration 
     as an algorithm constructs a subtree. After the last iteration, an 
     algorithm displays the vertices V(T), edges E(T), and total cost of subtree.

     Parameters
     ----------
     G = A networkx graph.
     starting_vertex = A node on 'G'.
     userChoice = user's choice on which graph to look at 1 - 4
     draw = A bool value.
     detail = A bool value.
    
     Returns
     -------
     T a subgraph of G. Including nodes, edges and weights.
     """
    
     T = prims_initialize(G, starting_vertex)
     if draw == True:
        draw_subtree(G,T)
        
     while is_spanning(G, T) == False:
        e = min_prims_edge(G,T)
        T.add_edge(e[0],e[1])
        if draw == True:
            draw_subtree(G,T)
    
     if detail == True:
        total_cost = sum([cost(G, e) for e in E(T)])
        print(f'----------------------------------------Tree {userChoice} Details-------------------------------------')
        print ('------------------------------------------------------------------------------------------')
        print(f'V({userChoice}) = {list(T.nodes())}')
        print(f'E({userChoice}) = {list(T.edges())}')
        print(f'Total Cost = {total_cost}')
        print ('------------------------------------------------------------------------------------------')
        print ('------------------------------------------------------------------------------------------')
     return T

