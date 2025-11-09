'''
Variable is a name that stores a value in a memory.
Python automatically detects the data type which is called as dynamic typing.
'''

# Integer data type
a = 10
print(type(a))

# Float data type
b = 10.5
print(type(b))

# String data type 
c = "Hello, World!"
print(type(c))

# Boolean data type
d = True
print(type(d))

# List (Ordered and mutable)
fruits = ["apple", "banana", "cherry"]
fruits[1] = "orange"  # Modifying the second element    
print(type(fruits))

# Tuple (Ordered and immutable) List cannot be modified after creation
coordinates = (10.0, 20.0)
print(type(coordinates))

# Dictionary (Key-Value pairs)
person = {
    "name": "John",
    "age": 30
}
print(type(person))

# set (unique and unordered)
numbers = {1, 2, 3, 4, 5}
print(type(numbers))

