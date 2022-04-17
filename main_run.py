import sqlite3
from tkinter import *
from datetime import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import filedialog


def exit_app():
    quit()




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
    l_edi.config (text='photo')
    l_edi.config (image='')
    #try:
     #   l.config(text='photo')
    #
    #
      #  l.config(image='')
    #except:
    #    l_edi.config (text='photo')
    #    l_edi.config (image='')

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

lj=[]
lo=[]
lk=[]
lu=[]

def pre_st():
    global ent,an
    an=Toplevel()
    edi_lab=Label(an,text='Enter the id of book you want to edit:')
    edi_lab.pack()
    ent=Entry(an,)
    ent.pack()
    bu=Button(an,text='find',command=start_edit)
    bu.pack()

    an.mainloop()

def start_edit():

    global ent,title,author,datee,locatn,page,gnre,lang,pblr,ispn,tope,er,an,l_edi
    an.quit ()
    tope=Toplevel()
    tope.minsize (600, 500)
    tope.maxsize (600, 500)

    tope.title ('Edit Book')
    book_title = Label (tope, text='Book Titile', font=('arial', 12, 'bold'))
    book_title.place (relx=0.01, rely=0.02)
    editing = Label (tope, text='Editing book id: '+str(ent.get()), font=('arial', 12, 'bold'))
    editing.place (relx=0.61, rely=0.02)
    author = Label (tope, text='Author', font=('arial', 12, 'bold'))
    author.place (relx=0.01, rely=0.13)
    pdate = Label (tope, text='Publication Date(YYYY-MM-DD)', font=('arial', 12, 'bold'))
    pdate.place (relx=0.01, rely=0.24)
    location = Label (tope, text='Location', font=('arial', 12, 'bold'))
    location.place (relx=0.01, rely=0.35)
    num_page = Label (tope, text='Number of Pages', font=('arial', 12, 'bold'))
    num_page.place (relx=0.01, rely=0.46)
    genre = Label (tope, text='Genre', font=('arial', 12, 'bold'))
    genre.place (relx=0.01, rely=0.57)
    laan = Label (tope, text='Language', font=('arial', 12, 'bold'))
    laan.place (relx=0.01, rely=0.68)
    pub = Label (tope, text='Publisher', font=('arial', 12, 'bold'))
    pub.place (relx=0.01, rely=0.79)
    ispn = Label (tope, text='ISPN', font=('arial', 12, 'bold'))
    ispn.place (relx=0.01, rely=0.9)

    title = Entry (tope, relief='ridge', bd=5, font=('arial', 10))
    title.place (relx=0.02, rely=0.06, width=250, height=28)
    author = Entry (tope, relief='ridge', bd=5, font=('arial', 10))
    author.place (relx=0.02, rely=0.17, width=250, height=28)
    datee = Entry (tope, relief='ridge', bd=5, font=('arial', 10))
    datee.place (relx=0.02, rely=0.28, width=250, height=28)
    locatn = Entry (tope, relief='ridge', bd=5, font=('arial', 10))
    locatn.place (relx=0.02, rely=0.39, width=250, height=28)
    page = Entry (tope, relief='ridge', bd=5, font=('arial', 10))
    page.place (relx=0.02, rely=0.50, width=250, height=28)
    gnre = Entry (tope, relief='ridge', bd=5, font=('arial', 10))
    gnre.place (relx=0.02, rely=0.61, width=250, height=28)
    lang = Entry (tope, relief='ridge', bd=5, font=('arial', 10))
    lang.place (relx=0.02, rely=0.72, width=250, height=28)
    pblr = Entry (tope, relief='ridge', bd=5, font=('arial', 10))
    pblr.place (relx=0.02, rely=0.83, width=250, height=28)
    ispn = Entry (tope, relief='ridge', bd=5, font=('arial', 10))
    ispn.place (relx=0.02, rely=0.94, width=250, height=28)

    cho = Button (tope, text='Choose file', font=('arial', 12, 'bold'), command=ask_directory_edit)
    cho.place (relx=0.6, rely=0.7)

    saveb = Button (tope, text='Edit&Save', bd=3, font=('arial', 12, 'bold'), command=edit_data)
    saveb.place (relx=0.55, rely=0.85)
    cancel = Button (tope, text='Clear', bd=3, font=('arial', 12, 'bold',), command=cls)
    cancel.place (relx=0.75, rely=0.85)

    l_edi = Label (tope, image='', text='photo', compound='top', wraplength=80)
    l_edi.place (relx=0.5, rely=0.15, relwidth=0.4, relheight=0.55)

    er = Label (tope, text='-', bd=3, font=('arial', 12, 'bold'))
    er.place (relx=0.6, rely=0.95)
    tope.mainloop()

