from tabulate import tabulate
from exercises.csvExercise.read_context_manager import initialize_writer, ReaderContextManager, writer_csv


class InitializeCsv:
    def __init__(self):
        self.reader = self.init_reader()
        initialize_writer(writer_csv)

    @staticmethod
    def init_reader() -> list:
        with ReaderContextManager() as read:
            return read

    def add_employee(self, employee: dict):
        initialize_writer(lambda writer: writer.writerow(employee), mode='a')
        self.reader = self.init_reader()
