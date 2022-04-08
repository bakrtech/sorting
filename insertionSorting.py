# Python program for implementation of Insertion Sort

# Function to do insertion sort
def insertionSort(arr):
	# Traverse through 1 to len(arr)
	for i in range(1, len(arr)):
		key = arr[i] #11
		# Move elements of arr[0..i-1], that are
		# greater than key, to one position ahead
		# of their current position
		j = i-1 #0
		while j >=0 and key < arr[j] : #j zero hai aur 11 chota hai 0 se
				arr[j+1] = arr[j] #[12,12] 
				j -= 1
		print(arr[j+1]," as the value of j is ",j," and key is ",key)
		print(arr)
		arr[j+1] = key
# Driver code to test above
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
	print ("%d" %arr[i])

# This code is contributed by Mohit Kumra

