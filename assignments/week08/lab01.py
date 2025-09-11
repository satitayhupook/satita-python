"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""

class Rectangle:

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def get(self):
        return self.__length * self.__width
    
    def getPerimeter(self):
        return 2 * (self.__length + self.width)
    
    def isSquarn(self):
        if self.__length == self.__width:
            return True
        else:
            return False
        
x = Rectangle(10, 5)

print("Area of x = " + x.getarea())
print("Perimeter of x = " + x.getPerimeter())

if x.isSquarn:
    print("x is squarn")
else:
    print("x is not squarn")