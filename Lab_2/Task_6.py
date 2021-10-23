class Node:
    """
    This class represents a binary tree node with product's code and price.
    """
    def __init__(self, code, price):
        self.left = None
        self.right = None
        self.code = code
        self.price = price

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, node):
        if node and not isinstance(node, Node):
            raise TypeError("Left must have Node type!")
        self.__left = node

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, node):
        if node and not isinstance(node, Node):
            raise TypeError("Right must have Node type!")
        self.__right = node

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, code):
        if not isinstance(code, int):
            raise TypeError("Code must have int type!")
        if code < 1:
            raise ValueError("Code must be greater than 0!")
        self.__code = code

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError("Price must have int of float type!")
        if price < 0:
            raise ValueError("Price can't be less than 0!")
        self.__price = price

    def __str__(self):
        return f'Code: {self.code}, Price: {self.price}'


class Tree:
    """
    This class represents a binary tree of products' info(nodes).
    """
    def __init__(self):
        self.__root = None

    @property
    def root(self):
        return self.__root

    def add_product(self, code, price):
        if not isinstance(code, int):
            raise TypeError("Code must have int type!")
        if not isinstance(price, (int, float)):
            raise TypeError("Price must have int type!")
        if self.__root is None:
            self.__root = Node(code, price)
        else:
            self._add_product(code, price, self.root)

    def _add_product(self, code, price, node):
        if code < node.code:
            if node.left is not None:
                self._add_product(code, price, node.left)
            else:
                node.left = Node(code, price)
        else:
            if node.right is not None:
                self._add_product(code, price, node.right)
            else:
                node.right = Node(code, price)

    def find_product(self, code):
        if not isinstance(code, int):
            raise TypeError("Code must have int type!")
        if self.root is not None:
            return self.__find_product(code, self.root)
        else:
            return None

    def __find_product(self, code, node):
        if code == node.code:
            return node
        elif code < node.code and node.left is not None:
            return self.__find_product(code, node.left)
        elif code > node.code and node.right is not None:
            return self.__find_product(code, node.right)

    def total(self, code, number):
        if not isinstance(code, int):
            raise TypeError("Code must have int type!")
        if not isinstance(number, int):
            raise TypeError("Number must have int type!")
        if number < 1:
            raise ValueError("Number must be greater than 0!")
        product = self.find_product(code)
        return number * product.price


def main():
    tree = Tree()
    tree.add_product(2, 12.56)
    tree.add_product(4, 8.2)
    tree.add_product(7, 400)
    tree.add_product(1, 78)
    tree.add_product(3, 100)
    print("Product: ", tree.find_product(4))
    print("Product: ", tree.find_product(9))
    code = 0
    number = 0
    try:
        code = int(input("Enter the code of product: "))
    except TypeError:
        print("Wrong type!")
    try:
        number = int(input("Enter number of products: "))
    except TypeError:
        print("Wrong type!")
    print(tree.total(code, number))


main()
