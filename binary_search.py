def binary_search(arr,ele):
    low ,high = 0,len(arr)-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid] == ele:
            return mid
        elif arr[mid]<ele:
            low = mid+1
        else:
            high = mid-1
    return -1

print(binary_search([1,2,4,5,7,8,6],8))