print("sum of elements of list")
x = []
a = int(input("enter the no of elements: "))
for i in range(a):
    b = int(input("enter the elements: "))
    x.append(b)
sum = 0
for i in x:
    sum = sum + i
print(sum)