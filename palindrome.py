n = eval(input())
temp = n
reverse = 0
while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10
if n == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")

