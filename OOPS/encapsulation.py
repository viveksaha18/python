class Marks:
    def __init__(self, math, science):
        self.__math = math          # Private attribute
        self.__science = science    # Private attribute

    def getMath(self):
        return self.__math

marks = Marks(90, 85)
marks.__math = 95  # Attempting to modify private attribute  # This will not change the private attribute
print(marks.getMath())  # Output: 90