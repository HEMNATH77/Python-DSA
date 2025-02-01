n = int(input("Enter a number : "))
sum = 0
temp = n

while(temp !=  0):
    digit = temp % 10
    sum = digit ** 3 + sum
    temp //= 10

if(sum == n):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")







