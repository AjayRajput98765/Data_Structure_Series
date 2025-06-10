def max_subarray_sum(arr,k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(len(arr)):
        window_sum = arr[i] - arr[i-k]
        max_sum = max(max_sum,window_sum)
    return max_sum

print(max_subarray_sum([4,1,2,4,5],2))
    