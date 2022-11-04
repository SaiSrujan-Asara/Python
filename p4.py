print("sum of natural number")
a =int(input("enter the first number: "))
b =int(input('enter the second number: '))
sum = 0
for i in range(a, b+1):
    sum = sum + i
print(sum)