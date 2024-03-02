"""""
This file manages the user-interface part of the app
"""

from services.services import Services
from exceptions.exceptions import *
from repository.functions_repo import Person_Repository
from repository.repository import Activity_repo
from domain.entities import Person
from domain.entities import Activity

class UI:

    def __init__(self, all_persons, all_activities):
        self.__service = Services(all_persons, all_activities)

    #MENU:

    def print_menu(self):
        print("WELCOME! :D")
        print("This is your new personal activity planner!")
        print("Here are a few things you can do while using this app: ")
        print("Option 1: Manage persons and activities")
        print("Option 2: Add/Remove activities")
        print("Option 3: Search for persons / activities:")
        print("Option 4: Create statistics")
        print("Option 5: Exit")

    def print_submenu1(self):
        print("Here you can manage the lists of activities and persons.")
        print("Option 1. Add a person")
        print("Option 2. Add an acitvity")
        print("Option 3. Remove a person")
        print("Option 4. Remove an activity")
        print("Option 5. Update a person")
        print("Option 6. Update an activity")
        print("Option 7. List the persons")
        print("Option 8. List the activities")
        print("Option 0. Abandon\n")

    def print_submenu2(self):
        print("Option 1: Add an activity")
        print("Option 2: Remove an activity")

    def print_submenu3(self):
        print("Here you can search for a specific item!")
        print("Option 1: Search for a person")
        print("Option 2: Search for an activity")

    def print_submenu3_persons(self):
        print("You can search for a person using either their name or their phone number!")
        print("Option 1: Search by name")
        print("Option 2: Search by phone number")

    def print_submenu3_activties(self):
        print("You can search for an activity entering either its date, time or description!")
        print("Option 1: Search by date")
        print("Option 2: Search by time")
        print("Option 3: Search by description")

    def print_submenu4(self):
        print("Here you can create statistics from your planner!")
        print("Option 1: See the activities for a given date.")
        print("Option 2: See the busiest days.")
        print("Option 3: See the activities with a given person.")
        print("Option 0: Abandon\n")

    # MANAGE LISTS:

    #add

    def ui_add_person(self):
        try:
            persid = int(input("Input the id of your new person: "))
            name = input("Input the name of your new person: ")
            phone = input("Input the phone number of your new person:")
            self.__service.add_person(persid, name, phone)
            print("Person successfully added!")
        except Exception as e:
            print(e)

    def ui_add_activity(self):
        try:
            actid = int(input("Input the id of your new activity: "))
            persid = list(input("Input the id of your new person: "))
            date = input("Input the date of your new activity: ")
            time = input("Input the time of your new activity: ")
            description = input("Input the description of your new activity:")
            self.__service.add_activity(actid, persid, date, time, description)
            print("Activity successfully added!")
        except Exception as e:
            print(e)

    #remove

    def ui_rem_person(self):
        """
        Removes the person with id=persid from the persons_repo
        :return: None
        """
        persid = input("Please enter the id of the person you wish to remove: ")
        try:
            persid = int(persid)
        except ValueError:
            print("ERROR: Invalid ID :(")
            return
        self.__service.remove_person(persid)
        print("Person was successfully removed!")


    def ui_rem_activity(self):
        """
        Removes the activity with id=activ_id from the activity repo
        :param activ_id: int
        :return: None
        """
        activ_id = int(input("Please enter the id of the activity you wish to remove: "))
        self.__service.remove_activity(activ_id)
        print("Activity was removed successfully ! ")


    #update

    def ui_upd_person(self):
        """
        Sets the name and phone number of person from person repo with id=persid to name and phone
        :return: None
        """
        pers_id = input("Please enter the id of the person you wish to update: ")
        try:
            pers_id = int(pers_id)
        except ValueError:
            print("ERROR: Invalid ID :(")
            return
        name = input("Please enter the new name:")
        phone = input("Please enter the new phone number: ")
        persons = self.__service.get_persons()

        self.__service.update_person(pers_id, name, phone)
        print("The person was updated! ")

    def ui_upd_activity(self):
        """
        Sets the name and phone number of person from person repo with id=persid to name and phone
        :return: None
        """
        act_id = input("Please enter the id of the activity you wish to update: ")
        try:
            act_id = int(act_id)
        except ValueError:
            print("ERROR: Invalid ID :(")
            return

        persid = input("Please enter the id of the person that participates in this activity: ")
        try:
            persid = int(persid)
        except ValueError:
            print("ERROR: Invalid ID :(")
            return
        persons = self.__service.get_persons()

        date = input("Please enter the new date: ")
        time = input("Please enter the new time: ")
        description = input("Please enter the new description: ")

        self.__service.update_activity(act_id, persid,date,  time, description)
        print("Activity was updated! ")

    #printing

    def ui_list_persons(self):
        persons = self.__service.get_persons()
        for p in persons:
            print(p)

    def ui_list_activities(self):
        activities = self.__service.get_activities()
        for a in activities:
            print(a)


    def ui_manage_lists(self):
        while True:
            self.print_submenu1()
            choice2 = input("Please enter your choice: ")
            if choice2 == "1":
                self.ui_add_person()
            elif choice2 == "2":
                self.ui_add_activity()
            elif choice2 == "3":
                self.ui_rem_person()
            elif choice2 == "4":
                self.ui_rem_activity()
            elif choice2 == "5":
                self.ui_upd_person()
            elif choice2 == "6":
                self.ui_upd_activity()
            elif choice2 == "7":
                self.ui_list_persons()
            elif choice2 == "8":
                self.ui_list_activities()
            elif choice2 == "0":
                break
            else:
                print("Invalid choice")

    # ADDING AN ACTIVITY

    def add_activity(self):
        aid = input("Please enter the id of your activity: ")
        try:
            aid = int(aid)
        except ValueError:
            print("ERROR: Invalid ID :(")
            return
        num = int(input("Please enter how many persons you wish to add to this activity: "))
        persons = []
        all_persons = self.__service.get_persons()
        print("Please enter the IDs of these persons: ")
        try:
            for i in range(num):
                persid = input()
                try:
                    persid = int(persid)
                except ValueError:
                    print("ERROR: Invalid ID :(")
                    return
                ok = 0
                for i in range(len(all_persons)):
                    if all_persons[i].get_person_id() == persid:
                        ok = 1
                if ok == 0:
                    raise InvalidPerson
                else:
                    persons.append(persid)
        except InvalidPerson:
            print("Error occurred: The id of the person is not valid.")
        try:
            date = input("Please enter the date for your new activity: ")
            time = input("Please enter the time for your new activity: ")
            activities = self.__service.get_activities()
            for a in activities:
                if a.get_time() == time and a.get_date() == date:
                    raise InvalidTime
            description = input("Please enter the description of your new activity: ")
            self.__service.add_activity(aid, persons, date, time, description)
            print("Activity successfully added! :D")
        except InvalidTime:
            print("Error occurred: You already have an activity at this time.")


    #SEARCHING

    def searching(self):
        print(self.print_submenu3())

        choice = input("Please enter your choice: ")

        if choice == "1":
            print(self.print_submenu3_persons())
            c = input("Please enter your choice: ")
            if c == "1":
                name = input("Please enter the name of the person: ")
                persons = self.__service.search_pers_name(name)
                for p in persons:
                    print(p)
            elif c == "2":
                phone = input("Please enter the phone number of your person: ")
                persons = self.__service.search_pers_phone(phone)
                for p in persons:
                    print(p)
            else:
                print("Oops! Invalid choice :(")


        elif choice == "2":
            print(self.print_submenu3_activties())
            c = input("Please enter your choice: ")
            if c == "1":
                date = input("Please enter the date of your activity: ")
                activ = self.__service.search_activ_date(date)
                for a in activ:
                    print(a)
            elif c == "2":
                time = input("Please enter the time of your activity: ")
                activ = self.__service.search_activ_time(time)
                for a in activ:
                    print(a)
            elif c == "3":
                description = input("Please enter the description of your activity: ")
                activ = self.__service.search_activ_description(description)
                for a in activ:
                    print(a)
            else:
                print("Oops! Invalid choice :(")


    #STATISTICS

    def activ_given_date(self):
        date = input("Please enter the date: ")
        activities = self.__service.activ_given_date(date)
        for a in activities:
            print(a)

    def busiest_days(self):
        print(self.__service.busiest_days())

    def activ_given_pers(self):
        person = input("Please enter the ID of the person: ")
        activities = self.__service.activ_given_pers(person)
        for a in activities:
            print(a)

    def statistics(self):
        while True:
            self.print_submenu4()
            choice = input("Please enter your choice: ")
            if choice == "1":
                self.activ_given_date()
            elif choice == "2":
                self.busiest_days()
            elif choice == "3":
                self.activ_given_pers()
            elif choice == "0":
                break
            else:
                print("Oops! Invalid choice :(")

    #CONSOLE

    def console(self):
        while True:
            self.print_menu()
            choice = int(input("Please enter your choice: "))
            if choice == 1:
                self.ui_manage_lists()
            elif choice == 2:
                self.print_submenu2()
                c = input("Enter your choice: ")
                if c == "1":
                    self.add_activity()
                elif c == "2":
                    self.ui_rem_activity()
                else:
                    print("Oops! Invalid choice :(")
            elif choice == 3:
                self.searching()
            elif choice == 4:
                self.statistics()
            elif choice == 5:
                print("Thanks for using this program ! :D ")
                break
            else:
                print("Oops! Invalid choice! Please try again :( ")

    def start(self):
        self.console()