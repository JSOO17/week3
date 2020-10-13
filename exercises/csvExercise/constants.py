import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'employees.csv')

HEADERS = ["Id", "Name", "Phone", "Address", "Country"]
FILE = my_file
NAMES = ['Jaider', 'Steven', 'Luna', 'Mafe']
COUNTRIES = ['Colombia', 'Mexico', 'Argentina', 'Brazil', 'Chile', 'Peru', 'Espana']
