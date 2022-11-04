print("merge 2 lists to 3rd lists")
n1 = []
n2 = []
n3 = []
a =int(input("enter the no of elements in list 1: "))
for i in range(a):
    b = int(input("enter the numbers: "))
    n1.append(b)
c =int(input("enter the no of elements in list 2: "))
for i in range(c):
    d = int(input("enter the numbers: "))
    n2.append(d)

for i in range(a):
    n3.append(n1[i])
    
for i in range(c):
    n3.append(n2[i])

print(n2)
print(n3)