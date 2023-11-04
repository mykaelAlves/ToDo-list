from package.item import Item

class Habit(Item):
    def __init__(self, deadline, title, description):
        super().__init__(deadline, title, description)