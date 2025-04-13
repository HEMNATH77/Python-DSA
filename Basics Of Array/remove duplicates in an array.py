def remove_duplicates(a):
    s = []
    for i in a:
        if i not in s:
            s.append(i)
    return s
a = [1,2,3,3,4,5,2,1]
print(remove_duplicates(a))