def merge(arr, left, mid, right):
	left_arr_size = mid-left+1
	right_arr_size = right - mid

	left_Arr = [arr[left+x] for x in range(left_arr_size)]
	right_Arr = [arr[mid+1+x] for x in range(right_arr_size)]

	i = 0
	j = 0
	k = left

	while i < left_arr_size and j < right_arr_size:

		if left_Arr[i] < right_Arr[j]:
			arr[k] = left_Arr[i]
			i = i+1
		else:
			arr[k] = right_Arr[j]
			j = j+1
		k=k+1

	while i < left_arr_size:
		arr[k] = left_Arr[i]
		i=i+1
		k=k+1

	while j < right_arr_size:
		arr[k] = right_Arr[j]
		j=j+1
		k=k+1


def merge_sort(arr, left, right):

	if left < right:

		mid = (left+right)//2

		merge_sort(arr, left, mid)
		merge_sort(arr, mid+1, right)
		merge(arr, left, mid, right)

	return arr


arr = [14,6,39,56,44]
print(merge_sort(arr,0,len(arr)-1))