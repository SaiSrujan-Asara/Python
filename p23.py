print("second largest number")
n = []
a =int(input("enter the no of elements: "))
for i in range(a):
    b = int(input("enter the numbers: "))
    n.append(b)

for i in range(a):
    for j in range(1,a):
        if n[i] <= n[j]:
            second = n[i]
            n[i] = n[j]     
    print(second)
    break