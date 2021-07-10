from logging import warn
from tkinter import Button, Entry, Frame, Label, OptionMenu, StringVar, messagebox, Toplevel
from tkinter.constants import LEFT
from newUser import User

error = 'An error has ocurred'

def destroy(window):
    window.destroy()

def warning(message_text):
    messagebox.showwarning(title='Error', message = message_text)


def add_new_user(win = False, database = False, tv = False):
    if win and database and tv:
        new = Toplevel(win, padx=10, pady=10)
        new.title('Add new user')
        Label(new, text = 'Add new user.').pack()

        # Data
        data_frame = Frame(new,
            pady=10,
            padx=10
        )
        data_frame.pack()    

        # Name
        name_frame = Frame(data_frame,
        pady= 10,
        padx= 10
        )
        name_frame.pack()
        Label(name_frame, text= 'First name: ').pack(side=LEFT)
        first_name = Entry(name_frame)
        first_name.pack(side = LEFT)

        # Last name
        last_name_frame = Frame(data_frame, padx=10, pady=10)
        last_name_frame.pack()
        Label(last_name_frame, text = 'Last name: ').pack(side=LEFT)
        last_name = Entry(last_name_frame)
        last_name.pack(side = LEFT)

        # Gender
        gender_frame = Frame(data_frame, pady=10, padx=10)
        gender_frame.pack()
        Label(gender_frame, text= 'Gender: ').pack(side=LEFT)
        # Variable
        variable = StringVar(new)
        # Default value
        genders = ('Male', 'Female')
        variable.set(genders[0]) 

        # dropdown
        dropdown = OptionMenu(gender_frame, variable, *genders)
        dropdown.pack() 

        # Country
        country_frame = Frame(data_frame,
        padx=10,
        pady=10
        )
        country_frame.pack()
        Label(country_frame, text = 'Country: ').pack(side=LEFT)
        country = Entry(country_frame)
        country.pack(side=LEFT)

        # Age
        age_frame = Frame(data_frame,
            pady=10,
            padx=10
        )
        age_frame.pack()
        Label(age_frame, text = 'Age: ').pack(side=LEFT)
        age = Entry(age_frame)
        age.pack(side=LEFT)
        
        # Action buttons
        button_frame = Frame(new)
        button_frame.pack()

        # Add user function
        
        def add():
            try:

                user = User(
                    first_name.get(),
                    last_name.get(),
                    variable.get(),
                    country.get(),
                    int(age.get())
                )

                x = 'Unknow'
                if user.first_name == x :
                    warning('Insert a valid first name')
                elif user.last_name == x:
                    warning('Insert a valid last name')
                elif len(user.first_name) > 10:
                    warning('Fist name too long.')
                elif len(user.last_name) > 10:
                    warning('Last name is too long. ')
                else:
                    database.add_data(user.get_data(), tv)
                    new.destroy()
            except ValueError:
                messagebox.showerror(title= 'error', message = 'Insert a valid number')


        # Buttons
        Button(button_frame, text = 'Add', command = add).pack()
        Button(button_frame, text='Cancel', command = lambda:destroy(new)).pack()
        
    else:
        messagebox.showerror(title='error', message = error)
