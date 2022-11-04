print("reverse of a string")
a = input("enter the word: ")
l= len(a)
l = l-1
c1 = ""
while l >= 0:
    c1= c1 + a[l]
    l = l - 1
print("reverse of a string",c1)

