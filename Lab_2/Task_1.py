class Rectangle:

    def __init__(self, length=1, width=1):
        self.__width = self.set_wid(width)
        self.__length = self.set_len(length)

    def get_len(self):
        return self.__length

    def get_wid(self):
        return self.__width

    def set_len(self, length):
        if not isinstance(length, (int, float)):
            raise TypeError("Length must be int of float.")
        if not 0.0 < length < 20.0:
            raise ValueError("Invalid input. Length should be a number in range 0 - 20.")
        self.__length = length

    def set_wid(self, width):
        if not isinstance(width, (int, float)):
            raise TypeError("Length must be int of float.")
        if not 0.0 < width < 20.0:
            raise ValueError("Invalid input. Width should be a number in range 0 - 20.")
        self.__width = width

    def perimeter(self):
        print("Perimeter: ")
        return (self.__length + self.__width) * 2

    def square(self):
        print("Square: ")
        return self.__width * self.__length


def main():
    obj1 = Rectangle()
    try:
        obj1.set_len(1)
        print(obj1.perimeter())
        print(obj1.square())
    except Exception as e:
        print(e)


main()
