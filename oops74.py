class test:
    y = 10
    def reset(self):
        self.x = 100
        print(self.x)
    def re3(self):
        self.z = 1000
        print(self.z)
        print(self.x)
        print(self.y)

a = test()
print(a.y)
a.reset()
print(a.x)
a.re3()
print(a.z)

print("-----------------------")

class test:
    x = 10
    def reset(self):
        self.y = 1
        print(self.y)
        print(self.x)
    def re3(self):
        self.z = 3
        print(self.z)
        print(self.x)

a = test()
a.reset()
a.re3()

print("---------------------")


class test:
    x = 10
    def reset(self):
        self.y = 1
        print(self.y)
        print(self.x)
    def re3(self):
        self.z = 3
        print(self.z)
        print(self.x)
        print(self.y)

a = test()
a.reset()
a.re3()

print("---------------------------")

class test1:
    x = 10
    def reset(self,a):
        self.w=a
        self.y = 1
        print(self.y)
        print(self.x)
        print(self.w)
    def re3(self):
        self.z = 3
        print(self.z)
        print(self.x)
        print(self.y)
        print(self.w
              )

i = test1()
i.reset(50000000)
i.re3()
print("--")
print(i.w)