print("count no of consonants and vowels")
a = input("enter the word: ")
alp = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
spe = ["a","e","i","o","u"]
l= len(a)
c1 = 0
c2 = 0
for i in range(l):
    if a[i] in alp:
        c1 = c1 + 1
    elif a[i] in spe:
        c2 = c2 + 1
    else:
        continue

print("Vowels are",c2)
print("Consonants are",c1)
