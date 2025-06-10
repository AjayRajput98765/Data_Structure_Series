def first_occurrence(arr,x):
    low ,high = 0, len(arr)
    result = -1
    while low <= high :
        mid = (low+high)//2
        if arr[mid] == x:
            result = mid
            high = mid-1
        elif arr[mid]<x:
            low = mid+1
        else:
            high = mid-1
    return result

print(first_occurrence([4,2,4,7,5,8,2],2))
            
        