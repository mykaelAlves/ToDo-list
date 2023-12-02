from datetime import datetime

def __deadline_correct_format(deadline):
    try:    
        datetime.strptime(deadline, "%d/%m/%Y")
        return True
    except Exception as e:
        print(e)
        return False
    
    
def __title_is_null(title):
    return not bool(title.strip())


def __description_exceeded_lenght(description):
    if len(description) >= 200:
        return True
    return False


def check_task(task):
    try:
        if __title_is_null(task.title):
            raise RuntimeWarning("ERROR: TITLE SHOULDN'T BE NULL")
        if not __deadline_correct_format(task.deadline):
            raise RuntimeWarning("ERROR: WRONG DATE FORMAT")
        if __description_exceeded_lenght(task.description):
            raise RuntimeWarning("ERROR: DESCRIPTION IS TOO LONG")
        task.title
    except AttributeError as e:
        raise RuntimeWarning("ERROR: NOTHING WAS SELECTED")
    return True