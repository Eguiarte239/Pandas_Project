# Modules that will be used
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
import ctypes
import pandas as pd
import graphsClass
import reportsClass

if __name__ == '__main__':

    # This line will transform a tkinter window into an HD window
    ctypes.windll.shcore.SetProcessDpiAwareness(True)

    # Since we're working only with one file we can open it using pandas from here
    df = pd.read_csv('pedido.csv')

    # Create two different objects to generate different information when using the GUI
    graphsObject = graphsClass.Graphs()
    reportsObject = reportsClass.Reports()

    # Tuple to setup the options you'll be able to use in the GUI
    OPTIONS = ('Productos más vendidos', 'Montos', 'Clientes-producto más vendido', 'Empleados con más ventas', 'Productos más solicitados', 'Clientes frecuentes')

    # Setup the window parameters
    mw = tk.Tk()
    mw.title('Proyecto')
    mw.geometry("630x600") 
    mw.resizable(0, 0)

    # Combo box to see the available options to generate a graph
    selectGraph = ttk.Combobox(mw,value=OPTIONS, width=24)
    selectGraph.set('Gráficas')
    selectGraph.place(x = 60, y = 15)

    # Button to generate a graph based on an option selected. Will send the option selected, tuple and file to generate the correct graph
    btnGraphs = tk.Button(text='Gráficas', command= lambda: graphsObject.graphSelected(selectGraph, df))
    btnGraphs.place(x = 120, y = 45, width=100, height=25)

    # Combo box to see available options to generate a report inside a listbox
    selectReport = ttk.Combobox(mw,value=OPTIONS, width=24)
    selectReport.set('Reportes')
    selectReport.place(x = 378, y = 15)
    
    # Button to generate a report based on an option selected. Will send the option selected, tuple, listbox and file to generate the correct report inside listbox
    btnReports = tk.Button(text='Reportes', command= lambda: reportsObject.reportSelected(selectReport, df, listboxData))
    btnReports.place(x = 420, y = 45, width=100, height=25)

    # Listbox where reports will appear after being generated
    listboxData = tk.Listbox(mw)
    listboxData.grid(padx = 50, pady= 75)
    listboxData.config(width=65, height=20)

    # Button to save a generated graph as a PNG file. This will send the option selected and the tuple to name it correctly
    btnSaveGraphs = tk.Button(text='Descargar gráfica', command=lambda: graphsObject.saveGraph(selectGraph))
    btnSaveGraphs.place(x = 100, y = 520, width=130, height=35)

    # Button to save a generated graph as a PNG file. This will send the option selected and the tuple to name it correctly
    btnSaveReports = tk.Button(text='Descargar reporte', command=lambda: reportsObject.saveReport(selectReport, listboxData))
    btnSaveReports.place(x = 380, y = 520, width=130, height=35)
    
    # Loop to keep GUI alive
    mw.mainloop()