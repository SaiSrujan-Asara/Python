print("Insert element at any position")
n1 = []
n2 = []
a =int(input("enter the no of elements: "))
for i in range(a):
    b = int(input("enter the numbers: "))
    n1.append(b)
c= int(input("enter the number to be inserted: "))
d= int(input("enter the position to be inserted: "))
k = 0
if a+2 <= d:
    k = k + 1
    print("invalid Position")
else:
    for i in range(a):
        if i+1 == d:
            n2.append(c)
            n2.append(n1[i])
        else:
            n2.append(n1[i])

if k == 0:
    if a+1 == d:
        n2.append(c)
    print(n1)
    print(n2)

        