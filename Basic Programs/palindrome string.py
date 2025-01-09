n = input("enter a string : ")
temp = n
reverse = ""
while len(temp) > 0:
    reverse += temp[-1]
    temp = temp[:-1]
if n == reverse:
    print("palindrome")
else:
    print("Not a palindrome")
