def s1(func):
    def s2():
        
        print("this is the first inside")
        
        func()
        print("This is after the outside fuction")
            
    return s2

def s3():
    print("this is the fuction need to print")

z = s1(s3)

z()