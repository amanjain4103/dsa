def selection_sort(arr:List):

	# for example the given array [14,66,23,56,44]

	size = len(arr)
	for i in range(size-1):	
		min = i
		for j in range(i+1, size):
			if arr[j] < arr[min]:
				min = j 
		arr[i],arr[min] = arr[min], arr[i]

	return arr

arr = [14,66,23,56,44]
print(selection_sort(arr))
