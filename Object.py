class Numbers:
    def __init__(self, n1=0.0, n2=0.0):
        self.n1 = n1
        self.n2 = n2

    def display(self):
        print(f"First Value : {self.n1}\tSecond value : {self.n2}")

    def add(self, t):
        r = Numbers()
        r.n1 = self.n1 + t.n1   
        r.n2 = self.n2 + t.n2   
        return r
    
obj1 = Numbers(56.4, 98.3)
obj2 = Numbers(82.4, 19.6)

obj2 = obj1.add(obj2)

obj1.display()
obj2.display()
