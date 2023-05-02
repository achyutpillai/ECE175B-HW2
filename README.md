# HW 2 Problem 3

This code will create a bayesian network given inputs from the user and determine conditional independence
for any given nodes.

Libraries Used: pyAgrum, string, networkx, matplotlib.pyplot
        - pyAgrum and networkx will most likely need to be installed

Steps:
  - Make sure all libraries are installed before running the code
  - Answer all the user prompts correctly (i.e. how many nodes are in the network, ...)
  - After inputting all the information regarding the bayesian network, a visual representation will
    be shown.
  - If the network is correct close the bayesian network's plot window and continue
    answering the prompts. If it is incorrect restart the code and make sure you have
    inputted your bayesian network correctly
  - After closing the window, input all the information regarding what nodes you want
    check for conditional independence.
  - The program will determine if the two nodes the user gave for independence are independent
    given the nodes the user gave.
  - The program will then prompt the user if they want to find more conditional independences
  - If the user selects no, the program will end
