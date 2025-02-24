def merge(a):
    if len(a)<=1:
        return a
    mid = len(a)//2
    left = merge(a[:mid])
    right = merge(a[mid:])

    return merge_a (left , right)

def merge_a(left,right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])

    return result

a = [2,5,3,6,4,8,1]
print(merge(a))






