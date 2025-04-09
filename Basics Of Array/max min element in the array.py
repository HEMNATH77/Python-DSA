def max_min(n):
    if not n:
        return "Empty"
    max = n[0]
    min = n[0]
    for i in n:
        if i > max :
            max = i
        elif i < min:
            min = i
    return max,min

n = [3,4,5,2,1]
print(max_min(n))