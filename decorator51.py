def s1(fun):
    def s2(a,b,c):
    
        c = fun()
        re = (a + b) * c
        print(re)
        
    return s2


def s3():
    cal =  3
    return cal
    
x = s1(s3)
x(1,2,3)


