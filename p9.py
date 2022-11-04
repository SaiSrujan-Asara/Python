print("sum of first and last digit")
a =int(input("enter the number: "))
last = a % 10

while a >= 10:
    a = a / 10
sum = last + int(a)
print(sum)
