import os
import shutil
import sqlite3

from tkinter import *
from datetime import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import filedialog
from tkinter import messagebox

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
c.execute('CREATE TABLE IF NOT EXISTS tags('
          'tags VARCHAR,'
          'book_id INTEGER)')

def add_to_database(book_name,author_name,genre,language,release_date,number_of_pages,publisher,series,series_id,location,isbn,description,photo_dir):
    date_added=datetime.now()
    c.execute('INSERT INTO books (book_title,book_author,genre,language,release_date,number_of_pages,'
              'publisher,series,series_id,location,isbn,book_description,photo_dir,date_added) '
              'VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
              (book_name,author_name,genre,language,release_date,number_of_pages,publisher,series,series_id,location,isbn,description,photo_dir,date_added))
    conn.commit()
def add_genre():
    open('genre.txt','a').write('\n'+genre_add_entry.get ())
    print(genre_add_entry.get ())
    option_menu = genre_opt.children['menu']
    option_menu.add_command (label=genre_add_entry.get (), command=lambda v=genre_var, l=genre_add_entry.get (): v.set (l))

def insert_tags2entry():
    book_tags_entry.insert('end','\n'+tags_var.get()+'\n')

def photo_choosing():
    photo_dir.clear()
    img_file.clear()
    file_path=filedialog.askopenfilename()
    if len(file_path)!=0:
        photo_dir.append (file_path)
    else:
        photo_dir.append('cover-page/nop.png')
    for i in photo_dir:
        img1 = ImageTk.PhotoImage (Image.open (i).resize ((90, 100), Image.ANTIALIAS))
        img_file.append (img1)
    book_image.config (image=img_file[0], text='')

def adding():

    try:
        picture=photo_dir[0]
    except:
        if len(photo_dir)==0:
            if messagebox.askyesno ('Warning', "You didn't specify a photo,do you want to continue with a default picture ?"):
                picture='cover-page/nop.png'
                picture_fil.clear()
                for i in picture_dir:
                    no_img=ImageTk.PhotoImage(Image.open(i).resize((90,100),Image.ANTIALIAS))
                    picture_fil.append(no_img)
                book_image.config(image=picture_fil[0],text='')

    if len(book_title_entry.get())==0 or len(book_author_entry.get())==0:
        messagebox.showerror('Error','Book Title or Book Author  are empty')
    else:
        print('title: ',book_title_entry.get())
        print('author: ',book_author_entry.get())
        print('genre: ',genre_var.get())
        print('language: ',language_var.get())
        print('release year: ',book_releaseYear_entry.get())
        print('page no: ',book_pageNo_entry.get())
        print('publisher: ',book_publisher_entry.get())
        print('series: ',series_var.get(),', series num:  ',series_num_entry.get())
        print('location: ',location_var.get())
        print('ispn: ',book_isbn_entry.get())
        print('description: ',book_description_entry.get(0.0,'end'))
        for i in book_tags_entry.get(0.0,'end').split('\n'):
            if i=='':
                pass
            else:
                c.execute('INSERT INTO tags (tags,book_id) VALUES(?,?)',(i,last_id+1))
        if 'cover-page' in picture:
            print ('picture: ', picture)
            add_to_database (book_title_entry.get (), book_author_entry.get (), genre_var.get (), language_var.get (),
                             book_releaseYear_entry.get (), book_pageNo_entry.get (),
                             book_publisher_entry.get (), series_var.get (), series_num_entry.get (),
                             location_var.get (), book_isbn_entry.get (), str(book_description_entry.get (0.0, 'end')),
                             picture)
            add_new_book (get_lastID (), book_title_entry.get (), book_author_entry.get (), book_publisher_entry.get (),
                          location_var.get (), book_isbn_entry.get (), picture)
        else:
            shutil.move(picture,'cover-page')
            os.rename('cover-page/'+picture.split('/')[-1],'cover-page/{}'.format(book_title_entry.get()+'.'+picture.split('/')[-1].split('.')[-1]))
            picture_n= 'cover-page/{}'.format(book_title_entry.get()+'.'+picture.split('/')[-1].split('.')[-1])
            add_to_database (book_title_entry.get (), book_author_entry.get (), genre_var.get (), language_var.get (),
                             book_releaseYear_entry.get (), book_pageNo_entry.get (),
                             book_publisher_entry.get (), series_var.get (), series_num_entry.get (),
                             location_var.get (), book_isbn_entry.get (), str(book_description_entry.get (0.0, 'end')),
                             picture_n)
            add_new_book(get_lastID(),book_title_entry.get(),book_author_entry.get(),book_publisher_entry.get(),location_var.get(),book_isbn_entry.get(),picture_n)

