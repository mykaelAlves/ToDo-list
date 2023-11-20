from package.item import Item

class Task(Item):
    done = False
    
    def __init__(self, title, deadline, description):
        super().__init__(title, deadline, description)

    def set_done(self):
        self.done = True

    def get_done(self):
        if self.done:
            return "DONE"
        
        return "NOT DONE"
        