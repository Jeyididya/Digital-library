import sqlite3
from datetime import *
conn=sqlite3.connect('library.db')

c=conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS books('
          'book_id INTEGER PRIMARY KEY AUTOINCREMENT,'
          'book_title VARCHAR NOT NULL,'
          'book_author VARCHAR NOT NULL,'
          'genre VARCHAR DEFAULT "-",'
          'language VARCHAR DEFAULT "-",'
          'release_date DATE DEFAULT "-",'
          'number_of_pages INT DEFAULT 0,'
          'publisher VARCHAR DEFAULT "-",'
          'series VARCHAR DEFAULT "-",'
          'series_id VARCHAR DEFAULT "-",'
          'location VARCHAR DEFAULT "-",'
          'isbn INT DEFAULT "-",'
          'book_description VARCHAR DEFAULT "-",'
          'photo_dir VARCHAR,'
          'date_added TIMESTAMP)')

from tkinter import *
from tkinter import ttk
root=Tk()






root.mainloop()