print("Min and Max of a list")
n = []
a =int(input("enter the no of elements: "))
for i in range(a):
    b = int(input("enter the numbers: "))
    n.append(b)

for i in range(a):
    for j in range(1,a):
        if n[i] <= n[j]:
            n[i] = n[j]
    print("Maximum number is:",n[i])
    break

for i in range(a):
    for j in range(1,a):
        if n[i] >= n[j]:
            n[i] = n[j]
    print("Minimum number is:",n[i])
    break