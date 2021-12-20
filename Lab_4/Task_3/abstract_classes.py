from abc import ABC, abstractmethod


class ICourse(ABC):

    @property
    @abstractmethod
    def name(self):
        """name setter"""
        raise NotImplementedError

    @name.setter
    @abstractmethod
    def name(self, name):
        """name getter"""
        raise NotImplementedError

    @property
    @abstractmethod
    def teacher(self):
        """teacher setter"""
        raise NotImplementedError

    @teacher.setter
    @abstractmethod
    def teacher(self, teacher):
        """teacher getter"""
        raise NotImplementedError

    @property
    @abstractmethod
    def topics(self):
        """topics setter"""
        raise NotImplementedError

    @topics.setter
    @abstractmethod
    def topics(self, topics):
        """topics getter"""
        raise NotImplementedError

    @abstractmethod
    def __str__(self):
        raise NotImplementedError


class ITeacher(ABC):

    @property
    @abstractmethod
    def name(self):
        """name setter"""
        raise NotImplementedError

    @name.setter
    @abstractmethod
    def name(self, name):
        """name getter"""
        raise NotImplementedError

    @property
    @abstractmethod
    def surname(self):
        """surname setter"""
        raise NotImplementedError

    @surname.setter
    @abstractmethod
    def surname(self, surname):
        """surname getter"""
        raise NotImplementedError

    @property
    @abstractmethod
    def phone(self):
        """phone setter"""
        raise NotImplementedError

    @phone.setter
    @abstractmethod
    def phone(self, phone):
        """phone getter"""
        raise NotImplementedError

    @abstractmethod
    def __str__(self):
        raise NotImplementedError


class ILocalCourse(ABC):

    @abstractmethod
    def __str__(self):
        raise NotImplementedError


class IOffsiteCourse(ABC):

    @abstractmethod
    def __str__(self):
        raise NotImplementedError


class ICourseFactory(ABC):

    @abstractmethod
    def create_course(self, c_name, course_type, topics, teacher) -> object:
        """Create and return created course"""
        raise NotImplementedError
