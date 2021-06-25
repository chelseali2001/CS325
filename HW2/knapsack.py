# Citations:
# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/

import random
import time

# Dynamic programming method
def dp(val, wt, W, n):
  # Creating an empty table
  table = []
  for x in range(n + 1):
    table.append([])
    
    for i in range(W + 1):
      table[x].append(0)
  
  # Adding values into the table from the bottom up
  for x in range(n + 1):
    for y in range(W + 1):
      if x == 0 or y == 0: # Set the values of the first row or column to 0
        table[x][y] = 0
      elif wt[x - 1] <= y: # Check if the weight of the nth item is less than the capacity of column y
        # Finding the total weight when the nth item is added
        # If the nth item helps increase the total weight without exceeding the max weight, it will be added.
        # Otherwise, it will not be included
        if table[x - 1][y] < val[x - 1] + table[x - 1][y - wt[x - 1]]:
          table[x][y] = val[x - 1] + table[x - 1][y - wt[x - 1]]
        else:
          table[x][y] = table[x - 1][y]
      else:
        table[x][y] = table[x - 1][y] # Setting the current value with the previous one
  
  # Return the maximum possible weight
  return table[n][W]

# Recursion method
def rec(val, wt, W, n):
  if W == 0 or n == 0: # If the weight or number of values is 0
    return 0
  elif (wt[n - 1] > W): # If the weight of the current item will exceed the max weight, it will not be added
    return rec(val, wt, W, n - 1)
  else:
    # Finding the total weight when the nth item is added
    # If the nth item helps increase the total weight without exceeding the max weight, it will be added.
    # Otherwise, it will not be included
    return max(rec(val, wt, W, n - 1), val[n - 1] + rec(val, wt, W - wt[n -1], n - 1))

# Starting values
val = [50, 120, 100, 60, 75, 63, 56, 89, 90, 170]
wt = [10, 20, 30, 25, 1, 65, 39, 86, 97, 23]
W = 100
n = 10

# Trying 7 test cases
for x in range(7):
  # Collecting the runtime of the recursion method
  recTime = time.time()
  maxRec = rec(val, wt, W, n) # Running the recursion method
  recTime = time.time() - recTime
  
  # Collecting the runtime of the Dynamic programming method
  dpTime = time.time()
  maxdp = dp(val, wt, W, n) # Running the Dynamic programming method
  dpTime = time.time() - dpTime
  
  # Printing the results
  print("N =", n, " W =", W, " Rec time =", recTime, " DP time =", dpTime, " max Rec =", maxRec, " max DP =", maxdp)

  # Generating more random values for a new test case
  for i in range(5):
    val.append(random.randint(50, 200))
    wt.append(random.randint(1, 100))
  
  n += 5