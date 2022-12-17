from applicacion.salary import calculate_salary
from applicacion.db.people import get_employees
from datetime import date

if __name__ == '__main__':
    calculate_salary()
    get_employees()

dt = date.today()
print(dt)
