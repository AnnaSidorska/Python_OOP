import re


class Person:
    def __init__(self, name, surname, number_phone, birthday):
        self.name = name
        self.surname = surname
        self.number_phone = number_phone
        self.birthday = birthday

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must has a string type!")
        if not name:
            raise ValueError("Name can't be empty!")
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError("Surname must has a string type!")
        if not surname:
            raise ValueError("Surname can't be empty!")
        self.__surname = surname

    @property
    def number_phone(self):
        return self.__number_phone

    @number_phone.setter
    def number_phone(self, number_phone):
        if not isinstance(number_phone, str):
            raise TypeError("Phone number must have string type!")
        mask = re.compile("^[+]380[0-9]{9}$")
        if not mask.match(number_phone):
            raise ValueError("Invalid phone number format!")
        self.__number_phone = number_phone

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, birthday):
        if not isinstance(birthday, str):
            raise TypeError("Birthday must have a date type.")
        mask = re.compile("^[0-3][0-9]/[0-3][0-9]/[0-9]{4}$")
        if not mask.match(birthday):
            raise ValueError("Invalid date format!")
        if not birthday:
            raise ValueError("Field birthday can't be empty.")
        self.__birthday = birthday

    def __str__(self):
        return f'Name: {self.name}, surname: {self.surname}, phone: {self.number_phone}, birthday: {self.birthday}'


class Notebook:
    def __init__(self, *record):
        self.record = list(record)

    @property
    def record(self):
        return self.__record

    @record.setter
    def record(self, record):
        if isinstance(all(record), Person):
            raise TypeError("Records mush have type of Person.")
        self.__record = list(record)

    def __sub__(self, other):
        new_records = self.__record.copy()
        try:
            for item in new_records:
                new_records.remove(item)
        except Exception as e:
            print(e)
        return Notebook(list(map(str, new_records)))

    def __add__(self, other):
        new_records = self.__record.copy()
        new_records.append(other)
        return Notebook(list(map(str, new_records)))

    def __mul__(self, other):
        result = []
        if not isinstance(other, dict):
            raise TypeError('Given argument must be a dict.')
        if not all(i in ('name', 'surname', 'phone', 'birthday') for i in list(other.keys())):
            raise ValueError('No such data field.')
        for record in self.__record:
            if all(other[field] == self.find(record, field) for field in list(other.keys())):
                result.append(record)
        return result

    @staticmethod
    def find(record, field):
        return eval('record.' + field)

    def __str__(self):
        return '\n'.join(list(map(str, self.__record)))


def main():
    p1 = Person("Daniil", "Dankovsky", "+380678923165", '24/08/1999')
    p2 = Person("Artemy", "Vorakh", "+380938452789", '04/07/1995')
    p3 = Person("Klara", "Saburova", "+380661234567", '16/12/2002')
    d = Notebook(p1, p2)
    print(d, '\n')
    print("Add record:", d + p3)
    print("Remove record:", d - p1)
    for record in d * {'surname': 'Vorakh'}:
        print(record)


main()
