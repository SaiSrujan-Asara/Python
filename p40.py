n1 = [5, 2, 8, 7, 1];     
temp = 0;    
     
#Displaying elements of original array    
print("Elements of original array: ");    
for i in range(0, len(n1)):    
    print(n1[i], end=" ");    
     
#Sort the array in ascending order    
for i in range(0, len(n1)):    
    for j in range(i+1, len(n1)):    
        if n1[i] < n1[j]:
            k = n1[i]
            n1[i]=n1[j]
            n1[j]= k    
     
print(n1)