class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other_obj):
        test=Person("",0)
        test=str(self.age) + other_obj.name
        return test

    def __sub__(self, other_obj):
        test=Person("",0)
        test=self.age - other_obj.age
        return test

    def __mul__(self, other_obj):
        test=Person("",0)
        test=self.age * other_obj.age
        return test

    def __truediv__(self, other_obj):
        test=Person("",0)
        test=self.age / other_obj.age
        return test


p = Person("Alex", 15)
p1 = Person("Pesho", 10)
print(p*p1)