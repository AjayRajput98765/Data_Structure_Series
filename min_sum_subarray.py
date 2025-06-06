def min_sum_subarray(arr,k):
    window_sum = sum(arr[:k])
    min_sum = window_sum
    for i in range(k,len(arr)):
        window_sum += arr[i] - arr[i-k]
        min_sum = min(window_sum,min_sum)
    return min_sum


print(min_sum_subarray([2,4,1,5,6,7],2))
        
    
    