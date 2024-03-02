import unittest

from exceptions.exceptions import *
from services.services import Services
from domain.entities import *
from repository.functions_repo import *


class Tests(unittest.TestCase):
    def test_add_person(self):
        """"
        Tests the add_person method
        """
        persons = []
        activities = []
        service = Services(persons, activities)
        service.add_person(1, "P1", "T1")
        self.assertEqual(len(service.get_persons()), 1)
        self.assertEqual(service.get_persons()[0].get_person_id(), 1)
        self.assertEqual(service.get_persons()[0].get_name(), "P1")
        self.assertEqual(service.get_persons()[0].get_phone_number(), "T1")
        with self.assertRaises(UniqueError):
            service.add_person(1, "P2", "T2")

    def test_add_activity(self):
        """"
        Tests the add_activity method
        """
        persons = []
        activities = []
        service = Services(persons, activities)
        service.add_activity(1,1, "D1","T1","DE1")
        self.assertEqual(len(service.get_activities()), 1)
        self.assertEqual(service.get_activities()[0].get_activity_id(), 1)
        self.assertEqual(service.get_activities()[0].get_person_id(), 1)
        self.assertEqual(service.get_activities()[0].get_date(), "D1")
        self.assertEqual(service.get_activities()[0].get_time(), "T1")
        self.assertEqual(service.get_activities()[0].get_description(), "DE1")
        with self.assertRaises(UniqueError):
            service.add_activity(1, "D2", "T2", "DE2")

    def test_rem_person(self):
        """"
        Tests the rem_person method
        """
        persons = []
        activities = []
        service = Services(persons, activities)
        service.add_person(1, "P1", "T1")
        service.remove_person(1)
        self.assertEqual(len(service.get_persons()), 0)
        with self.assertRaises(ExistenceError):
            service.remove_person(2)

    def test_rem_activity(self):
        """"
        Tests the rem_activity method
        """
        persons = []
        activities = []
        service = Services(persons, activities)
        service.add_activity(1, 1, "D1", "T1", "DE1")
        service.remove_activity(1)
        self.assertEqual(len(service.get_activities()), 0)
        with self.assertRaises(ExistenceError):
            service.remove_activity(2)

    def test_upd_person(self):
        """"
        Tests the upd_person method
        """
        persons = []
        activities = []
        service = Services(persons, activities)
        service.add_person(1, "P1", "T1")
        service.update_person(1, "S2", "T2")
        self.assertEqual(service.get_persons()[0].get_name(), "S2")
        self.assertEqual(service.get_persons()[0].get_phone_number(), "T2")
        with self.assertRaises(ExistenceError):
            service.update_person(2, "S3", "T3")

    def test_upd_activity(self):
        """"
        Tests the upd_activity method
        """
        persons = []
        activities = []
        service = Services(persons, activities)
        service.add_activity(1, 1, "D1", "T1", "DE1")
        service.update_activity(1,1, "D2", "T2", "DE2")
        self.assertEqual(service.get_activities()[0].get_date(), "D2")
        self.assertEqual(service.get_activities()[0].get_time(), "T2")
        self.assertEqual(service.get_activities()[0].get_description(), "DE2")
        with self.assertRaises(ExistenceError):
            service.update_activity(2, "D3", "T3", "DE3")

    def test_save_person_repo(self):
        """"
        Tests the save method from the person repository
        """
        persons = []
        person_repo = Person_Repository(persons)
        person = Person(1,"N1", "P1")
        person_repo.save(person)
        self.assertEqual(len(persons), 1)
        self.assertEqual(persons[0].get_name(), "N1")
        self.assertEqual(persons[0].get_phone_number, "P1")
        with self.assertRaises(UniqueError):
            person2 = Person(1,"N2", "P2")
            person_repo.save(person2)

    def test_save_activity_repo(self):
        """"
        Tests the save method from the activity repository
        """
        activ = []
        activ_repo = Activity_Repository(activ)
        activity = Activity(1, 1, "D1", "T1", "DE1")
        activ_repo.save(activity)
        self.assertEqual(len(activ), 1)
        self.assertEqual(activ[0].get_date(), "D1")
        self.assertEqual(activ[0].get_time(), "T1")
        self.assertEqual(activ[0].get_description(), "DE1")
        with self.assertRaises(UniqueError):
            activ2 = Activity(1, "D2", "T2", "DE2")
            activ_repo.save(activ2)

    def test_upd_person_repo(self):
        """"
        Tests the update method from the person repository
        """
        persons = []
        person_repo = Person_Repository(persons)
        person = Person(1, "N1", "P1")
        person_repo.save(person)
        person2 = Person(1, "N2", "P2")
        person_repo.update(1, person2)
        self.assertEqual(persons[0].get_name(), "N2")
        self.assertEqual(persons[0].get_phone_number, "P2")
        with self.assertRaises(ExistenceError):
            person_repo.update(2, person)

    def test_upd_activity_repo(self):
        """"
        Tests the update method from the activity repository
        """
        activ = []
        activ_repo = Activity_Repository(activ)
        activity = Activity(1, 1, "D1", "T1", "DE1")
        activ_repo.save(activity)
        activity2 = Activity(1, 1, "D2", "T2", "DE2")
        activ_repo.update(1,activity2)
        self.assertEqual(activ[0].get_date(), "D2")
        self.assertEqual(activ[0].get_time(), "T2")
        self.assertEqual(activ[0].get_description(), "DE2")
        with self.assertRaises(ExistenceError):
            activ_repo.update(3, activity)


    def test_delete_person_repo(self):
        """"
        Tests the delete method from the person repository
        """
        persons = []
        person_repo = Person_Repository(persons)
        person = Person(1, "N1", "P1")
        person_repo.save(person)
        person_repo.delete_by_id(1)
        self.assertEqual(len(persons), 0)
        with self.assertRaises(ExistenceError):
            person_repo.delete_by_id(2)

    def test_delete_activity_repo(self):
        """"
        Tests the delete method from the activity repository
        """
        activities = []
        activ_repo = Activity_Repository(activities)
        activity = Activity(1, 1, "D1", "T1", "DE1")
        activ_repo.save(activity)
        activ_repo.delete_by_id(1)
        self.assertEqual(len(activities), 0)
        with self.assertRaises(ExistenceError):
            activ_repo.delete_by_id(2)

unittest.main()