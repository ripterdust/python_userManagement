from tkinter import Tk, ttk
from tkinter import *
from DB import Db
from functions import * 

# Tkinter config
root = Tk()
root.title('Users managment')
root.resizable(True, False)

# Database config
database = Db()

# Main frame config
mainFrame = Frame(root)
mainFrame.pack(padx=20, pady= 20)

# Title
Label(mainFrame, text = 'Users managment', pady=10).pack()

# --------- Treeview ------------
# Scrollbar settings
scrollbar = Scrollbar(mainFrame, orient='vertical')
scrollbar.pack(side='right', fill=Y)

# Treeview config
tv = ttk.Treeview(
    mainFrame, 
    columns=(1,2,3,4,5,6), 
    show='headings',
    selectmode='browse'
)
tv.pack(fill='both')

tv.configure(yscrollcommand=scrollbar.set)

# scrollbarr configuration
scrollbar.configure(command=tv.yview)
# setting headints
tv.heading(1, text = 'Id')
tv.column(1, anchor='center', width=50)

tv.heading(2, text = 'Name')
tv.column(2, anchor='center')

tv.heading(3, text = 'Last name')
tv.column(3, anchor='center')

tv.heading(4, text = 'Gender')
tv.column(4, anchor='center')

tv.heading(5, text='Country' )
tv.column(5, anchor='center')

tv.heading(6, text= 'Age' )
tv.column(6, anchor='center', width=40)
# Getting tkinter data
database.fetch_data(tv)

# Buttons of actions
buttons_frame = Frame(mainFrame, pady= 7)
buttons_frame.pack(anchor=CENTER)
# Delete button
Button(buttons_frame, 
text = 'Delete user', 
padx=10,
command= lambda:database.delete_data(tv)
).pack(side=LEFT)

# Add button
Button(buttons_frame,
text = 'Add new user',
padx= 20,
command = lambda:add_new_user(root, database, tv)
).pack(side=LEFT)

# Mainloop
root.mainloop()
