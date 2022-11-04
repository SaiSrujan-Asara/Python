print("Search of a number")
n1 = []
a =int(input("enter the no of elements: "))
for i in range(a):
    b = int(input("enter the numbers: "))
    n1.append(b)
b = int(input("enter the number to be search: "))
count = 0
for i in n1:
    count = count + 1
    if i == b:
        print("Number is found position at",count)
        break