def cleaner():
    book_title_entry.delete(0,'end')
    book_author_entry.delete(0,'end')
    book_releaseYear_entry.delete(0,'end')
    book_pageNo_entry.delete(0,'end')
    book_publisher_entry.delete(0,'end')
    series_num_entry.delete(0,'end')
    book_isbn_entry.delete(0,'end')
    book_description_entry.delete(0.0,'end')
    photo_dir.clear()
    img_file.clear()
    picture_fil.clear()

def main():
    adding()
    cleaner()
    last_id=get_lastID()
    add_window.title ('Adding Book(#ID={})'.format (last_id + 1))

def get_lastID():
    for i in c.execute('SELECT  MAX(book_id) FROM books'):
        return i[0]

def main_start():
    global genre_add_entry,genre_opt,genre_var,book_tags_entry,photo_dir,tags_var
    global img_file,book_image,picture_fil,picture_dir,book_title_entry,book_author_entry
    global language_var,book_releaseYear_entry,book_pageNo_entry,book_publisher_entry,series_var
    global series_num_entry,location_var,book_isbn_entry,book_description_entry,last_id,add_window
    try:
        os.makedir ('cover-page')
    except:
        pass
    add_window = Toplevel()
    '''                            
     ######   ######   #           #       #          ######      
     #        #    #   #                   #          #    #
     ######   ######   #           #     #####        ######
          #        #   #           #       #          # 
     ######        #   ######      #       ######     ######

    '''
    '''
    #            #        #####    #######    #
    #           # #       #    #   #          #
    #          #####      #####    #######    #
    #         #     #     #    #   #          #
    #######  #       #    ######   #######    #######



    '''

    book_title = Label (add_window, text='Book Title', font=('arial', 12, 'bold'))
    book_title.grid (row=0, column=0)
    book_author = Label (add_window, text='Book Author', font=('arial', 12, 'bold'))
    book_author.grid (row=1, column=0, pady=2)
    book_genre = Label (add_window, text='Genre', font=('arial', 12, 'bold'))
    book_genre.grid (row=2, column=0)
    book_language = Label (add_window, text='Language', font=('arial', 12, 'bold'))
    book_language.grid (row=3, column=0)
    book_releaseYear = Label (add_window, text='Release Year', font=('arial', 12, 'bold'))
    book_releaseYear.grid (row=4, column=0)
    book_pageNo = Label (add_window, text='Page Number', font=('arial', 12, 'bold'))
    book_pageNo.grid (row=5, column=0, pady=2)
    book_publisher = Label (add_window, text='Publisher', font=('arial', 12, 'bold'))
    book_publisher.grid (row=6, column=0, pady=2)
    book_series = Label (add_window, text='Series', font=('arial', 12, 'bold'))
    book_series.grid (row=7, column=0)
    book_seriesNum = Label (add_window, text='id', font=('arial', 12, 'bold'))
    book_seriesNum.place (relx=0.51, rely=0.43)

    book_location = Label (add_window, text='Location', font=('arial', 12, 'bold'))
    book_location.grid (row=8, column=0)
    book_isbn = Label (add_window, text='ISBN', font=('arial', 12, 'bold'))
    book_isbn.grid (row=9, column=0)
    book_description = Label (add_window, text='Book Description', font=('arial', 12, 'bold'))
    book_description.grid (row=10, column=0, pady=2)

    book_tags = Label (add_window, text='Book Tags', font=('arial', 12, 'bold'))
    book_tags.grid (row=13, column=0)

    '''
      ######   ##    #   #######    ######     #     #
      #        # #   #      #       #     #     #   #
      ######   #  #  #      #       ######       # #
      #        #   # #      #       #  #          #
      ######   #    ##      #       #   #         #
    '''

    book_title_entry = Entry (add_window, width=30, font=('arial', 12, 'bold'), relief='sunken', bd=2)
    book_title_entry.grid (row=0, column=1)
    book_author_entry = Entry (add_window, width=30, font=('arial', 12, 'bold'), relief='sunken', bd=2)
    book_author_entry.grid (row=1, column=1)
    # genre choosing---
    genre_options = [i.strip () for i in open ('genre.txt', 'r', encoding='utf-8').readlines ()]
    genre_var = StringVar ()
    genre_var.set (genre_options[0])

    genre_opt = OptionMenu (add_window, genre_var, *genre_options)
    genre_opt.grid (row=2, column=1, sticky='w')

    genre_entry_variable = StringVar ()
    genre_entry_variable.set ('Enter Genre to be added')
    genre_add_entry = Entry (add_window, font=('arial', 7, 'bold'), textvariable=genre_entry_variable, relief='sunken',
                             bd=2)
    genre_add_entry.place (relx=0.621, rely=0.12, relheight=0.06, relwidth=0.29)

    genre_add_button = Button (add_window, text='add', command=add_genre)
    genre_add_button.place (relx=0.92, rely=0.12)

    # language chooseing---
    language_options = ['English', 'አማርኛ']
    language_var = StringVar ()
    language_var.set (language_options[0])

    language_opt = OptionMenu (add_window, language_var, *language_options)
    language_opt.grid (row=3, column=1, sticky='w')

    book_releaseYear_entry = Entry (add_window, width=5, font=('arial', 12, 'bold'), relief='sunken', bd=2)
    book_releaseYear_entry.grid (row=4, column=1, sticky='w', pady=3)
    book_pageNo_entry = Entry (add_window, width=8, font=('arial', 12, 'bold'), relief='sunken', bd=2)
    book_pageNo_entry.grid (row=5, column=1, sticky='w')
    book_publisher_entry = Entry (add_window, width=18, font=('arial', 12, 'bold'), relief='sunken', bd=2)
    book_publisher_entry.grid (row=6, column=1, sticky='w')

    # series chooosing---
    series_options = [i.strip () for i in open ('series', 'r', encoding='utf-8').readlines ()]
    series_var = StringVar ()
    series_var.set (series_options[0])

    series_opt = OptionMenu (add_window, series_var, *series_options)
    series_opt.grid (row=7, column=1, sticky='w')

    series_num_entry = Entry (add_window, width=10, font=('arial', 10, 'bold'), relief='sunken', bd=2)
    series_num_entry.place (relx=0.56, rely=0.43, relheight=0.06, relwidth=0.2)

    # state choosing--
    # state_options=[]
    # state_var=StringVar()
    # state_var.set(series_options[0])

    # state_opt=OptionMenu(add_window,series_var,*series_options)
    # state_opt.grid(row=7,column=1,sticky='w')

    # book_state_entry=Entry(add_window,width=30,font=('arial', 12, 'bold'),relief='sunken',bd=2)
    # book_state_entry.grid(row=7,column=1)

    # location chhoosing---

    location_options = [i.strip () for i in open ('location.txt', 'r', encoding='utf-8').readlines ()]
    location_var = StringVar ()
    location_var.set (location_options[0])

    location_opt = OptionMenu (add_window, location_var, *location_options)
    location_opt.grid (row=8, column=1, sticky='w')

    book_isbn_entry = Entry (add_window, width=20, font=('arial', 12, 'bold'), relief='sunken', bd=2)
    book_isbn_entry.grid (row=9, column=1, sticky='w', pady=4)
    book_description_entry = Text (add_window, width=30, height=3, font=('arial', 12, 'bold'), relief='sunken', bd=2)
    book_description_entry.grid (row=10, column=1, rowspan=2)

    book_tags_entry = Text (add_window, width=20, height=5, font=('arial', 9, 'bold'), relief='sunken', bd=2)
    book_tags_entry.grid (row=12, column=1, rowspan=3, sticky='w', pady=3)

    tags_options = [i.strip () for i in open ('tags.txt', 'r', encoding='utf-8').readlines ()]
    tags_var = StringVar ()
    tags_var.set (tags_options[0])

    tags_opt = OptionMenu (add_window, tags_var, *tags_options)
    tags_opt.place (relx=0.62, rely=0.76)

    tags_add_button = Button (add_window, text='add', command=insert_tags2entry)
    tags_add_button.place (relx=0.86, rely=0.765)

    photo_dir = []
    img_file = []
    # img1=ImageTk.PhotoImage(Image.open('gh.jpg').resize((100,100),Image.ANTIALIAS))

    book_image = Label (add_window, bg='red', text='Photo', compound='left')
    book_image.place (relx=0.78, rely=0.28)

    choose_image = Button (add_window, text='choose image', command=photo_choosing)
    choose_image.place (relx=0.785, rely=0.52)

    # picture if the user didnt specify one
    picture_dir = ['cover-page/nop.png']
    picture_fil = []

    add_button = Button (add_window, text='Add Book', relief='raised', bd=5, command=main)
    add_button.grid (row=16, column=1, sticky='e', padx=5)
    cancel_button = Button (add_window, text='Cancel', relief='raised', bd=5, command=cleaner)
    cancel_button.grid (row=16, column=2)

    last_id = 0
    last_id = get_lastID ()
    add_window.title ('Adding Book(#ID={})'.format (last_id + 1))

    add_window.mainloop()


