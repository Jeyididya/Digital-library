
lj=[]
lo=[]

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
    pdi=lo[0]
    sql=sql.format(book_title,book_author,publication_date,location,number_of_pages,genre,publisher,isp,language,pdi,int(ent.get()))
    try:
        c.execute (sql)
        conn.commit ()
        er.config(text='-')
        lk.clear ()
        cls ()
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
    l_edi.config(image=lu[0])
    l_edi.config(text=lk[0])
