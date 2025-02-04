n = int(input("Enter a number : "))

for i in range(1,n+1):

    cube = i ** 3
    if cube == n:
        print("perfect cube")
        break
    elif (cube > n):
        print("Not a Perfect cube")
        break





