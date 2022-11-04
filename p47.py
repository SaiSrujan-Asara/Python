print("count no of charectyer")
a = input("enter the word: ")
alp = ["a","b","c","d","e","f","g","h","i","j","k","l","m"]
num = ["0","1","2","3","4","5","6","7","8","9"]
spe = ["@","#","$","%","&"]
l= len(a)
c1 = 0
c2 = 0
c3 = 0
for i in range(l):
    if a[i] in alp:
        c1 = c1 + 1
    elif a[i] in num:
        c2 = c2 + 1
    elif a[i] in spe:
        c3 = c3 + 1
    else:
        continue

print("alphabets are",c1)
print("Numbers are",c2)
print("Special char",c3)