from math import gcd


class Rational:
    """
    This class is for performing arithmetic with fractions.
    """
    def __init__(self, numerator=1, denominator=1):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Wrong types.")
        if denominator == 0:
            raise ZeroDivisionError("Division on zero is impossible!")
        if not numerator:
            self.__numerator = 0
            self.__denominator = denominator
        else:
            user_gcd = gcd(numerator, denominator)
            self.__numerator = numerator // user_gcd
            self.__denominator = denominator // user_gcd

    def __add__(self, other):
        if isinstance(other, int):
            self.__numerator = self.__numerator + self.__denominator * other
            self.__init__(self.__numerator, self.__denominator)
            return self
        if isinstance(other, Rational):
            self.__numerator = self.__numerator * other.__denominator + other.__numerator * self.__denominator
            self.__denominator = self.__denominator * other.__denominator
            self.__init__(self.__numerator, self.__denominator)
            return self
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, int):
            self.__numerator = self.__numerator + self.__denominator * other
            self.__init__(self.__numerator, self.__denominator)
            return self
        if isinstance(other, Rational):
            self.__numerator = self.__numerator * other.__denominator + other.__numerator * self.__denominator
            self.__denominator = self.__denominator * other.__denominator
            self.__init__(self.__numerator, self.__denominator)
            return self
        return NotImplemented

    def __sub__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        new_numerator = self.__numerator * other.__denominator - self.__denominator * other.__numerator
        new_denominator = self.__denominator * other.__denominator
        return Rational(new_numerator, new_denominator)

    def __isub__(self, other):
        if isinstance(other, int):
            self.__numerator = self.__numerator - self.__denominator * other
            self.__init__(self.__numerator, self.__denominator)
            return self
        if isinstance(other, Rational):
            self.__numerator = self.__numerator * other.__denominator - other.__numerator * self.__denominator
            self.__denominator = self.__denominator * other.__denominator
            self.__init__(self.__numerator, self.__denominator)
            return self
        return NotImplemented

    def __mul__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        new_numerator = self.__numerator * other.__numerator
        new_denominator = self.__denominator * other.__denominator
        return Rational(new_numerator, new_denominator)

    def __imul__(self, other):
        if isinstance(other, int):
            self.__numerator = self.__numerator * other
            self.__init__(self.__numerator, self.__denominator)
            return self
        if isinstance(other, Rational):
            self.__numerator = self.__numerator * other.__numerator
            self.__denominator = self.__denominator * other.__denominator
            self.__init__(self.__numerator, self.__denominator)
            return self
        return NotImplemented

    def __truediv__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        new_numerator = self.__numerator * other.__denominator
        new_denominator = self.__denominator * other.__numerator
        return Rational(new_numerator, new_denominator)

    def __idiv__(self, other):
        if isinstance(other, int):
            self.__denominator = self.__denominator * other
            self.__init__(self.__numerator, self.__denominator)
            return self
        if isinstance(other, Rational):
            self.__numerator = self.__numerator * other.__denominator
            self.__denominator = self.__denominator * other.__numerator
            self.__init__(self.__numerator, self.__denominator)
            return self
        return NotImplemented

    def __eq__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        if self.__numerator == other.__numerator and self.__denominator == other.__denominator:
            return True
        else:
            return False

    def __ne__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        if self.__numerator != other.__numerator and self.__denominator != other.__denominator:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.__numerator * other.__denominator > other.__numerator * self.__denominator:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__numerator * other.__denominator < other.__numerator * self.__denominator:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.__numerator * other.__denominator >= other.__numerator * self.__denominator:
            return True
        else:
            return False

    def __le__(self, other):
        if self.__numerator * other.__denominator <= other.__numerator * self.__denominator:
            return True
        else:
            return False

    def print_float(self):
        return self.__numerator / self.__denominator

    def __str__(self):
        return f'{self.__numerator}/{self.__denominator}'


def main():
    obj_1 = Rational(2, 4)
    obj_2 = Rational(5, 3)
    obj_3 = Rational(7, 9)
    try:
        print("Fraction_1 = ", obj_1, ", fraction_2 = ", obj_2, ", fraction_3 = ", obj_3)
        print("Fraction_1 + fraction_2 = ", obj_1 + obj_2)
        print("Fraction_1 - fraction_2 = ", obj_1 - obj_2)
        print("Fraction_1 * fraction_2 = ", obj_1 * obj_2)
        print("Fraction_1 / fraction_2 = ", obj_1 / obj_2)
        obj_2 += obj_2
        print("Fraction_2 += fraction_2 - ", obj_2)
        obj_2 -= obj_1
        print("Fraction_2 -= fraction_1 - ", obj_2)
        print("If fraction_1 == fraction_3: ", obj_1 == obj_3)
        obj_3 *= obj_1
        print("Fraction_3 *= fraction_2 - ", obj_3)
        obj_2 /= obj_3
        print("Fraction_2 /= fraction_3 - ", obj_2)
    except Exception as e:
        print(e)


main()
