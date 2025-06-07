def first_last_occur(arr,ele):
    
    first = last = -1
    for i in range(len(arr)):
        if arr[i] == ele:
            if first == -1:
                first = i
            last = i
    return(first,last)

print(first_last_occur([1,2,4,5,7,8,2],2)) 