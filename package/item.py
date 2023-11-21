from datetime import datetime

class Item():      
    def __init__(self, title, deadline, description):
        self.deadline = deadline
        self.title = title
        self.description = description
        self.__deadline_replace()


    def __deadline_replace(self):
        if self.deadline.lower() == "today":
            self.deadline = datetime.now().strftime("%d/%m/%Y")
            
            return
        if "-" in self.deadline:
            self.deadline = self.deadline.replace("-", "/")
        if ' ' in self.deadline:
            self.deadline = self.deadline.replace(' ', "/")
        if "." in self.deadline:
            self.deadline = self.deadline.replace(".", "/")


    def __get_dates(self):
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
        deadline, today_date = self.__get_dates()

        if deadline < today_date:
            return True

        return False
    

    def is_today(self):
        deadline, today_date = self.__get_dates()

        if deadline.date() == today_date.date():
            return True
        
        return False