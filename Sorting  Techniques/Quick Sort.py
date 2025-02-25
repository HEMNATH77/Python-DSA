def quick(a):
    if len(a) <= 1:
        return a

    pivot = a[len(a) // 2]

    left = [x for x in a if x < pivot]
    middle = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]

    return quick(left) + quick(middle) + quick(right)

a = [5,8,6,1,4,3]
print(quick(a))

