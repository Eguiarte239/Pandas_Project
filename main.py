import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
import ctypes
import pandas as pd
import graphsClass

if __name__ == '__main__':

    ctypes.windll.shcore.SetProcessDpiAwareness(True)

    df = pd.read_csv('pedido.csv')

    graphsObject = graphsClass.Graphs()

    GRAPHS = ('Productos más vendidos (5 años)', 'Montos (3 meses)', 'Clientes-producto más vendido (5 años)', 'Empleados con más ventas (Último mes)', 'Productos más solicitados (primer semestre)', 'Clientes frecuentes (primer semestre)')

    mw = tk.Tk()
    mw.title('Proyecto')
    mw.geometry("630x600") 
    mw.resizable(0, 0)

    selectGraph = ttk.Combobox(mw,value=GRAPHS, width=33)
    selectGraph.set('Gráficas')
    selectGraph.place(x = 60, y = 15)

    btnGraphs = tk.Button(text='Gráficas', command= lambda: graphsObject.graphSelected(selectGraph, GRAPHS, df, listboxData))
    btnGraphs.place(x = 120, y = 45, width=100, height=25)
    
    btnSecFilter = tk.Button(text='Reportes', command='')
    btnSecFilter.place(x = 420, y = 45, width=100, height=25)

    comboboxSecFilter = ttk.Combobox(mw,value='')
    comboboxSecFilter.set('Filtrado')
    comboboxSecFilter.place(x = 378, y = 15)

    listboxData = tk.Listbox(mw)
    listboxData.grid(padx = 50, pady= 75)
    listboxData.config(width=65, height=20)
    
    mw.mainloop()