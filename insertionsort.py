def insertion_sort(arr:List):

	# for example the given array [14,6,3,56,44]

	size = len(arr)
	for i in range(1,size):
		last = i
		for j in range(i,-1,-1):
			if arr[j] > arr[last]:
				arr[j], arr[last] = arr[last], arr[j]
				last = j 

	return arr

arr = [14,6,3,56,44]
print(insertion_sort(arr))

