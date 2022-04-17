from tkinter import *
from PIL import Image,ImageTk

root=Tk()
def resize_img(imgname):
    image = Image.open (imgname)
    image = image.resize ((50, 50), Image.ANTIALIAS)
    my_ing = ImageTk.PhotoImage (image)
    return my_ing


van=Canvas(root,bg='blue',width=500,height=500)
van.pack()

scr=Scrollbar(van,orient=VERTICAL,command=van.yview)
scr.place(relx=1,rely=0,relheight=1,anchor=NE)



ls=['lk.gif','g.png','hj.jpg','g.png','lk.gif','g.png','hj.jpg','g.png','lk.gif','g.png','hj.jpg','g.png','lk.gif','g.png','hj.jpg','g.png','lk.gif','g.png','hj.jpg','g.png','lk.gif','g.png','hj.jpg','g.png','lk.gif','g.png','hj.jpg','g.png','lk.gif','g.png','hj.jpg','g.png']
ll=[]
for i in ls:
    img1 = ImageTk.PhotoImage (Image.open (i).resize ((50, 50), Image.ANTIALIAS))
    ll.append(img1)
y=30
for i in range(len(ll)):
    van.create_window(50,y,window=Label(van,image=ll[i],text='Name:\nAuthor:',compound='left'))
    y+=40

van.config(yscrollcommand=scr.set,scrollregion=(0,0,0,y))
root.mainloop()


