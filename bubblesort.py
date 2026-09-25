def bubble_sort(arr: List):

	# for example the given array [14,66,23,56,44]

	size = len(arr)
	
	for i in range(size-1): # 0 to size-2 i.e, 0 to 3 : 4 times 

		for j in range(size - i - 1): # 0 to size - 1 - i, i.e, 0 to 3 
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]

	return arr

arr = [14,66,23,56,44]
print(bubble_sort(arr))
