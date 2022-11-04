print("All occurance of charecter")
a = input("enter the word: ")
l= len(a)
c = []
e = []
for i in range(0,l):
    count = 0
    if a[i] in e:
        continue
    else:
        e.append(a[i])
        for j in range(1,l):
            if a[i] == a[j]:
                count = count + 1
                c.append(count)
        
for i in range(len(e)):
    print("Total Occurance of",e[i], "is", c[i])