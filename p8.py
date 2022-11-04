print("find lcm of digits")
a =int(input("enter first number: "))
b =int(input("enter second number: "))
c =int(input("enter third number: "))
if a > b and a > c:
    l= a
elif b > c and b > a:
    l = b
elif c > a and c > b:
    l = c
else:
    l =c 

while l > 0:
    if l % a == 0 and l % b == 0 and l % c == 0:
        print("LCM of 3 numbers are",l)
        break
    l = l + 1