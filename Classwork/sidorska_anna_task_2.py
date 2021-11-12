from datetime import datetime


class Time:
    def __init__(self):
        current_time = datetime.now()
        self.__hours = current_time.hour
        self.__minutes = current_time.minute
        self.__seconds = current_time.second

    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, hours):
        if not isinstance(hours, int) and not hours:
            raise TypeError
        if not 0 <= hours <= 23:
            raise ValueError
        self.__hours = hours

    @property
    def minutes(self):
        return self.__minutes

    @minutes.setter
    def minutes(self, minutes):
        if not isinstance(minutes, int) and not minutes:
            raise TypeError
        if not 0 <= minutes <= 59:
            raise ValueError
        self.__minutes = minutes

    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def seconds(self, seconds):
        if not isinstance(seconds, int) and not seconds:
            raise TypeError
        if not 0 <= seconds <= 59:
            raise ValueError
        self.__seconds = seconds

    def add(self):
        if self.__hours + 1 >= 60:
            self.__hours = 00
        else:
            self.__hours += 1
        if self.__minutes + 1 >= 60:
            self.__minutes = 00
        else:
            self.__seconds += 1
        if self.__seconds + 1 >= 60:
            self.__seconds = 00
        else:
            self.__minutes += 1

    def __str__(self):
        return f"{self.__hours} hours, {self.__minutes} minutes, {self.__seconds} seconds"


def main():
    time = Time()
    time.add()
    print(time)


main()
