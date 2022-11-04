print("sorting of a number")
n1 = []
a =int(input("enter the no of elements: "))
for i in range(a):
    b = int(input("enter the numbers: "))
    n1.append(b)
print(n1)
k=0
for i in range(a):
    for j in range(i+1):
        if n1[i] > n1[j]:
            k = n1[i]
            n1[i]=n1[j]
            n1[j]= k
print(n1)
        