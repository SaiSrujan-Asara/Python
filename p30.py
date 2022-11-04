print("Unique numbers")
n1 = []
n2 = []
n3 = []
a =int(input("enter the no of elements: "))
for i in range(a):
    b = int(input("enter the numbers: "))
    n1.append(b)

for i in range(a):
    if n1[i] in n3:
        continue
    else:
        count = 1
        for j in range(i+1, a):
            if n1[i] == n1[j]:
                count = count + 1
        n2.append(count)
        n3.append(n1[i])
    
for i in range(len(n2)):
    print("Unique numbers are",n3[i])
    