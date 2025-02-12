def substring(a,b):
    m = len(a)
    n = len(b)
    for i in range(m-n+1):
        match = True
        for j in range(n):
            if a[i+j] != b[j]:
                match = False
                break
        if match:
            return True
    return False

a = "abcd"
b = "cd"

print(substring(a,b))




