print("saparate even and odd list")
n1 = []
even = []
odd = []
a =int(input("enter the no of elements: "))
for i in range(a):
    b = int(input("enter the numbers: "))
    n1.append(b)

for i in n1:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
    
print("list",n1)
print("even",even)
print("odd",odd)