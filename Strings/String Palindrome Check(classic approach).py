def palindrome(a):
    a = a.lower().replace(" ","")
    n = len(a)
    left = 0
    right = n - 1
    while left < right :
        if a[left] != a[right]:
            return False
        left += 1
        right -= 1
    return True
a = "Malayalam"
print(palindrome(a))
