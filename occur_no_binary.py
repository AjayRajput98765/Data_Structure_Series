def first_occurrence(arr, x):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            result = mid
            high = mid - 1  
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return result

def last_occurrence(arr, x):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            result = mid
            low = mid + 1  
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return result

def count_occurrences(arr, x):
    first = first_occurrence(arr, x)
    last = last_occurrence(arr, x)
    if first == -1:
        return 0
    return last - first + 1


arr = [1, 2, 2, 2, 3, 4, 5]
x = 2
print("Count of", x, "is:", count_occurrences(arr, x))  
