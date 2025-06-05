def count_frequency(arr):
    freq = {}
    for item in arr:
        freq[item] = freq.get(item,0)+1
    return freq

print(count_frequency([1,2,4,1,5,2,4,1]))