main_window=Tk()
main_window.maxsize(1365,670)
main_window.minsize(1365,670)

menu_bar=Menu(main_window)
main_window.config(menu=menu_bar)



file_menu=Menu(menu_bar,tearoff=0)
file_menu.add_command(label="Add Book",command=main_start)
file_menu.add_command(labe="Info")
file_menu.add_separator()
file_menu.add_command(label="Exit Application",command=quit)
menu_bar.add_cascade(label='Database',menu=file_menu)

tab_control=ttk.Notebook(main_window)
booksTab=ttk.Frame(tab_control)
tab_control.add(booksTab,text='Books')
viewTab=ttk.Frame(tab_control)
tab_control.add(viewTab,text='View ')
tab_control.pack(fill='both',expand='yes')
can=Canvas(booksTab,bg='grey')
can.pack(fill='both',expand='yes')


sc_bar=Scrollbar(can,orient=VERTICAL,command=can.yview)
sc_bar.place(relx=1,rely=0,relheight=1,anchor=NE)

all_books=[]
tags_list=[]

def database_to_list():
    sql="SELECT * FROM books"
    for row in c.execute(sql):
        all_books.append(row)
    sql="SELECT * FROM tags"
    for row in c.execute(sql):
        print('tags',row)
        tags_list.append(row)
