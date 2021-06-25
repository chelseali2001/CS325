# Works Cited: https://www.programiz.com/dsa/prim-algorithm

import math
import sys

# Minimum spanning tree (mst) function (based off of Prim's Algorithm)
def mstAlg(graph, n):
  chosen = []
  total = 0
  
  # Creating an array of boolean indicating which path is chosen
  for x in range(n):
    chosen.append(False)
  
  chosen[0] = True # Make the first vertex true
  
  # Going through all of the edges
  for j in range(n - 1):
    minimum = sys.maxsize
    coord = [0, 0]
    
    # Going through all of the vertices
    for x in range(n):
      # Getting the adjacent verticies to the chosen vertex
      if chosen[x]:
        for i in range(n):
          # If the vertex isn't chosen yet and it isn't the current vertex itself
          if not chosen[i] and graph[x][i]:
            # If the path is less than the current minimum
            if minimum > graph[x][i]:
              minimum = graph[x][i]
              coord[0] = x
              coord[1] = i

    # Adding the weight of the chosen path to the total
    total += graph[coord[0]][coord[1]]
    chosen[coord[1]] = True
  
  # Returning the total weight of the MST
  return total
  
# Open graph.txt file
fileText = open('graph.txt', 'r')
testCases = int(fileText.readline()) # Getting the number of test cases

# Going through all of the test cases
for x in range(testCases):
  data = int(fileText.readline()) # Getting the number of points (vertices) on the graph
  points = []
  
  # Collecting each point
  for i in range(data):
    points.append([])
    temp = fileText.readline().split(" ")
    points[i].append(int(temp[0]))
    points[i].append(int(temp[1]))
  
  graph = []
  
  # Creating an empty adjacency table
  for i in range(data):
    graph.append([])
    
    for j in range(data):
      graph[i].append(0)
  
  # Adding values to the adjacency table
  for i in range(data):
    for j in range(i + 1, data):
      # Calculating the distance between two points
      distance = int(round(math.sqrt(math.pow((points[i][0] - points[j][0]), 2) + math.pow((points[i][1] - points[j][1]), 2))))
      graph[i][j] = distance
      graph[j][i] = distance
  
  # Printing out the results
  message = "Test case " + str(x + 1) + ": MST weight " + str(mstAlg(graph, data))  
  print(message, "\n")