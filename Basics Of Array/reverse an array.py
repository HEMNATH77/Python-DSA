def reverse(n):
    start = 0
    end = len(n)-1
    while start < end:
        n[end] , n[start] = n[start] , n[end]

        start += 1
        end   -= 1
    return n

n = [1,2,3,4,5]
print("Reversed array : ",reverse(n))
