from datetime import datetime
import time

class Item():
    due = False
    
    def __init__(self, title, deadline, description):
        self.deadline = deadline
        self.title = title
        self.description = description

    def _get_dates(self):
        deadline = self.deadline.split("/");
        deadline = [x for x in deadline if x != '']

        j = 0

        for i in deadline:   
            deadline[j] = int(i)
            j+=1

        deadline = datetime(deadline[2], deadline[1], deadline[0])
        today = datetime.now()

        return deadline, today
        

    def is_due(self):
        deadline, today_date = self._get_dates()

        if deadline < today_date:
            self.due = True

        return self.due
    
    def is_today(self):
        deadline, today_date = self._get_dates()

        if deadline.date() == today_date.date():
            return True