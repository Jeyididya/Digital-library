from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk
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
          'photodir VARCHAR)')


topl=Tk()
topl.minsize (600, 500)
topl.maxsize (600, 500)

topl.title('Add Book')



book_title=Label(topl,text='Book Titile',font=('arial',12,'bold'))
book_title.place(relx=0.01,rely=0.02)
author=Label(topl,text='Author',font=('arial',12,'bold'))
author.place(relx=0.01,rely=0.13)
pdate=Label(topl,text='Publication Date(YYYY-MM-DD)',font=('arial',12,'bold'))
pdate.place(relx=0.01,rely=0.24)
location=Label(topl,text='Location',font=('arial',12,'bold'))
location.place(relx=0.01,rely=0.35)
num_page=Label(topl,text='Number of Pages',font=('arial',12,'bold'))
num_page.place(relx=0.01,rely=0.46)
genre=Label(topl,text='Genre',font=('arial',12,'bold'))
genre.place(relx=0.01,rely=0.57)
laan=Label(topl,text='Language',font=('arial',12,'bold'))
laan.place(relx=0.01,rely=0.68)
pub=Label(topl,text='Publisher',font=('arial',12,'bold'))
pub.place(relx=0.01,rely=0.79)
ispn=Label(topl,text='ISPN',font=('arial',12,'bold'))
ispn.place(relx=0.01,rely=0.9)




def ask_directory():
    global ls
    ls.clear()
    #print(filedialog.askopenfilename())
    ls.append(filedialog.askopenfilename())
    g()


ls = ['C:/Users/jedidiah/PycharmProjects/library/main/lk.gif']
li = []

def g():
    global ls,li

    for i in ls:
        img1 = ImageTk.PhotoImage (Image.open (i).resize ((120, 150), Image.ANTIALIAS))
        li.append (img1)
    l=Label(topl,image=li[0],text=ls[0],compound='top',wraplength=80)
    l.place (relx=0.5, rely=0.15, relwidth=0.4, relheight=0.55)
def inser_pubdate():
    try:
        da=datee.get().split()
        publication_date = date (int(da[0]), int(da[1]), int(da[2]))
        return publication_date
    except:
        pass

def insert_data():
    global ls
    book_title=title.get()
    book_author=author.get()
    date_added = datetime.now ()
    publication_date=inser_pubdate()
    location=locatn.get()
    number_of_pages=page.get()
    genre=gnre.get()
    language=lang.get()
    publisher=pblr.get()
    isp=ispn.get()
    pdi=ls[0]
    try:
        c.execute ("INSERT INTO books(book_title,book_author,date_added,Publication_date,location,number_of_pages,genre,publisher,language,ispn,photodir) VALUES(?,?,?,?,?,?,?,?,?,?,?)",
                   (book_title,book_author,date_added,publication_date,location,int(number_of_pages),genre,publisher,language,isp,pdi))
        conn.commit ()
        er.config(text='-')
        ls.clear ()
    except:
        er.config(text='Error occured! Try Again')
        print('error')



title=Entry(topl,relief='ridge',bd=5,font=('arial',10))
title.place(relx=0.02,rely=0.06,width=250,height=28)
author=Entry(topl,relief='ridge',bd=5,font=('arial',10))
author.place(relx=0.02,rely=0.17,width=250,height=28)
datee=Entry(topl,relief='ridge',bd=5,font=('arial',10))
datee.place(relx=0.02,rely=0.28,width=250,height=28)
locatn=Entry(topl,relief='ridge',bd=5,font=('arial',10))
locatn.place(relx=0.02,rely=0.39,width=250,height=28)
page=Entry(topl,relief='ridge',bd=5,font=('arial',10))
page.place(relx=0.02,rely=0.50,width=250,height=28)
gnre=Entry(topl,relief='ridge',bd=5,font=('arial',10))
gnre.place(relx=0.02,rely=0.61,width=250,height=28)
lang=Entry(topl,relief='ridge',bd=5,font=('arial',10))
lang.place(relx=0.02,rely=0.72,width=250,height=28)
pblr=Entry(topl,relief='ridge',bd=5,font=('arial',10))
pblr.place(relx=0.02,rely=0.83,width=250,height=28)
ispn=Entry(topl,relief='ridge',bd=5,font=('arial',10))
ispn.place(relx=0.02,rely=0.94,width=250,height=28)



cho=Button(topl,text='Choose file',font=('arial',12,'bold'),command=ask_directory)
cho.place(relx=0.6,rely=0.7)


saveb=Button(topl,text='Save',bd=3,font=('arial',12,'bold'),command=insert_data)
saveb.place(relx=0.6,rely=0.85)
cancel=Button(topl,text='Cancel',bd=3,font=('arial',12,'bold'))
cancel.place(relx=0.75,rely=0.85)

er=Label(topl,text='-',bd=3,font=('arial',12,'bold'))
er.place(relx=0.6,rely=0.95)





topl.mainloop()