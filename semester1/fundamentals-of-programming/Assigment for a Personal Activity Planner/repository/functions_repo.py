
class Person_Repository:

    def __init__(self, all_persons):
         self.__all_persons = all_persons

    def save(self, person):
        """"
        The function saves a new person to the list of all th other existing persons
        :param person: a new person that needs to be appended
        :return nothing
        """
        if self.find_by_id(person.get_person_id()) is not None:
            raise ValueError("Duplicate id")

        self.__all_persons.append(person)

    def find_by_id(self, pers_id):
        """"
        The function finds a person by its id
        :param pers_id: int
        :return the person that has that specific id
        """
        if pers_id - 1 in self.__all_persons:
            return self.__all_persons[pers_id]
        return None

    def update(self, person_id, person):
        """"
        :param person_id: int
        :param person: element of class Person
        :return nothing
        """

        self.__all_persons[person_id] = person

    def delete_by_id(self, person_id):
        """"
        This function deletes a person by its id
        :param person_id: int
        :return nothing
        """

        del self.__all_persons[person_id]



class Activity_Repository:
    def __init__(self, all_activities):
         self.__all_activities = all_activities

    def save(self, activity):
        """"
        The function saves a new activity to the list of all th other existing activities
        :param activity: a new activity that needs to be appended
        :return nothing
        """
        if self.__find_by_id(activity.get_activity_id()) is not None:
            raise ValueError("Duplicate id")

        self.__all_activities.append(activity)

    def __find_by_id(self, activity_id):
        """"
        The function finds an activity by its id
        :param activity_id: int
        :return the activity that has that specific id
        """
        if activity_id in self.__all_activities:
            return self.__all_activities[activity_id]
        return None

    def __find_by_persid(self, pers_id):
        """"
        The function finds an activity by the id of the person that participates in it
        :param pers_id: int
        :return the activity that has that specific id
        """
        if pers_id in self.__all_activities:
            return self.__all_activities[pers_id]
        return None

    def update(self, activity_id, activity):
        """"
        :param activity_id: int
        :param activity: element of class Activity
        :return nothing
        """

        self.__all_activities[activity_id] = activity

    def delete_by_id(self, activity_id):
        """"
        This function deletes an activity by its id
        :param activity_id: int
        :return nothing
        """

        del self.__all_activities[activity_id]

    def delete_by_persid(self, pers_id):
        """"
        This function deletes an activity by its id
        :param pers_id: int
        :return nothing
        """
        if self.__find_by_persid(pers_id) is None:
            raise ValueError("Id was not found!")

        del self.__all_activities[pers_id]



