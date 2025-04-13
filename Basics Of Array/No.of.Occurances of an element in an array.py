def no_of_occurs(a):
    count = 0
    target = int(input("Enter Target : "))
    for i in a:
        if a[i] == target:
            count += 1
    return count

a = [1,2,3,4,5,1,2,3,4]
print(no_of_occurs(a))