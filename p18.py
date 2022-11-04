print("check prime number in a range")
a =int(input("enter starting number: "))
b =int(input("entre ending number: "))
total = 0
for i in range(a, b+1):
    count = 0
    val = int(i/2)
    for j in range(1, val+1):
        if i % j == 0:
            count = count + 1
    if count == 1:
        print("Prime number is",i)
        total = total + i
print("sum of prime numbers are:", total)
            