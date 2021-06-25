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