from tkinter import *
from tkinter import ttk
import sqlite3
from datetime import*

from PIL import Image,ImageTk

conn=sqlite3.connect('library.db')

c=conn.cursor()

def refresh():
    cox = [140, 490, 850, 1200]
    num = 100
    sql = "SELECT * FROM BOOKS"
    fls = c.execute (sql)

    nu = 0
    coy = 100
    for i in fls:
        if nu < 3:
            lab (cox[nu], coy, i[0], i[1], i[2], i[8], i[5], i[9])
            nu += 1
        elif nu == 3:
            lab (cox[nu], coy, i[0], i[1], i[2], i[8], i[5], i[9])
            nu = 0
            coy += 180

    can.config (yscrollcommand=sc_bar.set, scrollregion=(0, 0, 0, coy))


root=Tk()
tab_control=ttk.Notebook(root)
booksTab=ttk.Frame(tab_control)
tab_control.add(booksTab,text='Books')
tab_control.pack(fill='both',expand='yes')
can=Canvas(booksTab,bg='grey')
can.pack(fill='both',expand='yes')

#print(can.winfo_width())
#print(can.winfo_height())


ref=Button(root,text='Refresh',bd=5,command=refresh)
can.create_window(970,20,window=ref)
search_entry=Entry(can)
search_btn=Button(can,text='Search',bd=5)
can.create_window(1100,20,window=search_entry,width=200)
can.create_window(1230,22,window=search_btn,height=20)
sc_bar=Scrollbar(can,orient=VERTICAL,command=can.yview)
sc_bar.place(relx=1,rely=0,relheight=1,anchor=NE)
can.config(yscrollcommand=sc_bar.set,scrollregion=(0,0,0,3000))


def resize_img(imgname):
    image = Image.open (imgname)
    image = image.resize ((50, 50), Image.ANTIALIAS)
    my_ing = ImageTk.PhotoImage (image)
    return my_ing


ls=['C:/Users/jedidiah/PycharmProjects/library/main/lk.gif']
li=[]

for i in ls:
      img1=ImageTk.PhotoImage(Image.open('C:/Users/jedidiah/PycharmProjects/library/main/lk.gif').resize((120,150),Image.ANTIALIAS))
      li.append(img1)

def lab(xcon,ycon,id,title,author,publisher,location,ispn,img=''):

    can.create_window (xcon, ycon,
                       window=Button (can, image=li[0], width=240, height=120, wraplength=230, activebackground='red',
                                      fg='green', justify='left',
                                      text='ID: {} \nTITLE: {} \nAUTHOR: {}\nPUBLISHER: {} \nLOCATION: {} \nISPN: {}  '.format(id,title,author,publisher,location,ispn),
                                      compound='left'))






root.mainloop()