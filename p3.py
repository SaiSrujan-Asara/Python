print("odd number")
a =int(input("enter the first number: "))
b =int(input('enter the second number: '))
for i in range(a, b+1):
    if i % 2 == 1:
        print(i)