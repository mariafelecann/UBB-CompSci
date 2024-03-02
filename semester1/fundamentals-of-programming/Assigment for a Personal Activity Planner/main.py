from repository.repository import Persons_repo
from repository.repository import Activity_repo
from ui.ui import UI

persons = Persons_repo()
all_persons = persons.get_list()

activities = Activity_repo()
all_activities = activities.get_list()

ui = UI(all_persons, all_activities)

ui.start()