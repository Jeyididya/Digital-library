import sqlite3
from tkinter import *
from datetime import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import filedialog

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
          'photodir VARCHAR)')


def refresh():
    cox = [140, 490, 850, 1200]

    sql_ = "SELECT * FROM BOOKS"
    fls_ = c.execute (sql_)

    nu = 0
    coy = 100
    #sra()
    for i in fls_:
        if nu < 3:
            lab (cox[nu], coy, i[0], i[1], i[2], i[8], i[5], i[9])
            nu += 1
        elif nu == 3:
            lab (cox[nu], coy, i[0], i[1], i[2], i[8], i[5], i[9])
            nu = 0
            coy += 180

    can.config (yscrollcommand=sc_bar.set, scrollregion=(0, 0, 0, coy))

def start():
    global title,author,datee,locatn,page,gnre,lang,pblr,ispn,topl,er,l
    topl = Toplevel ()
    topl.minsize (600, 500)
    topl.maxsize (600, 500)

    topl.title ('Add Book')
    book_title = Label (topl, text='Book Titile', font=('arial', 12, 'bold'))
    book_title.place (relx=0.01, rely=0.02)
    author = Label (topl, text='Author', font=('arial', 12, 'bold'))
    author.place (relx=0.01, rely=0.13)
    pdate = Label (topl, text='Publication Date(YYYY-MM-DD)', font=('arial', 12, 'bold'))
    pdate.place (relx=0.01, rely=0.24)
    location = Label (topl, text='Location', font=('arial', 12, 'bold'))
    location.place (relx=0.01, rely=0.35)
    num_page = Label (topl, text='Number of Pages', font=('arial', 12, 'bold'))
    num_page.place (relx=0.01, rely=0.46)
    genre = Label (topl, text='Genre', font=('arial', 12, 'bold'))
    genre.place (relx=0.01, rely=0.57)
    laan = Label (topl, text='Language', font=('arial', 12, 'bold'))
    laan.place (relx=0.01, rely=0.68)
    pub = Label (topl, text='Publisher', font=('arial', 12, 'bold'))
    pub.place (relx=0.01, rely=0.79)
    ispn = Label (topl, text='ISPN', font=('arial', 12, 'bold'))
    ispn.place (relx=0.01, rely=0.9)

    title = Entry (topl, relief='ridge', bd=5, font=('arial', 10))
    title.place (relx=0.02, rely=0.06, width=250, height=28)
    author = Entry (topl, relief='ridge', bd=5, font=('arial', 10))
    author.place (relx=0.02, rely=0.17, width=250, height=28)
    datee = Entry (topl, relief='ridge', bd=5, font=('arial', 10))
    datee.place (relx=0.02, rely=0.28, width=250, height=28)
    locatn = Entry (topl, relief='ridge', bd=5, font=('arial', 10))
    locatn.place (relx=0.02, rely=0.39, width=250, height=28)
    page = Entry (topl, relief='ridge', bd=5, font=('arial', 10))
    page.place (relx=0.02, rely=0.50, width=250, height=28)
    gnre = Entry (topl, relief='ridge', bd=5, font=('arial', 10))
    gnre.place (relx=0.02, rely=0.61, width=250, height=28)
    lang = Entry (topl, relief='ridge', bd=5, font=('arial', 10))
    lang.place (relx=0.02, rely=0.72, width=250, height=28)
    pblr = Entry (topl, relief='ridge', bd=5, font=('arial', 10))
    pblr.place (relx=0.02, rely=0.83, width=250, height=28)
    ispn = Entry (topl, relief='ridge', bd=5, font=('arial', 10))
    ispn.place (relx=0.02, rely=0.94, width=250, height=28)

    cho = Button (topl, text='Choose file', font=('arial', 12, 'bold'), command=ask_directory)
    cho.place (relx=0.6, rely=0.7)

    saveb = Button (topl, text='Save', bd=3, font=('arial', 12, 'bold'), command=insert_data)
    saveb.place (relx=0.6, rely=0.85)
    cancel = Button (topl, text='Cancel', bd=3, font=('arial', 12, 'bold',),command=cls)
    cancel.place (relx=0.75, rely=0.85)

    l = Label (topl, image='', text='photo', compound='top', wraplength=80)
    l.place (relx=0.5, rely=0.15, relwidth=0.4, relheight=0.55)

    er = Label (topl, text='-', bd=3, font=('arial', 12, 'bold'))
    er.place (relx=0.6, rely=0.95)
    topl.mainloop ()

def ask_directory():
    global lk
    lk.clear()
    lu.clear()
    lk.append(filedialog.askopenfilename())
    g()

def insert_data():
    global ls,er,sql,fls
    book_title = title.get ()
    book_author = author.get ()
    date_added = datetime.now ()
    publication_date = inser_pubdate ()
    location = locatn.get ()
    number_of_pages = page.get ()
    genre = gnre.get ()
    language = lang.get ()
    publisher = pblr.get ()
    isp = ispn.get ()
    try:
        pdi = lk[0]
    except:
        pdi='C:/Users/jedidiah/PycharmProjects/library/main/nop.png'

    try:
        c.execute ("INSERT INTO books(book_title,book_author,date_added,Publication_date,location,number_of_pages,genre,publisher,language,ispn,photodir) VALUES(?,?,?,?,?,?,?,?,?,?,?)",
                   (book_title,book_author,date_added,publication_date,location,int(number_of_pages),genre,publisher,language,isp,pdi))
        conn.commit ()
        er.config(text='-')
        lk.clear ()

        ss = "SELECT * FROM books ORDER BY book_id DESC LIMIT 1"
        for f in c.execute (ss):
            print (f[0])
            img1 = ImageTk.PhotoImage (Image.open (pdi).resize ((120, 150), Image.ANTIALIAS))
            li[f[0]] = img1


    except:
        er.config(text='Error occured! Try Again')
        print('error')
    cls ()

def cls():
    title.delete(0,END)
    author.delete(0,END)
    datee.delete(0,END)
    locatn.delete(0,END)
    page.delete(0,END)
    gnre.delete(0,END)
    lang.delete(0,END)
    pblr.delete(0,END)
    ispn.delete(0,END)
    l.config(text='photo')
    l.config(image='')

def g():
    global lk,l

    for i in lk:
        img1 = ImageTk.PhotoImage (Image.open (i).resize ((120, 150), Image.ANTIALIAS))
        lu.append (img1)
    l.config(image=lu[0])
    l.config(text=lk[0])
def inser_pubdate():
    global datee
    try:
        da=datee.get().split()
        publication_date = date (int(da[0]), int(da[1]), int(da[2]))
        return publication_date
    except:
        datee.delete(0,END)
        er.config(text='publication date incorrect!!!')
        return int('a')