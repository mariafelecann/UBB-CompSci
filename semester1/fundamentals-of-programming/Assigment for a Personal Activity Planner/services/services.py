"""
This file contains all the services needed for the app to work
"""
from domain.entities import Person
from domain.entities import Activity
from repository.functions_repo import Person_Repository
from repository.functions_repo import Activity_Repository
class Services:
    def __init__(self, all_persons, all_activities):
        self.__all_persons = all_persons
        self.__all_activities = all_activities

    #Adding:

    def add_person(self, id, name, phone):
        """
        Adds a student by calling the student repo
        :param id: int
        :param name: string
        :param phone: string
        :return: None
        """
        person = Person(id, name, phone)
        persons = Person_Repository(self.__all_persons)
        persons.save(person)

    def add_activity(self, id, pers_id, date, time, description):
        """
        Adds an activity by calling the activity repo
        :param id: int
        :param pers_id: list
        :param date: string
        :param time: string
        :param description: string
        :return: None
        """
        activity = Activity(id, pers_id, date, time, description)
        activities = Activity_Repository(self.__all_activities)
        activities.save(activity)

    #Removing:

    def remove_person(self, persid):
        """"
        Removes a person from the person repo and fom the activities repo
        :param persid: int
        :return: None
        """
        persons = Person_Repository(self.__all_persons)
        persons.delete_by_id(persid)


    def remove_activity(self, activ_id):
        """"
        Removes an activity from the activity repo
        :param activ_id: int
        :return: None
        """
        activities = Activity_Repository(self.__all_activities)
        activities.delete_by_id(activ_id)

    #Updating:

    def update_person(self, persid, name, phone):
        """"
        Updates a person with new values given by the user
        :param persid: int
        :param person: element of the person class
        :return: None
        """
        person = Person(persid, name, phone)
        persons = Person_Repository(self.__all_persons)
        persons.update(persid, person)

    def update_activity(self, activ_id, persid, date, time, description):
        """"
        Updates am activity with new values given by the user
        :param persid: int
        :param activ_id: int
        :param activity: element of the person class
        :return: None
        """
        activity = Activity(activ_id, persid, date, time, description)
        activities = Activity_Repository(self.__all_activities)
        activities.update(activ_id, activity)

    def activ_given_date(self, date):
        actlist = []
        for a in self.__all_activities:
            if a.get_date() == date:
                actlist.append(a)

        for i in range(len(actlist) - 1):
            time = actlist[i].get_time()
            p = time.find(":")
            houri = int(time[:p])
            minutesi = int(time[p + 1:])
            for j in range(i+1, len(actlist)):
                time = actlist[j].get_time()
                p = time.find(":")
                hourj = int(time[:p])
                minutesj = int(time[p+1:])
                if houri > hourj:
                    actlist[i], actlist[j] = actlist[j], actlist[i]
                elif houri == hourj:
                    if minutesi > minutesj:
                        actlist[i], actlist[j] = actlist[j], actlist[i]

        return actlist

    def split_date(self, date):
        """"
        Splits a date into day, month and year
        :param date: string
        :return day, month, year: string
        """
        p = date.find(".")
        day = date[:p]
        date = date[(p+1):]
        p = date.find(".")
        month = date[:p]
        year = date[(p+1):]
        return day, month, year


    def busiest_days(self):
        """"
        Returns a list of the busiest days, in ascending order
        :return dates: the list
        """
        copy = self.__all_activities
        dates = []
        for a in copy:

            date = a.get_date()

            day, month, year = self.split_date(date)
            day = int(day)
            month = int(month)
            year = int(year)

            if (year == 2022 and month == 12 and day >= 19) or (year > 2022):
                ok = 0
                if(len(dates) != 0):
                        for i in range(len(dates)):

                            if a.get_date() == dates[i]:
                                    ok = 1
                        if ok == 0:
                            dates.append(a.get_date())
                else:
                    dates.append(a.get_date())

        elements = []

        for i in range(len(dates)):
            elements.append(0)

        for i in range(len(dates)):
            for a in copy:
                if a.get_date() == dates[i]:
                    elements[i] += 1


        for i in range(len(elements) - 1):
            for j in range(i+1, len(elements)):
                if elements[i] > elements[j]:
                    elements[i], elements[j] = elements[j], elements[i]
                    dates[i], dates[j] = dates[j], dates[i]


        return dates

    def activ_given_pers(self, person):
        """"
        Returns the list of activities in which a given person participates
        person: object of class Person
        :return param activities, the list of activities
        """
        activities = []
        for a in self.__all_activities:
            date = a.get_date()

            day, month, year = self.split_date(date)
            day = int(day)
            month = int(month)
            year = int(year)

            if (year == 2022 and month == 12 and day >= 19) or (year > 2022):
                l = a.get_person_id()
                ok = 0
                for i in range(len(l)):
                    l[i] = int(l[i])
                    person = int(person)
                    if l[i] == person:
                        ok = 1
                if ok ==1:
                    activities.append(a)

        return activities

    def search_pers_name(self, name):
        """
        Returns a list of all persons who match the name with the parameter name, case insensitive
        :param name: string
        :return: list
        """
        persons = []
        for i in self.__all_persons:
            if name.upper() in i.get_name().upper():
                persons.append(i)
        return persons

    def search_pers_phone(self, phone):
        """
        Returns a list of all persons who match the phone numbers with the parameter phone, case insensitive
        :param phone: string
        :return: list
        """
        persons = []
        for i in self.__all_persons:
            if phone.upper() in i.get_phone_number().upper():
                persons.append(i)
        return persons

    def search_activ_date(self, date):
        """
        Returns a list of all activities who match the dates with the parameter date, case insensitive
        :param date: string
        :return: list
        """
        activities = []
        for i in self.__all_activities:
            if date.upper() in i.get_date().upper():
                activities.append(i)
        return activities

    def search_activ_time(self, time):
        """
        Returns a list of all activities who match the times with the parameter time, case insensitive
        :param time: string
        :return: list
        """
        activities = []
        for i in self.__all_activities:
            if time.upper() in i.get_time().upper():
                activities.append(i)
        return activities

    def search_activ_description(self, descr):
        """
        Returns a list of all activities who match the description with the parameter descr, case insensitive
        :param descr: string
        :return: list
        """
        activities = []
        for i in self.__all_activities:
            if descr.upper() in i.get_description().upper():
                activities.append(i)
        return activities

    def get_persons(self):
        return self.__all_persons

    def get_activities(self):
        return self.__all_activities




