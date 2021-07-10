import mysql.connector
from tkinter import messagebox


class Db:
    # Constructor
    def __init__(self):
        self._db = mysql.connector.connect(
            user = 'root',
            password = 'marlyn2010',
            database = 'travels',
            host = 'localhost'
        )
        self._cursor = self._db.cursor()
        self._table_name = 'usersdata'
        self._error = 'An error has ocurred'

    def fetch_data(self, tv):
        self._query = f'SELECT * FROM {self._table_name};'
        self._cursor.execute(self._query)
        rows = self._cursor.fetchall()
        for i in rows:
            tv.insert('', 'end', values = i)

        

    def delete_data(self, tv = False):

        if tv:
            current_item = tv.focus()
            item_data = tv.item(current_item)

            if item_data['values'] != '':
                try:
                    id = item_data['values'][0] 
                    self._query = f'DELETE FROM {self._table_name} WHERE user_uid = {id};'
                    self._cursor.execute(self._query)
                    self._db.commit()
                    tv.delete(*tv.get_children()) 
                    self.fetch_data(tv)
                except:
                    messagebox.showerror(title='Error', messagebox=self._error)
            else:
                messagebox.showwarning(title='Error', message='Please select an user.')
            
        else:
            messagebox.showerror(title = 'Error', message=self.__error)

    # add new user
    def add_data(self, data, tv = False,):
        self._query = f'''INSERT INTO {self._table_name}
        (first_name, last_name, gender, country, age)
        values {data};'''
        
        if tv:
            self._cursor.execute(self._query)
            self._db.commit()
            self.fetch_data(tv)
        else:
            messagebox.showerror(title = 'Error', message='Cannot add new user')