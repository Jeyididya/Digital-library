import os
import sqlite3
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk



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


main_window=Tk()
main_window.maxsize(1365,670)
main_window.minsize(1365,670)

menu_bar=Menu(main_window)
main_window.config(menu=menu_bar)

def ad():
    os.stat('adding_1.py')


file_menu=Menu(menu_bar,tearoff=0)
file_menu.add_command(label="Add Book",command=ad)
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

def database_to_list():
    sql="SELECT * FROM books"
    for row in c.execute(sql):
        all_books.append(row)
        print('r',row,all_books)
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


def display_items(x_con,y_con,id,title,author,publisher,location,ispn):
    can.create_window (x_con, y_con,
                       window=Button (can, image=li[id], width=240, height=120, wraplength=230, activebackground='red',
                                      fg='green', justify='left',
                                      text='ID: {} \nTITLE: {} \nAUTHOR: {}\nPUBLISHER: {} \nLOCATION: {} \nISPN: {}  '.format (
                                          id, title, author, publisher, location, ispn),
                                      compound='left',command=lambda :button_click(id)))








last_btn=[]

for i in all_books:
    if x_counter<3:
        display_items(x_coOrdinates[x_counter],y_coOrdinate,i[0],i[1],i[2],i[7],i[10],i[11])
        last_btn.clear()
        last_btn.append ((x_coOrdinates[x_counter],y_coOrdinate))
        x_counter+=1
        print(i[0],i[1],i[2],i[7],i[8],i[11])

    elif x_counter==3:
        display_items (x_coOrdinates [x_counter], y_coOrdinate, i[0],i[1],i[2],i[7],i[10],i[11])
        last_btn.clear()
        last_btn.append ((x_coOrdinates[x_counter], y_coOrdinate))
        x_counter=0
        y_coOrdinate+=180
can.config(yscrollcommand=sc_bar.set,scrollregion=(0,0,0,y_coOrdinate+100))

print(last_btn)

def add_new_book(iid,title,author,publisher,location,ispn):
    last_y=last_btn[0][1]
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
location_label.grid(row=3,column=1,sticky='w')


genre_label=Label(viewTab,text='Genre:',font=('arial', 12, 'bold'))
genre_label.grid(row=4,column=1,sticky='w')

language_label=Label(viewTab,text='Language:',font=('arial', 12, 'bold'))
language_label.grid(row=5,column=1,sticky='w')

releaseDate_label=Label(viewTab,text='Realease date:',font=('arial', 12, 'bold'))
releaseDate_label.grid(row=6,column=1,sticky='w')

noPage_label=Label(viewTab,text='Page No:',font=('arial', 12, 'bold'))
noPage_label.grid(row=7,column=1,sticky='w')

publisher_label=Label(viewTab,text='Publisher:',font=('arial', 12, 'bold'))
publisher_label.grid(row=8,column=1,sticky='w')

series_label=Label(viewTab,text='Series:',font=('arial', 12, 'bold'))
series_label.grid(row=9,column=1,sticky='w')

seriesId_label=Label(viewTab,text='Id:',font=('arial', 12, 'bold'))
seriesId_label.grid(row=9,column=2,sticky='w')

isbn_label=Label(viewTab,text='ISBN:',font=('arial', 12, 'bold'))
isbn_label.grid(row=10,column=1,sticky='w')

description_label=Label(viewTab,text='Description:',font=('arial', 12, 'bold'))
description_label.grid(row=11,column=1,sticky='w')

tags_label=Label(viewTab,text='Tags:',font=('arial', 12, 'bold'))
tags_label.grid(row=14,column=1,sticky='w')

dateAdded_label=Label(viewTab,text='Date Added:',font=('arial', 12, 'bold'))
dateAdded_label.grid(row=15,column=1)


#----

description_labelView=Text(viewTab,height=8,width=30)
description_labelView.grid(row=11,column=2,sticky='w')

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