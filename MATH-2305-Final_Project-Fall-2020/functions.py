import networkx as nx

def V(G):
    """
    Returns a set of verticies on a graph
    
    Parameters
    ----------
    G = A networkx graph.

    Returns
    -------
    set of vertices belonging to graph 'G'
    """
    return set(G.nodes())

def E(G):
    """
    Returns a set of edges on a graph
    
    Parameters
    ----------
    G = A networkx graph.
    
    Returns
    -------
    
    set of edges belonging to graph graph

    """
    return set(G.edges())


def prims_initialize(graph, v):
    
    """
    Returns a subgraph while making sure the vertex is found on the graph.
    
    Parameters
    ----------
    graph = A networkx graph.
    v = int value of a vertex

    Returns
    -------
    T a subgraph of G. Including nodes, edges and weights.
    """
    if v not in V(graph):
        return 'Error vertex not found'
    else:
        T = nx.Graph()
        T.add_node(v)
        return T


def cost(graph,e):
    
    """
    Return the cost of an edge on a graph.
    
    
    Parameters
    ----------
    G = A networkx graph.
    e = An edge on graph.
    
    Returns
    -------
    The weight of an edge 'e' on a graph 'graph'.

    """
    return graph.edges[e]['weight']


def is_spanning(graph, subgraph):
     """
     Return True or False by passing graph and subgraph through function V 
     to check if the subgraph uses all verticies of the original graph
    
     Parameters
     ----------
     graph = A networkx graph.
     subgraph = A networkx subgraph of 'graph'.
        
     Returns
     -------
     True if the subgraph is spanning.
     False if the subgraph is not spanning.
     """
    
     return V(graph) == V(subgraph)


def incident_edges(G, T):
     """
     Returns the valid incident edges.
     
     An incident edge is an edge that is adjacent to the node that is
     being evaluated. An edge is valid when both endpoints are not not already in
     the set containting tree nodes.
    
     Parameters
     ----------
     G = A networkx graph.
     T = A networkx subgraph of 'graph'.
        
     Returns
     -------
     A set of valid incident edges.
     """
     return [e for e in list(G.edges(V(T)))
                 if e[0] not in V(T) or e[1] not in V(T)]


def min_prims_edge(G, T):
     """
     Return the minimum cost incident edge from a set created by the incident_edge
     function. Uses the cost function to determine the minimum cost edge.
    
     Parameters
     ----------
     G = A networkx graph.
     T = A networkx subgraph of 'graph'.
        
     Returns
     -------
     The weight of an edge 'e' on a graph 'graph'.
     """
     possible_e = incident_edges(G,T)
     min_e = possible_e[0]              
     for e in possible_e:
        if cost(G,e) < cost(G,min_e):
            min_e = e
     return min_e


