print("Factoria of a number")
a =int(input("enter the number: "))
fact = 1
while  a > 0:
    fact = fact * a
    a = a - 1
print("Factorial of a number is:", fact)