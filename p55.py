cars = {
        'mid':["fortuner","endivor","Harrir"],
        'class':["benz","bmw","audi"],
        'Top':["Rolls royes","lamborgini","ferrarie"]
        }

for i,j in cars.items():
    print("My fav cars in", i ,"range is")
    for k in j:
        print(k)
        

print("---------")


cars = {
        'mid':{"first":"fortuner","second":"endivor","third":"Harrir"},
        'class':{"first":"benz","second":"bmw","third":"audi"},
        'Top':{"first":"Rolls royes","second":"lamborgini","third":"ferrarie"}
        }

for x,y in cars.items():
    print("My fav cars in", x ,"range is")
    for a,b in y.items():
        print(b)
        