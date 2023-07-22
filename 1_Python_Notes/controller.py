""" Controller - contains the main loop of the program
and combines the view and the data model """

from view import View
from model import Data
from log import logger


class Controller:
    def __init__(self):                                                    # class constructor
        self._view = View()  
        self._data = Data() 

    def add(self):                                                         # Adding note
        self._view.print('Adding an entry')
        title, note = self._view.add_edit()                                
        self._data.add(title, note)
        self._view.print('Entry added')
        logger(f'Adding an entry: Title = {title}; Note = {note} ', '<')

    def edit(self):                                                        # Edit note
        idx = int(self._view.note_id())                                    
        if idx > -1:
            self._view.print('Editing a post')
            self._view.print('If you do not need to change the data, leave it blank')
            title, note = self._view.add_edit()                            
            if self._data.edit(idx, title, note) != -1:  
                self._view.print(f'The note {idx} changed title => {title}, note => {note}')
                logger(f'The note {idx} changed! title => {title}, note => {note}', '>')
            else:
                self._view.print('There is no post with this index!')
                logger(f'Post editing error {str(idx)}. Note does not exist!', '>')

    def delete(self):                                                      # Deleting a note
        idx = int(self._view.note_id())                           
        if idx > -1:
            if self._data.delete(idx) != -1:  
                self._view.print(f'The note {idx} deleted!')
                logger(f'The note {idx} deleted!', '<')
            else:
                self._view.print('There is no post with this index!')
                logger(f'Note deletion error {str(idx)}. Note does not exist!', '>')

    def list(self):                                                        # Output of records for printing
        self._view.show_records(self._data)
        logger(f'Output {self._data.get_length()} rows', '>')

    def load(self):                                                        # Loading records from a file
        self._data.load_db()
        self._view.print('Records loaded from file.')
        logger('Records loaded from file.', '>')

    def save(self):                                                        # Saving records to a file
        self._data.save_db()
        self._view.print('The data is written to the file.')
        logger('The data is written to the file.', '>')

    def run(self):                                                         # Switch case commands
        self.load()
        while True:
            self._view.menu()
            inp = input('Enter command number -> ')
            logger(inp, '>') 
            match inp.lower():
                case '1':
                    self.add()
                case '2':
                    self.edit()
                case '3':
                    self.delete()
                case '4':
                    self.list()
                case '5':
                    self.save()
                case '6':
                    self.load()
                case '7':
                    self._view.info()
                case '8':
                    break
                case _:
                    self._view.print('The team does not exist. Dial for help - help')
        self.save()  
        logger('Completion of work.', '>')
        self._view.buy()                                                  