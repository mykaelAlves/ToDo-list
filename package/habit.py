from package.item import Item

class Habit(Item):
    def __init__(self, deadline, title, description, day_of_week):
        super().__init__(deadline, title, description)
        self.day_of_week = day_of_week

    def next_day():
        pass