def missing(a):
    n = len(a) + 1
    total = n * (n +1) // 2
    sum = 0
    for i in a:
        sum += i
    missing = total - sum
    return missing
a = [1,2,3,4,6]
print(missing(a))
