print("sum of even number")
a =int(input("enter the first number: "))
b =int(input('enter the second number: '))
sum = 0
for i in range(a, b+1):
    if i % 2 == 0:
        sum = sum + i
print(sum)