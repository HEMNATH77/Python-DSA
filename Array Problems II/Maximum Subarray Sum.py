def maximum_subarray_sum(a):
    max = a[0]
    sum = 0
    for i in a:
        sum = sum + i
        if sum > max:
            max = sum
        if sum < 0:
            sum = 0
    return max

a =[-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maximum_subarray_sum(a))
