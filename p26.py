print("copy 1 list to another")
n = []
copy_n=[]
a =int(input("enter the no of elements: "))
for i in range(a):
    b = int(input("enter the numbers: "))
    n.append(b)

for i in range(a):
    copy_n.append(n[i])
print(n)
print(copy_n)