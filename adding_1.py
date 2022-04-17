import os
import shutil
import sqlite3
from tkinter import *
from datetime import *
from PIL import Image,ImageTk
from tkinter import filedialog
from tkinter import messagebox



try:
    os.makedir('cover-page')
except:
    pass



add_window=Tk()
'''                            
 ######   ######   #           #       #          ######      
 #        #    #   #                   #          #    #
 ######   ######   #           #     #####        ######
      #        #   #           #       #          # 
 ######        #   ######      #       ######     ######
              
'''
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


















'''
#            #        #####    #######    #
#           # #       #    #   #          #
#          #####      #####    #######    #
#         #     #     #    #   #          #
#######  #       #    ######   #######    #######



'''




book_title=Label(add_window,text='Book Title',font=('arial', 12, 'bold'))
book_title.grid(row=0,column=0)
book_author=Label(add_window,text='Book Author',font=('arial', 12, 'bold'))
book_author.grid(row=1,column=0,pady=2)
book_genre=Label(add_window,text='Genre',font=('arial', 12, 'bold'))
book_genre.grid(row=2,column=0)
book_language=Label(add_window,text='Language',font=('arial', 12, 'bold'))
book_language.grid(row=3,column=0)
book_releaseYear=Label(add_window,text='Release Year',font=('arial', 12, 'bold'))
book_releaseYear.grid(row=4,column=0)
book_pageNo=Label(add_window,text='Page Number',font=('arial', 12, 'bold'))
book_pageNo.grid(row=5,column=0,pady=2)
book_publisher=Label(add_window,text='Publisher',font=('arial', 12, 'bold'))
book_publisher.grid(row=6,column=0,pady=2)
book_series=Label(add_window,text='Series',font=('arial', 12, 'bold'))
book_series.grid(row=7,column=0)
book_seriesNum=Label(add_window,text='id',font=('arial', 12, 'bold'))
book_seriesNum.place(relx=0.51,rely=0.43)


book_location=Label(add_window,text='Location',font=('arial', 12, 'bold'))
book_location.grid(row=8,column=0)
book_isbn=Label(add_window,text='ISBN',font=('arial', 12, 'bold'))
book_isbn.grid(row=9 ,column=0)
book_description =Label(add_window,text='Book Description',font=('arial', 12, 'bold'))
book_description.grid(row=10,column=0,pady=2)

book_tags=Label(add_window,text='Book Tags',font=('arial', 12, 'bold'))
book_tags.grid(row=13,column=0)





'''
  ######   ##    #   #######    ######     #     #
  #        # #   #      #       #     #     #   #
  ######   #  #  #      #       ######       # #
  #        #   # #      #       #  #          #
  ######   #    ##      #       #   #         #
'''


book_title_entry=Entry(add_window,width=30,font=('arial', 12, 'bold'),relief='sunken',bd=2)
book_title_entry.grid(row=0,column=1)
book_author_entry=Entry(add_window,width=30,font=('arial', 12, 'bold'),relief='sunken',bd=2)
book_author_entry.grid(row=1,column=1)
#genre choosing---
genre_options=[i.strip() for i in open('genre.txt','r',encoding='utf-8').readlines()]
genre_var=StringVar()
genre_var.set(genre_options[0])

genre_opt=OptionMenu(add_window,genre_var,*genre_options)
genre_opt.grid(row=2,column=1,sticky='w')

genre_entry_variable=StringVar()
genre_entry_variable.set('Enter Genre to be added')
genre_add_entry=Entry(add_window,font=('arial', 7, 'bold'),textvariable=genre_entry_variable,relief='sunken',bd=2)
genre_add_entry.place(relx=0.621,rely=0.12,relheight=0.06,relwidth=0.29)
def add_genre():
    open('genre.txt','a').write('\n'+genre_add_entry.get ())
    print(genre_add_entry.get ())
    option_menu = genre_opt.children['menu']
    option_menu.add_command (label=genre_add_entry.get (), command=lambda v=genre_var, l=genre_add_entry.get (): v.set (l))
genre_add_button=Button(add_window,text='add',command=add_genre)
genre_add_button.place(relx=0.92,rely=0.12)



#language chooseing---
language_options=['English','አማርኛ']
language_var=StringVar()
language_var.set(language_options[0])

language_opt=OptionMenu(add_window,language_var,*language_options)
language_opt.grid(row=3,column=1,sticky='w')


