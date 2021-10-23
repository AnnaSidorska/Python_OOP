import re


class Product:
    """
    This class represents a product.
    """
    def __init__(self, product_name, price, description):
        self.product_name = product_name
        self.price = price
        self.description = description

    @property
    def product_name(self):
        return self.__product_name

    @product_name.setter
    def product_name(self, product_name):
        if not isinstance(product_name, str):
            raise TypeError("Product name must have string type!")
        if not product_name:
            raise ValueError("Product name isn't specified!")
        self.__product_name = product_name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be int or float type!")
        if not price:
            raise ValueError("Price isn't specified!")
        if price <= 0:
            raise ValueError("Price can't be a negative number!")
        self.__price = price

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        if not isinstance(description, str):
            raise TypeError("Description must have string type!")
        if not description:
            raise ValueError("Description is not specified!")
        self.__description = description

    def __str__(self):
        return f'Product name: {self.__product_name}\nPrice: {self.__price}\nDescription: {self.__description}'


class Customer:
    """
    This class represents a customer.
    """
    def __init__(self, name, surname, phone):
        self.__name = name
        self.__surname = surname
        self.__phone = phone

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Customer's name must have string type!")
        if not name:
            raise ValueError("Customer's name can't be empty!")
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError("Customer's surname must have string type!")
        if not surname:
            raise ValueError("Customer's surname can't be empty!")
        self.__surname = surname

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        if not isinstance(phone, str):
            raise TypeError("Customer's phone number must have string type!")
        mask = re.compile("^[+]380[0-9]{9}$")
        if not mask.match(phone):
            raise ValueError("Invalid phone number format!")
        self.__phone = phone

    def __str__(self):
        return f'Name: {self.__name} {self.__surname} Phone: {self.__phone}'


class Order:
    """
    This class represents an order.
    """
    def __init__(self, customer, *product):
        self.__customer = customer
        self.__products = list(product)

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, customer):
        self.__customer = customer

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, value):
        self.__products = list(value)

    def add_product(self, value):
        self.products.append(value)

    def remove_product(self, value):
        self.products.remove(value)

    def total_sum(self):
        total_sum = 0
        for prod in self.__products:
            total_sum += prod.price
        return total_sum

    def __str__(self):
        list_products = '\n'.join(list(map(str, self.products)))
        return f'Customer:\n{self.__customer}\nProducts:\n{list_products}'


def main():
    customer1 = Customer("Julia", "Silpo", "+380669944566")
    product1 = Product("Waffles", 27.89, "Large")
    order1 = Order(customer1, product1)
    product2 = Product("Cookies", 21.99, "Tasty")
    product3 = Product("Ochkolamp", 69.69, "Animal")
    order1.add_product(product2)
    order1.add_product(product3)
    print(order1)
    print("Total order value:", round(order1.total_sum(), 2))


main()
