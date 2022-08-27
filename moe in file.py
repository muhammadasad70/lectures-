# .tell for tell where is the pointer
# .seek read from the location which you spacify
# f=open("file1.txt")
# print(f.readline())
# print(f.tell())
# print(f.readline())
# print(f.tell())
# f.seek(30)
# print(f.readline())
# f.close()
# with block working
with open ("file1.txt") as f:
    a=f.readlines()
    print(a)
f=open("file1.txt")
print(f.readline())
f=open("file1.txt")
print(f.readline(5))