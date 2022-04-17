import sqlite3
from datetime import*

conn=sqlite3.connect('library.db')

c=conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS books('
          'book_id INTEGER PRIMARY KEY AUTOINCREMENT,'
          'book_title VARCHAR NOT NULL,'
          'book_author VARCHAR NOT NULL,'
          'Publication_date DATE DEFAULT "-",'
          'date_added TIMESTAMP ,'
          'location VARCHAR DEFAULT "-",'
          'number_of_pages INT DEFAULT 0,'
          'genre VARCHAR DEFAULT "-",'
          'publisher VARCHAR DEFAULT "-",'
          'ispn INT DEFAULT "-",'
          'language VARCHAR DEFAULT "-",'
          'price DECIMAL DEFAULT "-",'
          'photodir VARCHAR)')

#c.execute('CREATE TABLE IF NOT EXISTS tags(tags VARCHAR,book_id INTEGER)')


def inser_pubdate():
    try:
        publication_date = [int (i) for i in input ('pub date: ').split ()]
        publication_date = date (publication_date[0], publication_date[1], publication_date[2])
        return publication_date
    except:
        return inser_pubdate()
def insert_data():
    book_title=input('title: ')
    book_author=input('author: ')
    publication_date=inser_pubdate()
    date_added=datetime.now()
    location=input('location: ')
    number_of_pages=int(input('pages: '))
    genre=input('genre: ')
    publisher=input('publisher: ')
    ispn=int(input('ispn: '))
    language=input('language: ')
    price=float(input('price: '))
    photodir=input('photo dir: ')

    c.execute('INSERT INTO books(book_title,book_author,Publication_date,date_added,location,number_of_pages,genre,publisher,ispn,language,price,photodir) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)',(book_title,book_author,publication_date,date_added,location,number_of_pages,genre,publisher,ispn,language,price,photodir))
    conn.commit()
def add_to_database():
    ans=input('a to add book q to quit')
    if ans=='a':
        insert_data()
def edit_book_data(idw):
    sql="UPDATE books SET book_title='{}',book_author='{}',Publication_date='{}',location='{}',number_of_pages='{}',genre='{}',publisher='{}',ispn='{}',language='{}',photodir='{}' WHERE book_id={}"
    book_title = input ('title: ')
    book_author = input ('author: ')
    publication_date = inser_pubdate ()
    date_added = datetime.now ()
    location = input ('location: ')
    number_of_pages = int (input ('pages: '))
    genre = input ('genre: ')
    publisher = input ('publisher: ')
    ispn = int (input ('ispn: '))
    language = input ('language: ')
    photodir = input ('photo dir: ')
    sql=sql.format(book_title,book_author,publication_date,location,number_of_pages,genre,publisher,ispn,language,photodir,idw)
    c.execute(sql)
    conn.commit()
#edit_book_data(2)

def read_data():
    sql="SELECT * FROM BOOKS"
    for i in c.execute(sql):
        print(i)
read_data()






