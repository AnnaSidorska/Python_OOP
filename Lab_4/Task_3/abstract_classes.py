from abc import ABC, abstractmethod


class ICourseFactory(ABC):
    @abstractmethod
    def create_course(self, c_name, course_type, topics, teacher) -> object:
        pass


class ICourse(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, name):
        pass

    @property
    @abstractmethod
    def teacher(self):
        pass

    @teacher.setter
    @abstractmethod
    def teacher(self, teacher):
        pass

    @property
    @abstractmethod
    def topics(self):
        pass

    @topics.setter
    @abstractmethod
    def topics(self, topics):
        pass

    @abstractmethod
    def __str__(self):
        pass


class ITeacher(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, name):
        pass

    @property
    @abstractmethod
    def surname(self):
        pass

    @surname.setter
    @abstractmethod
    def surname(self, surname):
        pass

    @property
    @abstractmethod
    def phone(self):
        pass

    @phone.setter
    @abstractmethod
    def phone(self, phone):
        pass

    @abstractmethod
    def __str__(self):
        pass


class ILocalCourse(ABC):
    @abstractmethod
    def __str__(self):
        pass


class IOffsiteCourse(ABC):
    @abstractmethod
    def __str__(self):
        pass
