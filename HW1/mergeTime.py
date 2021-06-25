import random
import time

# Funtion to sort an array of ints using merge sort
def sort(arr, n):
  if n > 1:
    mid = int(n / 2) # Middle index of the array
    left = arr[:mid] # First half of the array
    right = arr[mid:] # Second half of the array
 
    sort(left, len(left)) # Sorting the first half of the array
    sort(right, len(right)) # Sorting the second half of the array

    x = 0
    i = 0
    j = 0
    
    # Sorting and merging the two halves
    while x < len(left) and i < len(right):
        if left[x] < right[i]:
            arr[j] = left[x]
            x += 1
        else:
            arr[j] = right[i]
            i += 1
        j += 1

    # Merging any left over elements in the two arrays
    for k in range(x, len(left)):
      arr[j] = left[k]
      j += 1

    for k in range(i, len(right)):
      arr[j] = right[k]
      j += 1

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