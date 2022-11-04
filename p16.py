print("check prime number are not")
a =int(input("enter number: "))
count = 0

b= int(a/2)
for i in range(1,b):
    if a % i == 0:
        count = count + 1
if count == 1:
    print ("It is a prime number", a)
else:
    print("It is not prime number")