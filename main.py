from tabulate import tabulate
from random import randint, choice
from exercises.csvExercise.facade import FacadeClass
from exercises.csvExercise.constants import HEADERS, NAMES, COUNTRIES

facade = FacadeClass()

employees1 = facade.get_employees()


if __name__ == '__main__':

    employee = {'Id': randint(1, 99),
                'Name': 'Yanet',
                'Phone': 3045442343,
                'Address': 'Calle 140 #14-51',
                'Country': 'Francia'}
    facade.add_employee(employee)
    employees2 = facade.get_employees()
    print(tabulate(employees1, headers=HEADERS))
    print(tabulate(employees2, headers=HEADERS))

