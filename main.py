import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
import ctypes
import pandas as pd
import graphsClass
import reportsClass

if __name__ == '__main__':

    ctypes.windll.shcore.SetProcessDpiAwareness(True)

    df = pd.read_csv('pedido.csv')

    graphsObject = graphsClass.Graphs()
    reportsObject = reportsClass.Reports()

    OPTIONS = ('Productos más vendidos', 'Montos', 'Clientes-producto más vendido', 'Empleados con más ventas', 'Productos más solicitados', 'Clientes frecuentes')

    mw = tk.Tk()
    mw.title('Proyecto')
    mw.geometry("630x600") 
    mw.resizable(0, 0)

    selectGraph = ttk.Combobox(mw,value=OPTIONS, width=24)
    selectGraph.set('Gráficas')
    selectGraph.place(x = 60, y = 15)

    btnGraphs = tk.Button(text='Gráficas', command= lambda: graphsObject.graphSelected(selectGraph, OPTIONS, df))
    btnGraphs.place(x = 120, y = 45, width=100, height=25)

    selectReport = ttk.Combobox(mw,value=OPTIONS, width=24)
    selectReport.set('Reportes')
    selectReport.place(x = 378, y = 15)
    
    btnReports = tk.Button(text='Reportes', command= lambda: reportsObject.reportSelected(selectReport, OPTIONS, df, listboxData))
    btnReports.place(x = 420, y = 45, width=100, height=25)

    listboxData = tk.Listbox(mw)
    listboxData.grid(padx = 50, pady= 75)
    listboxData.config(width=65, height=20)

    btnSaveGraphs = tk.Button(text='Descargar gráfica', command=lambda: graphsObject.saveGraph(selectGraph, OPTIONS))
    btnSaveGraphs.place(x = 250, y = 520, width=130, height=35)
    
    mw.mainloop()