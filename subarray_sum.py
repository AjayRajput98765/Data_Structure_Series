def get_subarray_sum(arr,i,j):
    prefix = [0]*len(arr)
    prefix[0] = arr[0]
    for k in range(1,len(arr)):
        prefix[k] = prefix[k-1] + arr[k]
        
    return prefix[j] - (prefix[i-1]if i>0 else 0)

print(get_subarray_sum([1,2,4,5,6],1,3))