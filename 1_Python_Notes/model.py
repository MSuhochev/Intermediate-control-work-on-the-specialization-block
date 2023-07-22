import time
import io_module
import settings


class Data:
    new_var = []
    _data = new_var                                               # Data storage list

    def __init__(self):
        self._data = []

    def add(self, title, note):                                   # Adding data by fields
        self._data.append({'id': self.get_max_id() + 1,
                           'title': title,
                           'note': note,
                           'datetime': time.strftime('%d.%m.%Y %H:%M:%S', time.gmtime(time.time()))
                           })

    def edit(self, idx, title, note):                             # Data editing by index
        pointer = -1
        for i in range(self.get_length()):  
            if idx == int(self._data[i]['id']):
                pointer = i
                break
        if pointer == -1:  
            return -1
        else:  
            if len(title) > 0:
                self._data[pointer]['title'] = title
            if len(note) > 0:
                self._data[pointer]['note'] = note
            self._data[pointer]['datetime'] = time.strftime('%d.%m.%Y %H:%M:%S', time.gmtime(time.time()))
            return 0

    def delete(self, idx):                                        # Deleting a note by index
        pointer = -1
        for i in range(self.get_length()):  
            if idx == int(self._data[i]['id']):
                pointer = i
                break
        if pointer == -1:  
            return -1
        else:
            del self._data[pointer]  
            return 0

    def save_db(self):                                            
        if self._data is not None:
            io_module.save_json(self._data, settings.db_file)

    def load_db(self):                                            
        self._data.clear()                                        
        self._data = io_module.load_json(settings.db_file)

    def get_length(self):                                         
        return len(self._data) if self._data is not None else 0

    def get_max_id(self):                                         
        return max([i['id'] for i in self._data]) if self.get_length() > 0 else 0

    def get_data(self):                                           
        return self._data[:] if self._data is not None else []