database_to_list()


print(all_books)

x_coOrdinates=[140,490,850,1200]
y_coOrdinate=100

x_counter=0



li={}

for i in all_books:
    no_img = ImageTk.PhotoImage (Image.open (i[13]).resize ((90, 100), Image.ANTIALIAS))
    li[i[0]]=no_img
def button_click(b_id):
    print(b_id)
    tab_control.select(1)
    populate_data(b_id)


def display_items(x_con,y_con,id,title,author,publisher,location,ispn,tag='1view'):
    can.create_window (x_con, y_con,tags=tag,
                       window=Button (can, image=li[id], width=240, height=120, wraplength=230, activebackground='red',
                                      fg='green', justify='left',
                                      text='ID: {} \nTITLE: {} \nAUTHOR: {}\nPUBLISHER: {} \nLOCATION: {} \nISPN: {}  '.format (
                                          id, title, author, publisher, location, ispn),
                                      compound='left',command=lambda :button_click(id)))








last_btn=[]
print('ola',all_books)
def books_tab_populate(search='',types=''):
    global y_coOrdinate,x_counter
    if search=='':
        can.delete('searched')
        last_btn.clear()
        x_counter=0
        y_coOrdinate=100
        for i in all_books:
            if x_counter < 3:
                display_items (x_coOrdinates[x_counter], y_coOrdinate, i[0], i[1], i[2], i[7], i[10], i[11])
                last_btn.clear ()
                last_btn.append ((x_coOrdinates[x_counter], y_coOrdinate))
                x_counter += 1
                print (i[0], i[1], i[2], i[7], i[8], i[11])

            elif x_counter == 3:
                display_items (x_coOrdinates[x_counter], y_coOrdinate, i[0], i[1], i[2], i[7], i[10], i[11])
                last_btn.clear ()
                last_btn.append ((x_coOrdinates[x_counter], y_coOrdinate))
                x_counter = 0
                y_coOrdinate += 180
    else:
        temp_list=[]
        print('types',types)
        if types=='Id':
            for i in all_books:
                if i[0]==int(search):
                    temp_list.append(i)
        elif types=='Book Title':
            for i in all_books:
                if i[1]==search:
                    temp_list.append(i)
        elif types=='Book Author':
            for i in all_books:
                if i[2]==search:
                    temp_list.append(i)
        elif types=='Series':
            for i in all_books:
                if i[8]==search:
                    temp_list.append(i)
        elif types=='Tag':
            for i in tags_list:
                if search ==i[0]:
                    for j in all_books:
                        if j[0] == i[1]:
                            temp_list.append (j)

        elif types=='All':
            for i in all_books:
                if str(i[0])==search or search in i[1] or search in i[2] or search in i[8]:
                    temp_list.append(i)
            for i in tags_list:
                if search ==i[0]:
                    for j in all_books:
                        if j[0]==i[1]:
                            temp_list.append(j)
        print('resuuu',temp_list)
        can.delete('1view')
        x_counter=0
        y_coOrdinate=100

        for i in temp_list:
            if x_counter < 3:
                display_items (x_coOrdinates[x_counter], y_coOrdinate, i[0], i[1], i[2], i[7], i[10], i[11],'searched')
                last_btn.clear ()
                last_btn.append ((x_coOrdinates[x_counter], y_coOrdinate))
                x_counter += 1
                print (i[0], i[1], i[2], i[7], i[8], i[11])

            elif x_counter == 3:
                display_items (x_coOrdinates[x_counter], y_coOrdinate, i[0], i[1], i[2], i[7], i[10], i[11],'searched')
                last_btn.clear ()
                last_btn.append ((x_coOrdinates[x_counter], y_coOrdinate))
                x_counter = 0
                y_coOrdinate += 180

    can.config (yscrollcommand=sc_bar.set, scrollregion=(0, 0, 0, y_coOrdinate + 100))
