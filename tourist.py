from db import get_tourist
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
    
  
  l1 = Label(page,text='name')
  l1.pack()
  e1 = Entry(page)
  e1.pack()
  
  l2 = Label(page,text='phone no')
  l2.pack()
  e2 = Entry(page)
  e2.pack()
  
  b1 = Button(page,text='Add Tourist')
  b1.pack()
  
  
  
  