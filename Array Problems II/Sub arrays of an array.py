def subarray(a):
    n = len(a)
    result =[]
    for start in range(n):
        for end in range(start, n):
            sub = a[start:end+1]
            result.append(sub)
    return result

a = [1,2,3]
print(subarray(a))