books_tab_populate()
print(last_btn)



def add_new_book(iid,title,author,publisher,location,ispn,pic):
    last_y=last_btn[0][1]
    li[iid]= ImageTk.PhotoImage (Image.open (pic).resize ((90, 100), Image.ANTIALIAS))

    if last_btn[0][0]==1200:
        display_items (140, last_btn[0][1]+180, iid,title,author,publisher,location,ispn)
        last_btn.clear ()
        last_btn.append ((140,last_y+180))
        can.config (yscrollcommand=sc_bar.set, scrollregion=(0, 0, 0, last_btn[0][1]+180 + 100))
    elif last_btn[0][0]==140:
        display_items (490, last_btn[0][1],iid,title,author,publisher,location,ispn)
        last_btn.clear ()
        last_btn.append ((490,last_y))
        can.config (yscrollcommand=sc_bar.set, scrollregion=(0, 0, 0, last_btn[0][1] + 100))
    elif last_btn[0][0]==490:
        display_items (850, last_btn[0][1], iid,title,author,publisher,location,ispn)
        last_btn.clear ()
        last_btn.append ((850, last_y ))
        can.config (yscrollcommand=sc_bar.set, scrollregion=(0, 0, 0, last_btn[0][1] + 100))
    elif last_btn[0][0]==850:
        display_items (1200, last_btn[0][1],iid,title,author,publisher,location,ispn)
        last_btn.clear ()
        last_btn.append ((1200,last_y ))
        can.config (yscrollcommand=sc_bar.set, scrollregion=(0, 0, 0, last_btn[0][1] + 100))





