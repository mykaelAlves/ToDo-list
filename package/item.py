from datetime import date
import time

class Item():
    due = False
    
    def __init__(self, deadline, title, description):
        self.deadline = deadline
        self.title = title
        self.description = description

    def _get_dates(self): #to implement
        pass

    def is_due(self):
        deadline, today_date = self._get_dates()

        if deadline < today_date:
            self.due = True