book_releaseYear_entry=Entry(add_window,width=5,font=('arial', 12, 'bold'),relief='sunken',bd=2)
book_releaseYear_entry.grid(row=4,column=1,sticky='w',pady=3)
book_pageNo_entry=Entry(add_window,width=8,font=('arial', 12, 'bold'),relief='sunken',bd=2)
book_pageNo_entry.grid(row=5,column=1,sticky='w')
book_publisher_entry=Entry(add_window,width=18,font=('arial', 12, 'bold'),relief='sunken',bd=2)
book_publisher_entry.grid(row=6,column=1,sticky='w')

#series chooosing---
series_options=[i.strip() for i in open('series','r',encoding='utf-8').readlines()]
series_var=StringVar()
series_var.set(series_options[0])

series_opt=OptionMenu(add_window,series_var,*series_options)
series_opt.grid(row=7,column=1,sticky='w')

series_num_entry=Entry(add_window,width=10,font=('arial', 10, 'bold'),relief='sunken',bd=2)
series_num_entry.place(relx=0.56,rely=0.43,relheight=0.06,relwidth=0.2)


#state choosing--
#state_options=[]
#state_var=StringVar()
#state_var.set(series_options[0])

#state_opt=OptionMenu(add_window,series_var,*series_options)
#state_opt.grid(row=7,column=1,sticky='w')

#book_state_entry=Entry(add_window,width=30,font=('arial', 12, 'bold'),relief='sunken',bd=2)
#book_state_entry.grid(row=7,column=1)


#location chhoosing---

location_options=[i.strip() for i in open('location.txt','r',encoding='utf-8').readlines()]
location_var=StringVar()
location_var.set(location_options[0])

location_opt=OptionMenu(add_window,location_var,*location_options)
location_opt.grid(row=8,column=1,sticky='w')


book_isbn_entry=Entry(add_window,width=20,font=('arial', 12, 'bold'),relief='sunken',bd=2)
book_isbn_entry.grid(row=9,column=1,sticky='w',pady=4)
book_description_entry=Text(add_window,width=30,height=3,font=('arial', 12, 'bold'),relief='sunken',bd=2)
book_description_entry.grid(row=10,column=1,rowspan=2)

book_tags_entry=Text(add_window,width=20,height=5,font=('arial', 9, 'bold'),relief='sunken',bd=2)
book_tags_entry.grid(row=12,column=1,rowspan=3,sticky='w',pady=3)

tags_options=[i.strip() for i in open('tags.txt','r',encoding='utf-8').readlines()]
tags_var=StringVar()
tags_var.set(tags_options[0])

tags_opt=OptionMenu(add_window,tags_var,*tags_options)
tags_opt.place(relx=0.62,rely=0.76)

def insert_tags2entry():
    book_tags_entry.insert('end','\n'+tags_var.get()+'\n')


tags_add_button=Button(add_window,text='add',command=insert_tags2entry)
tags_add_button.place(relx=0.86,rely=0.765)





photo_dir=[]
img_file=[]
#img1=ImageTk.PhotoImage(Image.open('gh.jpg').resize((100,100),Image.ANTIALIAS))

book_image=Label(add_window,bg='red',text='Photo',compound='left')
book_image.place(relx=0.78,rely=0.28)

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

choose_image=Button(add_window,text='choose image',command=photo_choosing)
choose_image.place(relx=0.785,rely=0.52)

#picture if the user didnt specify one
picture_dir = ['cover-page/nop.png']
picture_fil = []


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
        else:
            shutil.move(picture,'cover-page')
            os.rename('cover-page/'+picture.split('/')[-1],'cover-page/{}'.format(book_title_entry.get()+'.'+picture.split('/')[-1].split('.')[-1]))
            picture_n= 'cover-page/{}'.format(book_title_entry.get()+'.'+picture.split('/')[-1].split('.')[-1])
            add_to_database (book_title_entry.get (), book_author_entry.get (), genre_var.get (), language_var.get (),
                             book_releaseYear_entry.get (), book_pageNo_entry.get (),
                             book_publisher_entry.get (), series_var.get (), series_num_entry.get (),
                             location_var.get (), book_isbn_entry.get (), str(book_description_entry.get (0.0, 'end')),
                             picture_n)




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

add_button=Button(add_window,text='Add Book',relief='raised',bd=5,command=main)
add_button.grid(row=16,column=1,sticky='e',padx=5)
cancel_button=Button(add_window,text='Cancel',relief='raised',bd=5,command=cleaner)
cancel_button.grid(row=16,column=2)




#---title ----
import sqlite3
conn=sqlite3.connect('library.db')
c=conn.cursor()
last_id=0

def get_lastID():
    for i in c.execute('SELECT  MAX(book_id) FROM books'):
        return i[0]
last_id=get_lastID()
add_window.title('Adding Book(#ID={})'.format(last_id+1))



add_window.mainloop()