search_books_entry=Entry(booksTab,relief='raised',bd=5)
can.create_window(1050,20,window=search_books_entry)


search_list=['Id','Book Title','Book Author','Series','Tag','All']
search_var=StringVar()
search_var.set(search_list[0])

search_opt = OptionMenu (booksTab, search_var, *search_list)
can.create_window(1150,20,window=search_opt,height=20)

search_button=Button(booksTab,text='Search',relief='raised',bd=5,command=lambda :books_tab_populate(search_books_entry.get(),search_var.get()))
can.create_window(1220,20,window=search_button,height=30)



#mb=Button(main_window,text='ha',command=lambda :add_new_book('iid','itle','author','publisher','location','ispn'))
#mb.place(relx=0,rely=0)




#====================================================================================================================================================

id_label=Label(viewTab,text='ID=',font=('arial', 12, 'bold'))
id_label.grid(row=1,column=0)

photo_label=Label(viewTab,text='Photo',bg='blue',width=40,height=23)
photo_label.grid(row=2,column=0,rowspan=8)

title_label=Label(viewTab,text='Title:',font=('arial', 12, 'bold'))
title_label.grid(row=2,column=1,sticky='w')

author_label=Label(viewTab,text='Author:',font=('arial', 12, 'bold'))
author_label.grid(row=3,column=1,sticky='w')

location_label=Label(viewTab,text='Location:',font=('arial', 12, 'bold'))
location_label.grid(row=4,column=1,sticky='w')


genre_label=Label(viewTab,text='Genre:',font=('arial', 12, 'bold'))
genre_label.grid(row=5,column=1,sticky='w')

language_label=Label(viewTab,text='Language:',font=('arial', 12, 'bold'))
language_label.grid(row=6,column=1,sticky='w')

releaseDate_label=Label(viewTab,text='Realease date:',font=('arial', 12, 'bold'))
releaseDate_label.grid(row=7,column=1,sticky='w')

noPage_label=Label(viewTab,text='Page No:',font=('arial', 12, 'bold'))
noPage_label.grid(row=8,column=1,sticky='w')

publisher_label=Label(viewTab,text='Publisher:',font=('arial', 12, 'bold'))
publisher_label.grid(row=9,column=1,sticky='w')

series_label=Label(viewTab,text='Series:',font=('arial', 12, 'bold'))
series_label.grid(row=10,column=1,sticky='w')

seriesId_label=Label(viewTab,text='Id:',font=('arial', 12, 'bold'))
seriesId_label.grid(row=10,column=3,sticky='w')

isbn_label=Label(viewTab,text='ISBN:',font=('arial', 12, 'bold'))
isbn_label.grid(row=11,column=1,sticky='w')

description_label=Label(viewTab,text='Description:',font=('arial', 12, 'bold'))
description_label.grid(row=12,column=1,sticky='w')

tags_label=Label(viewTab,text='Tags:',font=('arial', 12, 'bold'))
tags_label.grid(row=15,column=1,sticky='w')

dateAdded_label=Label(viewTab,text='Date Added:',font=('arial', 12, 'bold'))
dateAdded_label.grid(row=16,column=1,sticky='w')


def exiting_edit():
    edit_title_entry.grid_forget()
    edit_location_entry.grid_forget()
    edit_author_entry.grid_forget()
    edit_genre_entry.grid_forget()
    edit_language_entry.grid_forget()
    edit_releaseDate_entry.grid_forget()
    edit_numPage_entry.grid_forget()
    edit_publisher_entry.grid_forget()
    edit_series_entry.grid_forget()
    edit_seriesID_entry.grid_forget()
    edit_isbn_entry.grid_forget()
    edit_tags_entry.grid_forget()
