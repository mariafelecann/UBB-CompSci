from domain.entities import Person
from domain.entities import Activity

class Persons_repo:
    def __init__(self):
        pers1 = Person(0,'Maria Felecan', '0758647475')
        pers2 = Person(1, 'Taylor Swift', '0744492492')
        pers3 = Person(2,'Fuego', '073547794')
        pers4 = Person(3, 'Ioana Gabor', '075537483526')
        pers5 = Person(4, 'Marcel Gabor', '07555364789')
        pers6 = Person(5, 'Georgiana Felecan', '0758934267')
        pers7 = Person(6, 'Isabela Dawer', '07567890765')
        pers8 = Person(7, 'Mircea Eliade', '0756445335')
        pers9 = Person(8, 'Ion Pop', '07345268331')
        pers10 = Person(9, 'Ana Grigore', '0766345221')
        self.all_persons = [pers1, pers2, pers3, pers4, pers5, pers6, pers7, pers8, pers9, pers10]

    def get_list(self):
        return self.all_persons

class Activity_repo:
    def __init__(self):
        act1 = Activity(0,[0],'1.01.2023','18:30', 'New Years Day Party')
        act2 = Activity(1,[0,1],'1.01.2023', '9:45', 'Grocery Shopping')
        act3 = Activity(2,[1], '2.07.2022', '10:30', 'Painting Contest')
        act4 = Activity(3,[2],'25.12.2022', '14:30', 'Christmas Concert')
        act5 = Activity(4, [5, 6, 7], '2.07.2022', '12:50', 'Yoga with friends')
        act6 = Activity(5, [2, 6], '3.05.2023', '10:25', 'Trip to the mountains')
        act7 = Activity(6, [1, 3, 7], '3.05.2023', '18:30', 'Movie Night')
        act8 = Activity(7, [2,8,9], '10.11.2024', '17:20', 'Wedding Attendance')
        act9 = Activity(8, [0, 1 ,9], '2.07.2022', '20:20', 'Friend Night')
        self.all_activities = [act1, act2, act3, act4, act5, act6, act7, act8, act9]

    def get_list(self):
        return self.all_activities

