capacity = int(input("Enter  capacity  : "))

level = input("Enter  Level(L/M/H) : ")

if capacity < 0:
    print(" Invalid ")
elif capacity == 0:
    print("Time = 0 min")
elif capacity > 7000:
    print("Overload")


if level == 'L'  and capacity <= 2000:
    print("Time : 25 minutes " )
elif level == 'M' and 2001 <= capacity <= 4000:
    print("Time : 35 minutes")
elif level == 'H' and 4001 <= capacity <= 7000:
    print("Time: 45 minutes")
else :
    print("enter valid level")

print(capacity,level)






























