print("reverse of number")
a =int(input("enter number: "))
rev = 0
while a > 0:
    x = a % 10
    rev = (rev * 10) + x
    a = int(a / 10)
    
print(rev)