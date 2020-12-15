import networkx as nx
from functions import *
from algorithms import prims_algorithm
from drawing import *

print ('------------------------------------------------------------------------------------------')
print ("This program implements Prim's Algorithm to solve the minimum weight spanning tree problem")
print ("---------------------Choose from 3 different graphs to see its details--------------------")
print ('------------------------------------------------------------------------------------------')
print ('Enter 1 for Graph 1')
print ('Enter 2 for Graph 2')
print ('Enter 3 for graph 3')

correctChoice = False
while correctChoice == False:
    try:
        userChoice = int(input('Please choose a graph to look at: '))
        if userChoice in range(1, 5):
            txtFile = f'test-graphs/G{userChoice}.txt'
        else:
            raise Exception("Please enter number between 1 - 4")
        correctChoice = True
    except:
        print("Please enter only numbers between 1 - 4")


graph_data = open(txtFile, 'r')

G = nx.read_weighted_edgelist(graph_data, nodetype = int)

T = prims_algorithm(G, 0, userChoice, True, True)