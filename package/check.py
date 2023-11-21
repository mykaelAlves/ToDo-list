from datetime import datetime

def deadline_format(deadline):
    try:    
        datetime.strptime(deadline, "%d/%m/%Y")
        return True
    except Exception as e:
        print(e)
        return False