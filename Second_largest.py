def second_largest(arr):
    first = second = float('-inf')
    
    for num in arr:
        if num>first:
            second = first
            first = num
        else: 
            num>second and num!=first
            second = num
    return second if second != float('-inf') else None

print(second_largest([10,15,14,7,18]))
    
