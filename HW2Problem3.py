import pyAgrum as gum
import string
import networkx as nx
import matplotlib.pyplot as plt


def main():
    bn = gum.BayesNet("Bayesian Network")

    #list of uppercase letters
    alphabet = list(string.ascii_uppercase)

    #Asks user for information
    numNodes = int(input("Enter the number of nodes in the Bayesian Network: "))
    nameNodesBool = input("Would you like to name the nodes yourself? (Y/N): ")

    #checking for misinput
    while(nameNodesBool != 'Y') and (nameNodesBool != 'y') and (nameNodesBool != 'N') and (nameNodesBool != 'n'):
        print("That is not a valid input")
        nameNodesBool = input("Would you like to name the nodes yourself? (Y/N): ")

    # Allows user to choose the names of its nodes or chooses
    # them from the alphabet
    #node names are stored in a list
    nodeNames = []
    if(nameNodesBool == 'Y' or nameNodesBool == 'y'):
        for i in range(numNodes):
            temp = input("Name of Node " + str(i+1) + ": ")
            nodeNames.append(temp)
        print("Node names are " + str(nodeNames))
    else:
        for i in range(numNodes):
            nodeNames.insert(i, alphabet[i])
        print("Node names are " + str(nodeNames))

    nodes = []
    for i in nodeNames:
        nodes.append(bn.add(i, 2))
    #Asks user for number of edges in Bayesian Network
    numEdges = int(input("How many edges are present in the Bayesian Network?: "))


    #Using the number and type of edges, creates the Bayesian Network
    edges = [(None,None) for x in range(numEdges)]
    for i in range(numEdges):
        while True:
            print("\nWhat nodes are connected in Edge " + str(i+1) + "?")
            tNode = input("Tail Node: ")
            hNode = input("Head Node: ")
            if(hNode in nodeNames) and (tNode in nodeNames):
                break
            print("One or more of these nodes are not valid")
        head = nodeNames.index(hNode)
        tail = nodeNames.index(tNode)
        #stores each edge with Head and Tail defined
        edges[i] = (tail, head)

    #adds edges to bayesian network
    for edge in edges:
        bn.addArc(*edge)



    #Visual Representation of Bayesian Network
    G = nx.DiGraph()
    G.add_edges_from(edges)
    mapping = {v : k for v, k in enumerate(nodeNames)}
    G = nx.relabel_nodes(G, mapping)
    nx.draw(G, with_labels = True)
    #prints out the bayesian network so user can confirm if it is correct
    plt.show()


    #Checks for conditional independence of two nodes given any nodes
    while True:
        print("\nWhat nodes do you want to check for conditional independence?")
        A = input("Node 1: ")
        B = input("Node 2: ")
        while True:
            try:
                numGiven = int(input("How many given nodes?: "))
                break
            except ValueError:
                print("Not a valid number")
        given = []
        #stores given nodes in a list
        for x in range(numGiven):
            given.append(input("Given Node: "))
        #uses function to check for conditional independence following the d-separation rules
        if bn.isIndependent(A,B,given):
            print(str(A) + " and " + str(B) + " are conditionally independent given " + str(given) + "\n")
        else:
            print(str(A) + " and " + str(B) + " are NOT conditionally independent given " + str(given) + "\n")
        quit = input("Do you want to find another conditional independence? (Y/N): ")
        if (quit == 'N') or (quit =='n'):
            break

    #conditional probability code
    #receiving local conditional probabilities
#    while True:
#        findProbBool = input("Do you want to find any conditional probabilities? (Y/N): ")
#        if (findProbBool == 'n') or (findProbBool == 'N'):
#            break
#        print("Input all local probabilities")
#
#        for node in nodeNames:
#            prob = []
#            parentsWithChild = ((bn.cpt(node).names))
#            if(len(parentsWithChild) > 1):
#                for i in range(2**len(parentsWithChild)):
#                    binary = str((bin(i).replace("0b", "")).zfill(len(parentsWithChild)))
#                    line = "P(" + str(parentsWithChild[0]) + "=" + str(binary[0]) + "| "
#                    for k in range(len(parentsWithChild)-1):
#                        line = line + parentsWithChild[k+1] + "=" + str(binary[k+1])
#                        if(k+2 != len(parentsWithChild)):
#                            line = line + ", "
#                    line = line + ") = "
#                    prob.append(float(input(line)))
#
#                    idx = []
#                    for k in range(len(binary) -1, -1, -1):
#                        idx.append(int(binary[k]))
#                    idx = tuple(idx)
#                    bn.cpt(parentsWithChild[0])[idx] = prob[i]
#            else:
#                prob.append(float(input("P("+ str(parentsWithChild[0]) + "=0) = ")))
#                prob.append(float(input("P(" + str(parentsWithChild[0]) + "=1) = ")))
#                bn.cpt(parentsWithChild[0])[0] = prob[0]
#                bn.cpt(parentsWithChild[0])[1] = prob[1]
#            print(bn.cpt(parentsWithChild[0]))

main()
