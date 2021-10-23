class Student:
    """
    This class represents the student.
    """
    all_records = []

    def __init__(self, record, name, surname, grades):
        self.record = record
        self.name = name
        self.surname = surname
        self.grades = grades

    @property
    def record(self):
        return self.__record

    @record.setter
    def record(self, record):
        if not isinstance(record, int):
            raise TypeError("Record book number must must has an int type!")
        if record < 0:
            raise ValueError("Record book number can't be less than zero!")
        self.all_records.append(record)
        self.__record = record

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
    def grades(self):
        return self.__grades

    @grades.setter
    def grades(self, grades):
        if not grades:
            raise ValueError("Grades aren't specified!")
        if not isinstance(grades, dict):
            raise TypeError("All grades must be in a dictionary!")
        if not all(isinstance(grade, int) for grade in grades.values()):
            raise TypeError("Grade must has an int type!")
        if not all(0 <= grade <= 100 for grade in grades.values()):
            raise ValueError("Grade must be in range from 0 to 100!")
        self.__grades = grades

    def average_score(self):
        score = 0
        for value in self.grades.values():
            score += value
        return score / len(self.grades)

    def __str__(self):
        return f'Name: {self.name}\nSurname: {self.surname}\nRecord book: {self.record}\nGrades: {self.grades}'


class Group:
    """
    This class represents the group of students.
    """
    num_of_students = 0
    __duplicate_name = []

    def __init__(self, *student):
        self.__student = list(student)
        for student in self.__student:
            if student.name and student.surname in self.__duplicate_name:
                raise ValueError("Duplicate student's name and surname!")
            self.__duplicate_name.append(student.name + student.surname)
        self.num_of_students += 1
        if self.num_of_students > 20:
            raise ValueError("Group must contain less than 20 students!")

    @property
    def student(self):
        return self.__student

    @student.setter
    def student(self, value):
        if isinstance(all(value), Student):
            raise TypeError("Students mush have type of Student")
        self.__student = list(value)

    def add_student(self, student):
        self.__student.append(student)
        self.num_of_students += 1
        if self.num_of_students > 20:
            raise ValueError("Group must contain less than 20 students!")

    def remove_student(self, student):
        self.__student.remove(student)
        self.num_of_students -= 1

    def top_five(self):
        top = {}
        for student in self.__student:
            top[student.name, student.surname] = student.average_score()
        sort_score = {key: value for key, value in sorted(top.items(), key=lambda item: item[1], reverse=True)}
        return list(sort_score)[0:5]

    def __str__(self):
        list_of_students = '\n'.join(list(map(str, self.student)))
        return f"Students: \n{list_of_students}\n"


def main():
    st1 = Student(123, "Anna", "Kotova", {"Math": 65, "Database": 63, "Java": 78})
    st2 = Student(124, "Julia", "Silpoply", {"Math": 100, "Database": 100, "Java": 100})
    st3 = Student(127, "Ihor", "Silpolevky", {"Math": 79, "Database": 99, "Java": 75})
    st4 = Student(666, "Arthur", "Sarakhman", {"Math": 96, "Database": 98, "Java": 99})
    st5 = Student(100, "Oleh", "Morg", {"Math": 60, "Database": 60, "Java": 59})
    st6 = Student(45, "William", "Os-Brown", {"Math": 69, "Database": 89, "Java": 78})
    group = Group(st1, st2, st3, st4)
    group.add_student(st5)
    group.add_student(st6)
    print(group)
    print("Best students: ", group.top_five())


main()
