# The greedy algorithm for the problem
def greedy(activity, n):
  chosen = []
  
  # Sorting the activities by decreasing start time using insertion sort
  # Iterating from activity[1] to activity[n]
  for x in range(1, n):
    key = activity[x] # Current element
    i = x - 1
    
    # Comparing the current element to the previous elements
    while i >= 0:
      if activity[i][1] < key[1]:
        activity[i + 1] = activity[i]
      else:
        break
        
      i -= 1
    
    # Setting the correct position of the current element  
    activity[i + 1] = key
  
  x = 0
  chosen.append(activity[x][0]) # Last activity is always selected
  
  # Iterating through the sorted activities
  for i in range(1, n):
    # If the activity has an end time less than or equal to the start time of the previous chosen activity, it is selected.
    if activity[i][2] <= activity[x][1]:
      chosen.append(activity[i][0]) # Recording the chosen activity id
      x = i

  return chosen

# Open data.txt file
fileText = open('act.txt', 'r')
set = 1

# Going through all of the test cases
while True:
  line = fileText.readline()
  
  if not line: # If the end of the file is reached, end program
    break
  else:
    n = int(line) # Getting the number of activities
    
    activity = []
    
    # Getting the activities
    for x in range(n):
      arr = fileText.readline().split()
      activity.append([])
      activity[x].append(int(arr[0]))
      activity[x].append(int(arr[1]))
      activity[x].append(int(arr[2]))
    
    chosen = greedy(activity, n) # Finding the max activities
    chosen.reverse()
    
    # Printing results
    print("Set ", str(set))
    print("Maximum number of activities = ", str(len(chosen)))
    
    for x in range(len(chosen)):
      print("", chosen[x], end="")
    
    set += 1
    
    print("\n")