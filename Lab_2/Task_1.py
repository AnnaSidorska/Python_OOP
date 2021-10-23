class Rectangle:
    """
    This class is for calculating area and perimeter of the rectangle.
    """
    def __init__(self, length=1, width=1):
        self.__width = width
        self.__length = length

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        if not isinstance(length, (int, float)):
            raise TypeError("Length must be int of float.")
        if not 0.0 < length < 20.0:
            raise ValueError("Invalid input. Length should be a number in range 0 - 20.")
        self.__length = length

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, (int, float)):
            raise TypeError("Width must be int of float.")
        if not 0.0 < width < 20.0:
            raise ValueError("Invalid input. Width should be a number in range 0 - 20.")
        self.__width = width

    def perimeter(self):
        return f'Area: {(self.__length + self.__width) * 2}'

    def square(self):
        return f'Square: {self.__width * self.__length}'


def main():
    obj1 = Rectangle()
    try:
        obj1.length = 3
        obj1.width = 1.5
        print(obj1.perimeter())
        print(obj1.square())
    except Exception as e:
        print(e)


main()
