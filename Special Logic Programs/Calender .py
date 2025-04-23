def calender(a):
    day = input("Enter the day : ")
    n = 10
    index = a.index(day)
    new = (index + n) % 7
    return a[new]
a =["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
print(calender(a))