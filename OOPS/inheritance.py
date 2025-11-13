class Parent:
    def show(self):
        print("This is the parent class method.")

class Child(Parent):
    def show(self):
        super().show()  # Calling the parent class method
        print("This is the child class method.")

c = Child()
c.show()
