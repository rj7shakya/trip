from db import get_tourist,add_tourist
from tkinter import *
from tkinter import ttk


def setup_tourist(page):
  tree = ttk.Treeview(page,columns=['a','b'])
  tree['show'] = 'headings'
  tree.heading('a',text='name')
  tree.heading('b',text='phone no')
  tree.pack()
  
  data = get_tourist()
  
  for id,name,phone_no in data:
    tree.insert("",END,values=(name,phone_no))
    
  l3 = Label(page,text='Id')
  l3.pack()
  e3 = Entry(page)
  e3.pack()
  
  l1 = Label(page,text='name')
  l1.pack()
  e1 = Entry(page)
  e1.pack()
  
  l2 = Label(page,text='phone no')
  l2.pack()
  e2 = Entry(page)
  e2.pack()
  
  def on_add():
    add_tourist(e3.get(),e1.get(),e2.get())
    tree.insert("",END,values=(e1.get(),e2.get()))
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
  
  b1 = Button(page,text='Add Tourist',command=on_add)
  b1.pack()
  
  
  
  