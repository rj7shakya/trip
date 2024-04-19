from tkinter import *
from tkinter import ttk

root = Tk()
tab = ttk.Notebook(root)

tourist_page = Frame(tab,bg='red')
guide_page = Frame(tab,bg='pink')
trip_page = Frame(tab,bg='orange')

tab.add(tourist_page,text='Tourist')
tab.add(guide_page,text='Guide')
tab.add(trip_page,text='Trip')
tab.pack(expand = 1, fill ="both") 

from tourist import setup_tourist

setup_tourist()


root.geometry('500x500')
root.mainloop() 