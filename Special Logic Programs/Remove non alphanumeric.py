def non_alpha(a):
    result = ""
    for i in a:
        if ('a'<= i <='z') or ('A'<= i <='Z') or ('0'<= i <='9'):
            result += i
    return result

a = input("Enter a : ")
print(non_alpha(a))
