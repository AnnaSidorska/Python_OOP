import datetime


class Person:
    """
        This class represents a person.
    """
    def __init__(self, surname, pass_id, education, job, date, occupation, salary):
        self.surname = surname
        self.pass_id = pass_id
        self.education = education
        self.job = job
        self.date = date
        self.occupation = occupation
        self.salary = salary

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError
        if not surname:
            raise ValueError
        self.__surname = surname

    @property
    def pass_id(self):
        return self.__pass_id

    @pass_id.setter
    def pass_id(self, pass_id):
        if not isinstance(pass_id, int):
            raise TypeError
        if pass_id < 0:
            raise ValueError
        if not pass_id:
            raise ValueError
        self.__pass_id = pass_id

    @property
    def education(self):
        return self.__education

    @education.setter
    def education(self, education):
        if not isinstance(education, str):
            raise TypeError
        if not education:
            raise ValueError
        self.__education = education

    @property
    def job(self):
        return self.__job

    @job.setter
    def job(self, job):
        if not isinstance(job, str):
            raise TypeError
        if not job:
            raise ValueError
        self.__job = job

    @property
    def date(self):
        return self._date.strftime('%d.%m.%Y')

    @date.setter
    def date(self, date):
        self._date = datetime.datetime.strptime(date, '%d.%m.%Y')

    @property
    def occupation(self):
        return self.__occupation

    @occupation.setter
    def occupation(self, occupation):
        if not isinstance(occupation, str):
            raise TypeError
        if not occupation:
            raise ValueError
        self.__occupation = occupation

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if not isinstance(salary, (int, float)):
            raise TypeError
        if salary < 0:
            raise ValueError
        if not salary:
            raise ValueError
        self.__salary = salary

    def __str__(self):
        return f'Surname: {self.__surname}\nPassport id: {self.__pass_id}\nEducation: {self.__education}\n' \
               f'Job: {self.__job}\nDate: {self.date}\nOccupation: {self.__occupation}\nSalary: {self.__salary}'


class Queue:
    """
            This class represents a queue of list if person.
        """
    def __init__(self, *person):
        self.person = list(person)

    @property
    def person(self):
        return self.__person

    @person.setter
    def person(self, person):
        if isinstance(all(person), Person):
            raise TypeError
        if not person:
            raise ValueError
        self.__person = list(person)

    def add_person(self, person):
        self.__person.append(person)

    def del_person(self, person):
        self.__person.remove(person)

    def top_salary(self):
        self.__person.sort(key=lambda student: student.salary, reverse=True)
        return self.__person[0]

    def __str__(self):
        queue = '\n'.join(list(map(str, self.person)))
        return f"Queue: \n{queue}\n"


def main():
    p1 = Person("Johnson", 456, "KPI", "Programmer", "13.10.2021", "Team lead", 1500)
    p2 = Person("Suhulov", 123, "KNU", "Cook", "14.10.2021", "Chef", 1000)
    p3 = Person("Kuzik", 777, "NAU", "System admin", "17.12.2020", "Programmer", 14568)
    queue = Queue(p1, p2)
    queue.add_person(p3)
    print(queue)
    print("Best salary:\n", queue.top_salary())


main()
