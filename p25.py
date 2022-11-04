print("count positive and negative number")
n = []
a =int(input("enter the no of elements: "))
for i in range(a):
    b = int(input("enter the numbers: "))
    n.append(b)
c1 = 0
c2 = 0
for i in n:
    if i > 0:
        c1 = c1 + 1
    if i < 0:
        c2 = c2 + 1
    
print("no of positive numbers are:", c1)
print("no of negative numbers are:", c2)