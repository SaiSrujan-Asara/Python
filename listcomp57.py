a = [1,2,3,4,5,6,7]

list = [i for i in a if i % 2 == 0 ]
print(list)

matrix = [[j for j in range(5)] for i in range(3)]
 
print(matrix)


list = ["even number" if i %2 == 0 else "odd number" for i in range(9)]
print(list)


print("---------------")

i = ["r","a","m"]
j = [1,2,3]

dic = {x:y for (x,y) in zip(i,j) }
print(dic)

dic1 = {i:i*2 for i in range(1,9)}
print(dic1)