def canceling_edit(bid):
    exiting_edit()
    populate_data(bid)
    edit_button.config(state='active')
    edit_save_button.place_forget()
    edit_cancel_button.place_forget()


def writing_edit2database(bkid):
    sql="UPDATE books SET book_title='{}',book_author='{}',genre='{}',language='{}',release_date='{}',number_of_pages='{}',publisher='{}',series='{}',series_id='{}',location='{}',isbn='{}',book_description='{}' WHERE book_id = '{}'".format(edit_title_entry.get(),
                    edit_author_entry.get(),edit_genre_entry.get(),edit_language_entry.get(),edit_releaseDate_entry.get(),edit_numPage_entry.get(),edit_publisher_entry.get(),
                    edit_series_entry.get(),edit_seriesID_entry.get(),edit_location_entry.get(),edit_isbn_entry.get(),description_labelView.get(0.0,'end'),bkid)
    c.execute(sql)
    ta=edit_tags_entry.get()
    ta=ta.split('#')
    for i in ta:
        if i in [j.strip().strip('#') for j in open('tags.txt','r')]:
            pass
        else:
            open('tags.txt','a').writelines('\n'+'#'+i)
            c.execute ('INSERT INTO tags (tags,book_id) VALUES(?,?)', ('#'+i, bkid))
    conn.commit()
    canceling_edit(bkid)


def editing_data_():
    global edit_title_entry,edit_location_entry,edit_save_button,edit_cancel_button,edit_genre_entry,edit_author_entry,edit_language_entry,edit_releaseDate_entry,edit_numPage_entry,edit_publisher_entry,edit_series_entry,edit_seriesID_entry,edit_isbn_entry,edit_tags_entry
    edit_button.config(state='disabled')
    edit_save_button=Button(viewTab,text='Save',command=lambda: writing_edit2database(id_label['text'].split(':')[-1]))
    edit_save_button.place(relx=0.7,rely=0.9,relwidth=0.04)

    edit_cancel_button=Button(viewTab,text='Cancel',command=lambda: canceling_edit(id_label['text'].split(':')[-1]))
    edit_cancel_button.place(relx=0.75,rely=0.9)
    # vars
    title_var = StringVar ()
    locat_var = StringVar ()
    genr_var = StringVar ()
    lang_var = StringVar ()
    releaseDate_var = StringVar ()
    numPage_var = StringVar ()
    publisher_var = StringVar ()
    seri_var = StringVar ()
    seriId_var = StringVar ()
    isbn_var = StringVar ()
    tag_var = StringVar ()
    author_var=StringVar()


    title_var.set(title_label['text'].split(':')[-1])
    locat_var.set(location_label['text'].split(':')[-1])
    genr_var.set(genre_label['text'].split(':')[-1])
    lang_var.set(language_label['text'].split(':')[-1])
    releaseDate_var.set(releaseDate_label['text'].split(':')[-1])
    numPage_var.set(noPage_label['text'].split(':')[-1])
    publisher_var.set(publisher_label['text'].split(':')[-1])
    seri_var.set(series_label['text'].split(':')[-1])
    seriId_var.set(seriesId_label['text'].split(':')[-1])
    isbn_var.set(isbn_label['text'].split(':')[-1])
    tag_var.set(tags_label['text'].split(':')[-1])
    author_var.set(author_label['text'].split(':')[-1])



    title_label.config (text='Title:')
    author_label.config (text='Author:')
    location_label.config (text='Location:')
    genre_label.config (text='Genre:')
    language_label.config (text='Language:')
    releaseDate_label.config (text='Release Date:')
    noPage_label.config (text='Number of Pages:')
    publisher_label.config (text='Publisher:')
    series_label.config (text='Series:')
    seriesId_label.config (text='id:')
    isbn_label.config (text='ISBN:')
    tags_label.config(text='Tags:')
    #description_labelView.insert (0.0,




    edit_title_entry=Entry(viewTab,textvariable=title_var,width=20)
    edit_title_entry.grid(row=2,column=2,sticky='w')
    edit_author_entry = Entry (viewTab, textvariable=author_var, width=20)
    edit_author_entry.grid (row=3, column=2, sticky='w')
    edit_location_entry=Entry(viewTab,textvariable=locat_var)
    edit_location_entry.grid(row=4,column=2,sticky='w')
    edit_genre_entry=Entry(viewTab,textvariable=genr_var)
    edit_genre_entry.grid(row=5,column=2,sticky='w')
    edit_language_entry=Entry(viewTab,textvariable=lang_var)
    edit_language_entry.grid(row=6,column=2,sticky='w')
    edit_releaseDate_entry=Entry(viewTab,textvariable=releaseDate_var)
    edit_releaseDate_entry.grid(row=7,column=2,sticky='w')
    edit_numPage_entry=Entry(viewTab,textvariable=numPage_var)
    edit_numPage_entry.grid(row=8,column=2,sticky='w')
    edit_publisher_entry=Entry(viewTab,textvariable=publisher_var)
    edit_publisher_entry.grid(row=9,column=2,sticky='w')
    edit_series_entry=Entry(viewTab,textvariable=seri_var)
    edit_series_entry.grid(row=10,column=2,sticky='w')
    edit_seriesID_entry=Entry(viewTab,textvariable=seriId_var)
    edit_seriesID_entry.grid(row=10,column=4,sticky='w')
    edit_isbn_entry=Entry(viewTab,textvariable=isbn_var)
    edit_isbn_entry.grid(row=11,column=2,sticky='w')

    edit_tags_entry=Entry(viewTab,textvariable=tag_var)
    edit_tags_entry.grid(row=15,column=2,sticky='w')





