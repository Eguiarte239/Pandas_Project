import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(True)

mw = tk.Tk()
mw.title('Proyecto')
mw.geometry("630x600") 
mw.resizable(0, 0)

btnMainFilter = tk.Button(text='Filtrar', command='')
btnMainFilter.place(x = 120, y = 45, width=100, height=25)
 
comboboxMainFilter = ttk.Combobox(mw,value='')
comboboxMainFilter.set('Filtrado')
comboboxMainFilter.place(x = 78, y = 15)

btnSecFilter = tk.Button(text='Filtrar', command='')
btnSecFilter.place(x = 420, y = 45, width=100, height=25)

comboboxSecFilter = ttk.Combobox(mw,value='')
comboboxSecFilter.set('Filtrado')
comboboxSecFilter.place(x = 378, y = 15)

listboxData = tk.Listbox(mw)
listboxData.grid(padx = 50, pady= 75)
listboxData.config(width=65, height=20)
 
mw.mainloop()