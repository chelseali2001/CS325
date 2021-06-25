# Citation
# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
# https://www.geeksforgeeks.org/printing-items-01-knapsack/

# Dynamic programming solution
def dp(val, wt, W, n):
  # Creating an empty table
  table = []
  for x in range(n + 1):
    table.append([])
    
    for i in range(W + 1):
      table[x].append(0)
      
  fam = []
  
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
  
  maxWeight = table[n][W]
  temp = W
  
  # Printing the items needed to get the max weight
  for x in range(n, 0, -1):
    # Checking if the value is included in the max weight
    if maxWeight > 0 and maxWeight != table[x - 1][temp]:
      fam.append(x)
      
      # Reducing the total weight
      maxWeight -= val[x - 1]
      temp -= wt[x - 1]
  
  fam.sort() # Sorting the order of the items
  fam.insert(0, table[n][W]) # Adding the max weight to the beginning of the list
  
  # Return the maximum possible weight
  return fam

# Open data.txt file
fileText = open('shopping.txt', 'r')
text = fileText.readlines()

testCases = int(text[0]) # Getting the number of test cases
line = 1

# Going through all of the test cases
for x in range(testCases):
  val = []
  wt = []
  W = []
  n = int(text[line]) # Getting the number of items
  line += 1
  
  # Getting the values and weights of each item
  for i in range(n):
    arr = text[line].split()
    val.append(int(arr[0]))
    wt.append(int(arr[1]))
    line += 1

  F = int(text[line]) # Getting the number of family members
  line += 1
  ans = []
  total = 0
  
  # Getting the total price of all goods that the entire family and each family member can carry out during their shopping spree
  for i in range(F):
    W = int(text[line])
    line += 1
    ans.append(dp(val, wt, W, n))
    total += ans[i][0]
  
  # Printing the total price as well as the items each family member can get
  print("Test Case", x + 1)
  print("Total Price", total)
  
  # Printing the individual items
  for i in range(F):
    print(str(i + 1) + ": ", end='')
    
    for j in range(1, len(ans[i])):
      print(ans[i][j], end=' ')
    
    print()
  
  print()