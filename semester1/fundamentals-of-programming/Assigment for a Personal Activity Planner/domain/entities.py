"""
This file contains the entities needed for the app
"""


class Person:
    def __init__(self, person_id, name, phone_number):
        self.__person_id = person_id
        self.__name = name
        self.__phone_number = phone_number

    def get_person_id(self):
        return self.__person_id

    def set_person_id(self, person_id):
        self.__person_id = person_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def __str__(self):
        return f'person_id = {self.__person_id}, name = {self.__name}, phone_number = {self.__phone_number}'


class Activity:

    def __init__(self, activity_id, person_id, date, time, description):
        self.__activity_id = activity_id
        self.__person_id = person_id
        self.__date = date
        self.__time = time
        self.__description = description

    def get_activity_id(self):
        return self.__activity_id

    def set_activity_id(self, activity_id):
        self.__activity_id = activity_id

    def get_person_id(self):
        return self.__person_id

    def set_person_id(self, person_id):
        self.__person_id = person_id

    def get_date(self):
        return self.__date

    def set_date(self, date):
        self.__date = date

    def get_time(self):
        return self.__time

    def set_time(self, time):
        self.__time = time

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def __str__(self):
        return f'activity_id = {self.__activity_id}, person_id = {self.__person_id}, date = {self.__date},  time = {self.__time}, description = {self.__description}'