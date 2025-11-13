class Student:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        
    def greet(self):
        print("Hello")
    

# Creating an object of the Student class
s1 = Student("Vivek", 21)
print(s1.name)  # Output: Vivek
print(s1.age)   # Output: 21
s1.greet()      # Output: Hello

class Car:
    def __init__(self, brand, model):
        carBrand = brand
        carModel = model
        print(carBrand)
        print(carModel)

# Creating an object of the Car class
c1 = Car("Toyota", "Corolla")
