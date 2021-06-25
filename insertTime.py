import random
import time

# Funtion to sort an array of ints using insertion sort
def sort(arr, n):
  # Iterating from arr[1] to arr[n]
  for x in range(1, n):
    key = arr[x] # Current element
    i = x - 1
    
    # Comparing the current element to the previous elements
    while i >= 0:
      if arr[i] > key:
        arr[i + 1] = arr[i]
      else:
        break
        
      i -= 1
    
    # Setting the correct position of the current element  
    arr[i + 1] = key

n = 0
arr = []

# Sorts an array of 10 different sizes
for x in range(1, 11):
  n = 2500 * x # Getting the new size of the array
  
  # Appending random numbers between 0-10000 to the array
  for i in range(n):
    arr.append(random.randint(0, 10000))
  
  start_time = time.time() # Getting the start time
  sort(arr, n) # Sorting the array
  end_time = time.time() - start_time # Calculates the total time needed for sorting
  
  print("n = " + str(n), ", Runtime = ", str(end_time))
  
  arr.clear() # Resetting/Clearing the array