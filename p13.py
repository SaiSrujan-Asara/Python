print("factors of a number")
a =int(input("enter the number: "))
print("The factor are")
for i in range(1,a+1):
    if a % i == 0:
        print(i)