edit_button=Button(viewTab,text='Edit Data',command=editing_data_)
edit_button.place(relx=0.9,rely=0.02,relwidth=0.05)


#----

description_labelView=Text(viewTab,height=8,width=30)
description_labelView.grid(row=12,column=2,sticky='w')

viewImage=[]
viewData=[]

photo_label.config(width=220,height=370)
def populate_data(bookId):
    bk_data=''

    for row in c.execute('SELECT * FROM books WHERE book_id = {}'.format(bookId)):
        bk_data=row
    print(bk_data)
    viewData.clear ()
    viewImage.clear ()
    viewImage.append(bk_data[-2])

    for i in viewImage:
        view_i = ImageTk.PhotoImage (Image.open (i).resize ((200, 350), Image.ANTIALIAS))
        viewData.append(view_i)
    photo_label.config(image=viewData[0])
    id_label.config(text='ID:{}'.format(bk_data[0]))
    title_label.config(text='Title:{}'.format(bk_data[1]))
    author_label.config(text='Author:{}'.format(bk_data[2]))
    location_label.config(text='Location:{}'.format(bk_data[10]))
    genre_label.config(text='Genre:{}'.format(bk_data[3]))
    language_label.config(text='Language:{}'.format(bk_data[4]))
    releaseDate_label.config(text='Release Date:{}'.format(bk_data[5]))
    noPage_label.config(text='Number of Pages:{}'.format(bk_data[6]))
    publisher_label.config(text='Publisher:{}'.format(bk_data[7]))
    series_label.config(text='Series:{}'.format(bk_data[8]))
    seriesId_label.config(text='id:{}'.format(bk_data[9]))
    isbn_label.config(text='ISBN:{}'.format(bk_data[11]))
    description_labelView.insert(0.0,bk_data[-3])

    tags = ''
    for row in c.execute ('SELECT * FROM tags WHERE book_id = {}'.format (bookId)):
        print (row)
        tags += row[0]
    tags_label.config(text='Tags:{}'.format(tags))


    dateAdded_label.config(text='Date Added:{}'.format(bk_data[-1]))










main_window.mainloop()