def ask_directory_edit():
    global lk
    lj.clear()
    lo.clear()
    lj.append(filedialog.askopenfilename())
    g_edi()


def edit_data():
    global ls,er
    sql = "UPDATE books SET book_title='{}',book_author='{}',Publication_date='{}',location='{}',number_of_pages='{}',genre='{}',publisher='{}',ispn='{}',language='{}',photodir='{}' WHERE book_id={}"
    book_title=title.get()
    book_author=author.get()
    publication_date=inser_pubdate()
    location=locatn.get()
    number_of_pages=page.get()
    genre=gnre.get()
    language=lang.get()
    publisher=pblr.get()
    isp=ispn.get()
    pdi=lj[0]
    sql=sql.format(book_title,book_author,publication_date,location,number_of_pages,genre,publisher,isp,language,pdi,int(ent.get()))
    try:
        c.execute (sql)
        conn.commit ()
        er.config(text='-')
        #lo.clear ()
        #lj.clear()
        #cls ()
        ss = "SELECT * FROM books ORDER BY book_id DESC LIMIT 1"
        for f in c.execute (ss):
            img1 = ImageTk.PhotoImage (Image.open (pdi).resize ((120, 150), Image.ANTIALIAS))
            li[int(ent.get())] = img1
    except:
        er.config(text='Error occured! Try Again')

def g_edi():
    global lj,l

    for i in lj:
        img1 = ImageTk.PhotoImage (Image.open (i).resize ((120, 150), Image.ANTIALIAS))
        lo.append (img1)
    l_edi.config(image=lo[0])
    l_edi.config(text=lj[0])




root=Tk()
root.title('books')



menu_bar=Menu(root)
root.config(menu=menu_bar)

file_menu=Menu(menu_bar,tearoff=0)
file_menu.add_command(label="Add Book",command=start)
file_menu.add_command(labe="Edit Book",command=pre_st)
file_menu.add_command(labe="Info")
file_menu.add_separator()
file_menu.add_command(label="Exit Application",command=exit_app)
menu_bar.add_cascade(label='Database',menu=file_menu)

tab_control=ttk.Notebook(root)
booksTab=ttk.Frame(tab_control)
tab_control.add(booksTab,text='Books')
tab_control.pack(fill='both',expand='yes')
can=Canvas(booksTab,bg='grey')
can.pack(fill='both',expand='yes')




ref=Button(root,text='Refresh',bd=5,command=refresh)
can.create_window(970,20,window=ref)
search_entry=Entry(can)
search_btn=Button(can,text='Search',bd=5)
searchby=Menubutton(can,text='Search By ')
can.create_window(1300,20,window=searchby)
searchby.menu=Menu(searchby,tearoff=0)
searchby["menu"]=searchby.menu
id=IntVar()
title=IntVar()
author=IntVar()
ispn=IntVar()

searchby.menu.add_checkbutton(label='id',variable=id)
searchby.menu.add_checkbutton(label='title',variable=title)
searchby.menu.add_checkbutton(label='author',variable=author)
searchby.menu.add_checkbutton(label='ispn',variable=ispn)
can.create_window(1100,20,window=search_entry,width=200)
can.create_window(1230,22,window=search_btn,height=20)



sc_bar=Scrollbar(can,orient=VERTICAL,command=can.yview)
sc_bar.place(relx=1,rely=0,relheight=1,anchor=NE)


sql = "SELECT * FROM BOOKS"
fls = c.execute (sql)
ls=dict()
li={}
def sra():
    for i in fls:
        ls[i[0]]=i[11]
    for i in ls:
        img1=ImageTk.PhotoImage(Image.open(ls[i]).resize((120,150),Image.ANTIALIAS))
        li[i]=img1
sra()
def pt(id):
    print(id)
def lab(xcon,ycon,id,title,author,publisher,location,ispn):

    can.create_window (xcon, ycon,
                       window=Button (can, image=li[id], width=240, height=120, wraplength=230, activebackground='red',
                                      fg='green', justify='left',command=lambda:pt(id),
                                      text='ID: {} \nTITLE: {} \nAUTHOR: {}\nPUBLISHER: {} \nLOCATION: {} \nISPN: {}  '.format(id,title,author,publisher,location,ispn),
                                      compound='left'))

root.mainloop()