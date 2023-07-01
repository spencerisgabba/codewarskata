def max_sequence(arr):
    
    if not arr:
        return 0

    max = arr[0]
    sum = 0 

    for num in arr:
        sum += num
        if sum < 0:
            sum = 0
        if sum > max:
            max = sum

    if max < 0:
        return 0
    else:
        return max