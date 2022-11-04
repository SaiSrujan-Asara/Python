print("negative numbers in list")
x = []
a = int(input("enter the no of elements: "))
for i in range(a):
    b = int(input("enter the elements: "))
    x.append(b)
for i in x:
    if i < 0:
        print(i)