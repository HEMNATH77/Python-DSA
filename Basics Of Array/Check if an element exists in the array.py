def check(a):
    element = int(input("Enter the element to check : "))
    if element in a:
        index = a.index(element)
        return f"{element} is in the array at {index}"       # f is formatted string

    else:
        return f" {element} is not in the array"

a = [1,2,3,4,5]

print(check(a))