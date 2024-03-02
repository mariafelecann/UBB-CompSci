class InvalidPerson(Exception):
    "This person is not in your planner, so it will not be associated with this activity!"
    pass


class InvalidTime(Exception):
    "You already have an activity at this time!"
    pass


class UniqueError(Exception):
    def __init__(self, message):
        super().__init__(message)


class ExistenceError(Exception):
    def __init__(self, message):
        super().__init__(message)
