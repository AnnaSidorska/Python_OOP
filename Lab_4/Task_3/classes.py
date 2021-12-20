from abstract_classes import *
from config import db
import re

cursor = db.cursor()


class Teacher(ITeacher):
    """
    Class represents a teacher, contains name, surname, phone.
    Implements ITeacher.
    """

    def __init__(self, name, surname, phone):
        self.name = name
        self.surname = surname
        self.phone = phone

    @property
    def name(self):
        """name getter"""
        return self.__name

    @name.setter
    def name(self, name):
        """name setter"""
        if not isinstance(name, str):
            raise TypeError("Name must has a string type!")
        if not name:
            raise ValueError("Name can't be empty!")
        self.__name = name

    @property
    def surname(self):
        """surname getter"""
        return self.__surname

    @surname.setter
    def surname(self, surname):
        """surname setter"""
        if not isinstance(surname, str):
            raise TypeError("Surname must has a string type!")
        if not surname:
            raise ValueError("Surname can't be empty!")
        self.__surname = surname

    @property
    def phone(self):
        """phone getter"""
        return self.__phone

    @phone.setter
    def phone(self, phone):
        """phone setter"""
        if not isinstance(phone, str):
            raise TypeError("Phone number must have string type!")
        mask = re.compile("^[+]380[0-9]{9}$")
        if not mask.match(phone):
            raise ValueError("Invalid phone number format!")
        self.__phone = phone

    def __str__(self):
        return f'{self.name} {self.surname}, phone: {self.phone}'


class Course(ICourse):
    """
    Class represents a course, contains name, teacher, topics.
    Implements ICourse.
    """

    def __init__(self, name, topics, teacher):
        self.name = name
        self.topics = topics
        self.teacher = teacher

    @property
    def name(self):
        """name getter"""
        return self.__name

    @name.setter
    def name(self, name):
        """name setter"""
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if not name:
            raise ValueError("Name of the course is empty.")
        self.__name = name

    @property
    def teacher(self):
        """teacher getter"""
        return self.__teacher

    @teacher.setter
    def teacher(self, teacher):
        """teacher setter"""
        if not isinstance(teacher, Teacher):
            raise TypeError("Teacher must be a Teacher.")
        if not teacher:
            raise ValueError("Teacher of the course is empty.")
        self.__teacher = teacher

    @property
    def topics(self):
        """topics getter"""
        return self.__topics

    @topics.setter
    def topics(self, topics):
        """topics setter"""
        if not isinstance(topics, list):
            raise TypeError("Not list!")
        if not all(isinstance(elem, str) for elem in topics):
            raise ValueError("Not string!")
        self.__topics = topics

    def __str__(self):
        return f'Course:\n\tName: {self.__name}\n\tTeacher: {self.__teacher}\n\tTopics: {self.__topics}'


class LocalCourse(ILocalCourse, Course):
    """
    Class contains information about local course.
    Implements ILocalCourse, Course.
    """

    def __init__(self, name, topics, teacher):
        super().__init__(name, topics, teacher)
        self.course_type = "Local"

    def __str__(self):
        return f'Local course:\n\tName: {self.name}\n\tTeacher: {self.teacher}\n\tTopics: {self.topics}'


class OffsiteCourse(IOffsiteCourse, Course):
    """
    Class contains information about offsite course.
    Implements IOffsiteCourse, Course.
    """

    def __init__(self, name, topics, teacher):
        super().__init__(name, topics, teacher)
        self.course_type = "Offsite"

    def __str__(self):
        return f'Offsite course:\n\tName: {self.name}\n\tTeacher: {self.teacher}\n\tTopics: {self.topics}'


class CourseFactory(ICourseFactory):
    """
    Class contains methods for course factory.
    """

    def create_course(self, c_name, course_type, topics, teacher):
        """Create and return created course"""
        if course_type == "Local":
            return LocalCourse(c_name, topics, teacher)
        elif course_type == "Offsite":
            return OffsiteCourse(c_name, topics, teacher)
        else:
            raise ValueError("Input value is incorrect!")

    @staticmethod
    def add_teacher(Teacher):
        """Add teacher to database"""
        insert = f"INSERT INTO teacher(Teacher_name, Teacher_surname, Teacher_phone) " \
                 f"VALUES(%s, %s, %s)"
        values = Teacher.name, Teacher.surname, Teacher.phone
        cursor.execute(insert, values)
        db.commit()

    @staticmethod
    def add_course(Course):
        """Add course to database"""
        insert = f"INSERT INTO course(Course_name, Course_type, Course_topics, name_teacher) " \
                 f"VALUES(%s, %s, %s, %s)"
        values = Course.name, Course.course_type, ', '.join(Course.topics), Course.teacher.name
        cursor.execute(insert, values)
        db.commit()

    @staticmethod
    def get_courses():
        """Get all courses from database"""
        cursor.execute("SELECT * FROM course")
        all_teachers = cursor.fetchall()
        return '\n'.join(map(str, all_teachers))

    @staticmethod
    def get_teachers():
        """Get all teachers from database"""
        cursor.execute("SELECT * FROM teacher")
        all_teachers = cursor.fetchall()
        return '\n'.join(map(str, all_teachers))

    @staticmethod
    def find_course(value):
        """Find course by teacher's name"""
        select = "SELECT * FROM course WHERE name_teacher = %s"
        name = (value,)
        cursor.execute(select, name)
        result = cursor.fetchall()
        return '\n'.join(map(str, result))
