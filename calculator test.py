x=int(input("enter 1st number"))
y=int(input("enter 2nd number"))
z=input("enter the desire operator")
if x==45 and y==3 and z=="*":
    print("555")
elif x==56 and y==9 and z=="+":
    print("77")
elif x==56 and y==6 and z=="/":
    print("4")
elif z=="+":
    print(x+y)
elif z=="-":
    print(x-y)
elif z=="*":
    print(x*y)
else:
    print(x//y)


