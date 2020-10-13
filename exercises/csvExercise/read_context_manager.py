import csv
from random import randint, choice
from exercises.csvExercise.constants import FILE, HEADERS, NAMES, COUNTRIES
from exercises.csvExercise.log import Log

log = Log()


def ignore_first(read) -> list:
    df = list(read)
    if df:
        df.pop(0)
    return df


class ReaderContextManager:
    def __enter__(self):
        try:
            with open(FILE, encoding="utf8") as f:
                reader = ignore_first(csv.reader(f))
                return reader
        except UnicodeDecodeError:
            log.error("could not fetching")

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def writer_csv(writer):
    ids = []
    times_id = 0
    for x in range(0, 10):
        id = randint(1, 99)
        if id not in ids:
            ids.append(id)
            dict_employees = {'Id': id,
                              'Name': choice(NAMES),
                              'Phone': str(randint(3000000000, 3040000000)),
                              'Address': 'Calle 140 #14-51',
                              'Country': choice(COUNTRIES)}
            writer.writerow(dict_employees)
        elif id in ids:
            times_id = times_id + 1
            log.debug(str(f"{id} ya existe"))
    log.info(str(f"{times_id} repeat"))


def initialize_writer(function, mode='w') -> None:
    try:
        with open(FILE, mode, newline="") as f:
            writer = csv.DictWriter(f, fieldnames=HEADERS, delimiter=',')
            if mode == 'w':
                writer.writeheader()

            function(writer)
    except UnicodeDecodeError:
        print("could not open")
