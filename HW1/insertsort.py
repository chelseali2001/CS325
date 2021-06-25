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

# Open data.txt file
fileText = open('data.txt', 'r')
text = fileText.readlines()

# Reading the file line by line
for x in text:
  arr = x.split()
  n = int(arr[0]) # Getting the length of the array
  new_arr = arr[1:] # Getting rid of the first element in the list
  int_arr = [int(val) for val in new_arr] # Converting the line of strings to an array of ints
  
  sort(int_arr, n) # Sorting the array of ints
  
  # Printing the sorted array
  for i in range(n):
    print(int_arr[i], end=" ")
  
  print()

# Close file
fileText.close()