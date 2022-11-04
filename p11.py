print("occurance of number")
a =int(input("enter number: "))
count = 0
while a >= 10:
    x = a % 10
    b = a
    while b > 0:
        y = b % 10
        if x == y:
            count = count + 1
        b = int(b / 10)
    print("Occurance of",x,count)
    count = 0
    a = int(a / 10)
            