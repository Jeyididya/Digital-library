from tkinter import *
from tkinter import ttk


from PIL import Image,ImageTk

root=Tk()
tab_control=ttk.Notebook(root)
booksTab=ttk.Frame(tab_control)
tab_control.add(booksTab,text='Books')
tab_control.pack(fill='both',expand='yes')
can=Canvas(booksTab,bg='grey')
can.pack(fill='both',expand='yes')



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




def resize_img(imgname):
    image = Image.open (imgname)
    image = image.resize ((50, 50), Image.ANTIALIAS)
    my_ing = ImageTk.PhotoImage (image)
    return my_ing


ls=['lk.gif']
li=[]

for i in ls:
      img1=ImageTk.PhotoImage(Image.open('lk.gif').resize((120,150),Image.ANTIALIAS))
      li.append(img1)
def lab(xcon,ycon,id,title,author,publisher,location,ispn,img=''):

    can.create_window (xcon, ycon,
                       window=Button (can, image=li[0], width=240, height=120, wraplength=230, activebackground='red',
                                      fg='green', justify='left',
                                      text='ID: {} \nTITLE: {} \nAUTHOR: {}\nPUBLISHER: {} \nLOCATION: {} \nISPN: {}  '.format(id,title,author,publisher,location,ispn),
                                      compound='left'))

#cox=[140,490,850,1200]
#num=100
#fls=[]
#for i in range(num):
#    fls.append('a'+str(i))
#nu=0
#coy=100
#for i in fls:
#    if nu<3:
#        lab(cox[nu],coy,'id','ti','aut','pub','loc','ispn')
#        nu+=1
#    elif nu==3:
#        lab (cox[nu], coy, 'id', 'ti', 'aut', 'pub', 'loc', 'ispn')
#        nu=0
#        coy+=180

#can.config(yscrollcommand=sc_bar.set,scrollregion=(0,0,0,coy))

root.mainloop()