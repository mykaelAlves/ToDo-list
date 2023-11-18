from package.item import Item

class Task(Item):
    def __init__(self, title, deadline, description):
        super().__init__(title, deadline, description)