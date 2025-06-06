def running_sum(arr):
    result = []
    current_sum = 0
    for x in arr:
        current_sum += x
        result.append(current_sum)
    return result


print(running_sum([4,5,4,7,5]))