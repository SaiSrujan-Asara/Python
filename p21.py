print("min and max of a number")
x = []
a = int(input("enter the no of elements: "))
for i in range(a):
    b = int(input("enter the elements: "))
    x.append(b)
j = 1
for i in x:
    count = 0
    while count < a:
        if x[i] < x[j]:
            x[i] = x[j]
            j = j + 1
        count = count + 1
        print(x[i])
            