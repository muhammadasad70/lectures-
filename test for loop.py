list=["ahmad","ali","asad","hassan",1,2,45,65,67,89,90,86,64,53]
for item in list:
    if str(item).isnumeric() and item>6:
        print(item)