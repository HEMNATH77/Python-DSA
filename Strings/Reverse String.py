def reverse(a):
    a = list(a)
    n = len(a)
    left = 0
    right = n - 1
    while left < right :
        a[left],a[right] = a[right],a[left]
        left += 1
        right -= 1
    return "".join(a)
a = "geeks"
print(reverse(a))
