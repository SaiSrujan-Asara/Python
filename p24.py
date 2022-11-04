print("count even and odd number")
n = []
a =int(input("enter the no of elements: "))
for i in range(a):
    b = int(input("enter the numbers: "))
    n.append(b)
c1 = 0
c2 = 0
for i in n:
    if i % 2 == 0:
        c1 = c1 + 1
    else:
        c2 = c2 + 1
print("total number of even are:", c1)
print("total number of odd are:", c2)