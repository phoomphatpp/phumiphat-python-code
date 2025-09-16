"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""
class Rectangle:
    def __init__(self,length,width):
        self.__length = length
        self.__width = width
    def getArea(self):
        result = self.__length * self.__width
        return f"Area = {result}"
    def getPerimeter(self):
        result = 2*(self.__length + self.__width)
        return f"Perimeter = {result}"
    def isSquare(self):
        if self.__length == self.__width:
            return True
        else:
            return False
box1 = Rectangle(2,4)
box1.__length = 100 #no affect
box1.__width = 100  #no affect
print(box1.getArea())
print(box1.getPerimeter())
print(box1.isSquare())
