print("last occurance of char")

s = "Hello, World"
c = 'o'
 
index = s.rfind(c)

print(index)

if index != -1:
    print(f"Char '{c}' is found at index {index}")    # Char 'o' is found at index 8
else:
    print("Char not found")