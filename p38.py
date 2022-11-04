print("right rotation")
n1 = []
n2 = []
a =int(input("enter the no of elements: "))
for i in range(a):
    b = int(input("enter the numbers: "))
    n1.append(b)
c = int(input("enter the position to rotate: "))

v= a - c

for i in range(v, a):
    n2.append(n1[i])
for i in range(v):
    n2.append(n1[i])

print(n2)