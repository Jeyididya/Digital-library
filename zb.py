from tkinter import *


root=Tk()
root.title('books')

root.minsize (900, 640)
root.maxsize (900, 640)

menu_bar=Menu(root)
root.config(menu=menu_bar)


file_menu=Menu(menu_bar,tearoff=0)
file_menu.add_command(label="Add Book")
file_menu.add_command(labe="Edit Book")
file_menu.add_command(labe="Info")
file_menu.add_separator()
file_menu.add_command(label="Exit Application")
menu_bar.add_cascade(label='Database',menu=file_menu)







def view_page():
    l=Label(root,text='jola')
    l.pack()

root.mainloop()
