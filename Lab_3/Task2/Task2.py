import datetime
import json


class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Customer name must have a string type.")
        if not name:
            raise ValueError("Customer name can't be empty.")
        self.__name = name

    def __str__(self):
        return f'{self.name}'


class Pizza:
    def __init__(self, day, name, price, ingredients):
        self.day = day
        self.name = name
        self.price = price
        self.ingredients = ingredients

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day):
        if not isinstance(day, str):
            raise TypeError("Day must have a string type.")
        if not day:
            raise ValueError("Day can't be empty.")
        self.__day = day

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Pizza name must have a string type.")
        if not name:
            raise ValueError("Pizza name can't be empty.")
        self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError("Price must have a numeric type.")
        if price < 0 and not price:
            raise ValueError("Price can't be negative number.")
        self.__price = price

    @property
    def ingredients(self):
        return self.__ingredients

    @ingredients.setter
    def ingredients(self, ingredients):
        if any(not isinstance(ing, str) for ing in ingredients):
            raise TypeError("Ingredients must have a string type.")
        self.__ingredients = ingredients

    def __str__(self):
        return f'{self.name}, price: {self.price}\nIngredients: {self.ingredients}'

    def get_info(self):
        return {
            "Day": self.day,
            "Name": self.name,
            "Price": self.price,
            "Ingredients": self.ingredients
        }

    @staticmethod
    def get_pizza():
        day = datetime.datetime.today().strftime('%A')
        with open("pizza.json", "r") as f:
            data = json.load(f)
            for i in data["Pizza"]:
                if i["Day"] == day:
                    return Pizza(day, i["Name"], i["Price"], i["Ingredients"])


class MondayPizza(Pizza):
    def __init__(self, name, price, ingredients):
        super().__init__("Monday", name, price, ingredients)

    def __str__(self):
        return f'Monday pizza {self.name}, price: {self.price}\nIngredients: {self.ingredients}'


class TuesdayPizza(Pizza):
    def __init__(self, name, price, ingredients):
        super().__init__("Tuesday", name, price, ingredients)

    def __str__(self):
        return f'Tuesday pizza {self.name}, price: {self.price}\nIngredients: {self.ingredients}'


class WednesdayPizza(Pizza):
    def __init__(self, name, price, ingredients):
        super().__init__("Wednesday", name, price, ingredients)

    def __str__(self):
        return f'Wednesday pizza {self.name}, price: {self.price}\nIngredients: {self.ingredients}'


class ThursdayPizza(Pizza):
    def __init__(self, name, price, ingredients):
        super().__init__("Thursday", name, price, ingredients)

    def __str__(self):
        return f'Thursday pizza {self.name}, price: {self.price}\nIngredients: {self.ingredients}'


class FridayPizza(Pizza):
    def __init__(self, name, price, ingredients):
        super().__init__("Friday", name, price, ingredients)

    def __str__(self):
        return f'Friday pizza {self.name}, price: {self.price}\nIngredients: {self.ingredients}'


class SaturdayPizza(Pizza):
    def __init__(self, name, price, ingredients):
        super().__init__("Saturday", name, price, ingredients)

    def __str__(self):
        return f'Saturday pizza {self.name}, price: {self.price}\nIngredients: {self.ingredients}'


class SundayPizza(Pizza):
    def __init__(self, name, price, ingredients):
        super().__init__("Sunday", name, price, ingredients)

    def __str__(self):
        return f'Sunday pizza {self.name}, price: {self.price}\nIngredients: {self.ingredients}'


class Order:
    ingredients = {
        "Pepperoni": 25,
        "Mozzarella": 20,
        "Mushrooms": 30,
        "Sauce": 10,
        "Bacon": 35,
        "Olives": 12,
        "Tomato": 17
    }

    def __init__(self, customer, pizza):
        self.customer = customer
        self.pizza = pizza

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("Customer in order must have type of Customer.")
        if not customer:
            raise ValueError("No customer!")
        self.__customer = customer

    @property
    def pizza(self):
        return self.__pizza

    @pizza.setter
    def pizza(self, pizza):
        if not isinstance(pizza, Pizza):
            raise TypeError("Pizza in order must have type of Pizza.")
        if not pizza:
            raise ValueError("No pizza!")
        self.__pizza = pizza

    def make_order(self):
        print(f'Hello, {self.customer.name}!\n'
              f'Today is {self.pizza.day}. Pizza of the day: {str(self.pizza)}')
        if input(f'Add some ingredients? (Y/N) ').lower() == "y":
            print(self.ingredients)
            for ing in self.ingredients:
                if input(f'Add {ing}? (Y/N) ').lower() == "y":
                    self.pizza.ingredients.append(ing)
                    self.pizza.price += self.ingredients[ing]
        print('Your pizza is ' + str(self.pizza))

    def __str__(self):
        return f'Customer: {self.customer}, pizza: {self.pizza}'


class FileHandle:
    @staticmethod
    def add_information():
        week = [
            MondayPizza("Margherita", 120, ["Mozzarella", "Basil"]),
            TuesdayPizza("Pepperoni", 115, ["Sauce", "Cheese"]),
            WednesdayPizza("Mexican", 140, ["Olives", "Tomato"]),
            ThursdayPizza("Four-cheese", 155, ["Mozzarella", "Gorgonzola"]),
            FridayPizza("Supreme", 130, ["Bacon", "Onion"]),
            SaturdayPizza("Hawaiian", 120, ["Ham", "Pineapple"]),
            SundayPizza("BBQ", 150, ["Pepperoni", "Ham"])
        ]
        information = {"Pizza": []}
        for i in week:
            information["Pizza"].append(i.get_info())
        with open("pizza.json", "w") as f:
            json.dump(information, f)


def main():
    customer = Customer("Daniil")
    Order(customer, Pizza.get_pizza()).make_order()


main()
