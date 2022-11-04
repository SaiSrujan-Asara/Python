print("HCF of a number")
a =int(input("enter the first number: "))
b =int(input("enter the second number: "))
c =int(input("enter the third number: "))
if a <= (b and c):
    s = a
elif b <= (a and c):
    s = b
else:
    s = c
if a >= (b and c):
    l = a
elif b >= (a and c):
    l = b
else:
    l = c

r = l % s
rem = r
while rem != 0:
    q = rem
    rem = s % rem
    if rem == 0:
        s = q 
if l != a:
    new = a
elif l != b:
    new = b
else:
    new = c
s = q
l= new
r = l % s

rem = r
while rem != 0:
    q = rem
    rem = s % rem
    if rem == 0:
        s = q 
print("HCF of 3 numbers are:", q)
        