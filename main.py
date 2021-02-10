from datetime import datetime
from application.directory_db.people import get_employees
from application.salary import calculate_salary

dt = datetime.now()

print(dt)
if __name__ == '__main__':
    get_employees()
    calculate_salary()
