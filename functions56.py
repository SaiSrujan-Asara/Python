# define two methods

# second method that will be returned
# by first method
def B(a,b,c):
	print("Inside the method B.",a,b,c)
	
# first method that return second method
def A(a):
	print("Inside the method A.",a)
	
	# return second method
	return B

# form a object of first method
# i.e; second method
returned_function = A(10)

returned_function(5,6,7)

print("-----------------------------------------")

def D(a,b,c):
	#print("Inside the method B.",a,b,c)
	return a,b,c
# first method that return second method
def C(a):
	print("Inside the method A.",a)
	
	# return second method
	return D

# form a object of first method
# i.e; second method
z = C(100)

k = z(50,60,70)

print(k)

print("----------------------------------------------")


def k(d):
    print("this is last statemenr wich is:", d)


def i(a,b,c):
    print("Inside the method B.",a,b,c)
    
    return k
	
# first method that return second method
def j(a):
	print("Inside the method A.",a)
	
	# return second method
	return i

# form a object of first method
# i.e; second method
t = j(100000)

print("******")

l= t (23,89,34)

l(0)
