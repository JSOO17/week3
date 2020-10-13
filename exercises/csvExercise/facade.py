from exercises.csvExercise.initialize_csv import InitializeCsv


class FacadeClass:
    def __init__(self):
        self.df = InitializeCsv()

    def get_employees(self):
        return self.df.reader

    def add_employee(self, employee):
        return self.df.add_employee(employee)
