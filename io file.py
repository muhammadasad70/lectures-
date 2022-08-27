# r-read mode-default
# w-write mode
# x-creat a file if not exixt
# a-add the content to the file
# b-binary file
# t-text file -default
# +-both read and write mode
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end="")
#     print("\n",end="")
# print("-----------------------")
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print("\n",end="")
# for i in range(4):
#     for j in range(4):
#         print("#",end="")
#     print("\n",end="")
# for i in range(5):
#     for j in range(1,5):
#         print(" ",end="")
#     for j in range(i+1):
#         print('*',end="")
#     print()
for i in range(5,0,-1):
    for k in range(1,6-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print("\n",end="")