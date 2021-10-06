class Product:
    def __init__(self, price, description):
        self.__price = price
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be int of float.")
        self.__description = description

    def get_price(self):
        return self.__price

    def get_description(self):
        return self.__description


class Customer:
    def __init__(self, name, surname, mobile_phone):
        self.__name = name
        self.__surname = surname
        self.__mobile_phone = mobile_phone

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_phone(self):
        return self.__mobile_phone


class Order:
    def __init__(self, customer, product):
        self.__customer = customer
        self.__products = []
        self.__products.append(product)

    def calculate_sum(self):
        total_amount = 0
        for temp_prod in self.__products:
            total_amount += temp_prod.get_price()
        return total_amount

    def add_product(self, product):
        self.__products.append(product)

    def output(self):
        for temp_desc in self.__products:
            print('Name of product: ' + temp_desc.get_description())
            print('Price of product: ', temp_desc.get_price())
        print("Customers' name: ", f'{self.__customer.get_name()}')
        print("Customers' surname: ", f'{self.__customer.get_surname()}')


def main():
    product_1 = Product(1599, "IPhone")
    customer_1 = Customer("John", "Pavlovich", 20377)
    order_1 = Order(customer_1, product_1)
    order_1.add_product(Product(150, "Waffles"))
    print('Total price: ', order_1.calculate_sum())
    order_1.output()


main()
