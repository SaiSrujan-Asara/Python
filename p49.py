print("count no of words")
a = input("enter the word: ")
l= len(a)
c1 = 1
print(l)
for i in range(l):
    if a[i] == " ":
        c1 = c1 + 1
print("total words are",c1)

