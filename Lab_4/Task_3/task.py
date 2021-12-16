from abstract_classes import *
from config import db
import re

cursor = db.cursor()


class CourseFactory(ICourseFactory):
    def create_course(self, c_name, course_type, topics, teacher):
        if course_type == "Local":
            return LocalCourse(c_name, topics, teacher)
        elif course_type == "Offsite":
            return OffsiteCourse(c_name, topics, teacher)


class Teacher(ITeacher):
    def __init__(self, name, surname, phone):
        self.name = name
        self.surname = surname
        self.phone = phone

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
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        if not isinstance(phone, str):
            raise TypeError("Phone number must have string type!")
        mask = re.compile("^[+]380[0-9]{9}$")
        if not mask.match(phone):
            raise ValueError("Invalid phone number format!")
        self.__phone = phone

    def __str__(self):
        return f'{self.name} {self.surname}, phone: {self.phone}'


class Course(ICourse):
    def __init__(self, name, topics, teacher):
        self.name = name
        self.topics = topics
        self.teacher = teacher

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if not name:
            raise ValueError("Name of the course is empty.")
        self.__name = name

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, teacher):
        if not isinstance(teacher, Teacher):
            raise TypeError("Teacher must be a Teacher.")
        if not teacher:
            raise ValueError("Teacher of the course is empty.")
        self.__teacher = teacher

    @property
    def topics(self):
        return self.__topics

    @topics.setter
    def topics(self, topics):
        if not isinstance(topics, list):
            raise TypeError("Not list!")
        if not all(isinstance(elem, str) for elem in topics):
            raise ValueError("not string")
        self.__topics = topics

    def __str__(self):
        return f'Course:\n\tName: {self.__name}\n\tTeacher: {self.__teacher}\n\tTopics: {self.__topics}'


class LocalCourse(ILocalCourse, Course):
    def __init__(self, name, topics, teacher):
        super().__init__(name, topics, teacher)
        self.course_type = "Local"

    def __str__(self):
        return f'Local course:\n\tName: {self.name}\n\tTeacher: {self.teacher}\n\tTopics: {self.topics}'


class OffsiteCourse(IOffsiteCourse, Course):
    def __init__(self, name, topics, teacher):
        super().__init__(name, topics, teacher)
        self.course_type = "Offsite"

    def __str__(self):
        return f'Offsite course:\n\tName: {self.name}\n\tTeacher: {self.teacher}\n\tTopics: {self.topics}'


def main():
    t1 = Teacher("Daniil", "Dankovsky", "+380678923165")
    t2 = Teacher("Artemy", "Burakh", "+380932378217")
    c1 = CourseFactory().create_course("Java/Spring",  "Local", ['Java', 'Spring', 'JavaScript'], t1)
    c2 = CourseFactory().create_course("Full-stack Development",  "Offsite", ['Front-end', 'Back-end'], t2)
    # insert = f"INSERT INTO course(Course_name, Course_type, Course_topics, id_teacher) " \
    #          f"VALUES(%s, %s, %s, %s)"
    # val = "Full-stack Development", "Offsite", ', '.join(['Front-end', 'Back-end']), 2
    # cursor.execute(insert, val)
    # db.commit()
    print(c1)
    print(c2)


main()
