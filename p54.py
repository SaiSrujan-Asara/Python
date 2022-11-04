dic={"n1":"sai","n2":"rama","n4":"shiv","n5":"rama"}

x = dic["n1"]
#print(x)

y = dic["n2"]
#print(y)

dic["n3"]="krishna"

#print(dic)

z= dic["n3"]
#print(z)


for i in dic.items():
    for j in i:
        print(j)
print("------")

for i in dic:
    print(i)

l = ["shiva", "vishnu","bhrama","n2"]

for i in dic:
    if i in l:
        print("Greatest of all warriors",i)
        
print("------")

for i in dic.values():
    print(i)
    
print("-------")

for i in set(dic.values()):
    print(i)