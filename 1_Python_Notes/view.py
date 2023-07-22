# Viewer - data display and user interaction

import time


class View:
    def __init__(self):
        pass

    @staticmethod
    def menu():                                                         # Menu bar
        print('Menu:')
        print('\t 1 - add (Add a new note)')
        print('\t 2 - edit (Edit note)')
        print('\t 3 - del  (Delete note)')
        print('\t 4 - list (Displaying a list of notes)')
        print('\t 5 - save (Save the database to a file)')
        print('\t 6 - load (Load database from file)')
        print('\t 7 - info (About the application)')
        print('\t 8 - exit (Exit from the application)')

    @staticmethod
    def print(text):                              
        print(text)

    @staticmethod
    def note_id():                                                       # Action index query
        return input('Enter the record number to action, or -1 to cancel the action:')

    @staticmethod
    def add_edit():                                                      # Data entry method to add or edit
        title: str = input('Enter note title: ')
        note: str = input('Note Description: ')
        return title, note

    @staticmethod
    def show_records(data):                                              # Display a list of notes in a table
        def print_head(): 
            print(
                f'{"-" * 2}ID{"-" * 3}+{"-" * 12}Title{"-" * 13}+'
                f'{"-" * 30}Note{"-" * 25}+{"-" * 8}Time{"-" * 8}')

        def print_footer():  
            print(f'{"-" * 7}+{"-" * 30}+{"-" * 59}+{"-" * 21}')

        def print_row(row):                                             # One row of a table with data
            print(f'{list_data[row]["id"]:7}|{list_data[row]["title"]:30}|'
                  f'{list_data[row]["note"]:59}|{list_data[row]["datetime"]:11}')

        list_data = data.get_data()                                     
        print('Enter the date for which you want to display the list of notes in the format dd.mm.yyyy,')
        inp = input('or press <Enter> to display full list:')           # Request data for filter by date

        if len(inp) > 0:                                                # Filter set
            try:
                valid_date = time.strptime(inp, '%d.%m.%Y')             # Checking the filter - (the date must be correct)
                print_head()
                for i in range(data.get_length()):
                    if time.strftime('%d.%m.%Y', valid_date) == list_data[i]['datetime'][:10]:  # Data filtering
                        print_row(i)
                print_footer()
            except ValueError:
                print('Date entered incorrectly.')
        else:                                                           # Print full database, without filtering
            print_head()
            for i in range(data.get_length()):
                print_row(i)
            print_footer()

    @staticmethod
    def info():                                                         # Info about the application
        print('Intermediate certification')                             
        print('Notes app (Python)')
        print('Maxim Sukhochev')


    @staticmethod
    def buy():                                                         
        print('See you later')