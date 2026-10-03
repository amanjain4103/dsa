def partition(arr, left, right):
    pivot = left
    i = left+1
    j = right

    while(True):

        while i <= right and arr[i] <= arr[pivot]:
            i+=1
        while j >= left + 1 and arr[j] >= arr[pivot]:
            j-=1

        if(i>j):
            break
        
        arr[i],arr[j] = arr[j],arr[i]

    arr[j],arr[pivot] = arr[pivot], arr[j]

    pivot_new_pos = j
    return pivot_new_pos


def quick_sort(arr, left, right):
    if left < right: 
        pivot = partition(arr,left,right)
        quick_sort(arr,left, pivot-1)
        quick_sort(arr,pivot+1,right)


arr = [23,45,12,65,34,10,3]
quick_sort(arr,0,(len(arr)-1))
print(arr)