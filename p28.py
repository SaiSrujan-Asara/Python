print("delete element at any position")
n1 = []
n2 = []
a =int(input("enter the no of elements: "))
for i in range(a):
    b = int(input("enter the numbers: "))
    n1.append(b)
c = int(input("enter the position of element to be delete: "))

if c > a:
    print("invalid position")
else:
    for i in range(a):
        if i+1 == c:
            continue
        else:
            n2.append(n1[i])

    print(n1)
    print(n2)