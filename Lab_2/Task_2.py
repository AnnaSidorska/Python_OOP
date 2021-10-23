import math


class Rational:
    """
    This class is for performing arithmetic with fractions.
    """
    def __init__(self, numerator=1, denominator=1):
        if not isinstance(numerator, int):
            raise TypeError("Wrong type of numerator.")
        if not isinstance(denominator, int):
            raise TypeError("Wrong type of denominator")
        if denominator == 0:
            raise ZeroDivisionError("Division on zero is impossible!")
        self.__numerator = numerator
        self.__denominator = denominator

    def print_float(self):
        return self.__numerator / self.__denominator

    def print_fraction(self):
        user_gcd = math.gcd(self.__numerator, self.__denominator)
        first_number = self.__numerator // user_gcd
        second_number = self.__denominator // user_gcd
        return f'{first_number}/{second_number}'


def main():
    obj = Rational(4, 2)
    print(obj.print_float())
    print(obj.print_fraction())


main()
