def linear_Search(arr , ele):
    for i in range(len(arr)):
        if arr[i] == ele:
            return i
    return -1


print(linear_Search([4,5,6,7,8,9],5))