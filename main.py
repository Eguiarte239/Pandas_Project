import tkinter as tk
from tkinter import END, ttk
from tkinter.ttk import *
import ctypes
import pandas as pd
from matplotlib import pyplot as plt

ctypes.windll.shcore.SetProcessDpiAwareness(True)

class Graphs():
    def __init__(self):
        pass

    def graphSelected(self, filter, GRAPHS, df, listbox):
        if filter.get() == GRAPHS[0]:
            self.firstGraph(GRAPHS, df, listbox)
    
        elif filter.get() == GRAPHS[1]:
            self.secondGraph(GRAPHS, df, listbox)

        elif filter.get() == GRAPHS[2]:
            self.thirdGraph(GRAPHS, df, listbox)
        
        elif filter.get() == GRAPHS[3]:
            self.fourthGraph(GRAPHS, df, listbox)
        
    def firstGraph(self, GRAPHS, df, listbox):
        listbox.delete(0,END)
        df['fecha'] = pd.date_range('11/22/2016', periods=1000, freq='D')
        mask = (df['fecha'] > '11/21/2017') & (df['fecha'] <= '11/21/2022')
        newDF = dict(df.loc[mask].value_counts(df['codigo_cliente'])[:5])
        print(newDF)
        plt.bar(newDF.keys(), newDF.values())
        plt.title(GRAPHS[0])
        plt.xlabel('Clients')
        plt.ylabel("Amount")
        plt.show()
        for key, value in newDF.items():
            listbox.insert(END, '--------------------------------------------------------')
            listbox.insert(END, ("Cantidad de productos vendidos: "+str(value)))

    def secondGraph(self, GRAPHS, df, listbox):
        listbox.delete(0,END)
        df['fecha'] = pd.date_range('8/21/2022', periods=1000, freq='D')
        mask = (df['fecha'] > '8/21/2022') & (df['fecha'] <= '11/21/2022')
        newDF = dict(df.loc[mask].value_counts(df['monto']))
        plt.bar(newDF.keys(), newDF.values())
        plt.title(GRAPHS[1])
        plt.xlabel('Clients')
        plt.ylabel("Amount")
        plt.show()
        for key, value in newDF.items():
            listbox.insert(END, '--------------------------------------------------------')
            listbox.insert(END, ("Montos de pedidos: "+str(key)))
        
    def thirdGraph(self, GRAPHS, df, listbox):
        listbox.delete(0,END)
        df['fecha'] = pd.date_range('11/22/2016', periods=1000, freq='D')
        mask = (df['fecha'] > '11/21/2017') & (df['fecha'] <= '11/21/2022')
        newDF = dict(df.loc[mask].value_counts(df['codigo_cliente'])[:5])
        for key, value in newDF.items():
            listbox.insert(END, '-------------------------------------------------------------------------------')
            listbox.insert(END, ("Cliente que ha comprado el producto más vendido en cinco años: "+str(key)))
    
    def fourthGraph(self, GRAPHS, df, listbox):
        listbox.delete(0,END)
        df['fecha'] = pd.date_range('10/21/2022', periods=1000, freq='D')
        mask = (df['fecha'] > '10/21/2022') & (df['fecha'] <= '11/21/2022')
        newDF = dict(df.loc[mask].value_counts(df['codigo_empleado']))
        plt.bar(newDF.keys(), newDF.values())
        plt.title(GRAPHS[3])
        plt.xlabel('Clients')
        plt.ylabel("Amount")
        plt.show()
        for key, value in newDF.items():
            listbox.insert(END, '--------------------------------------------------------')
            listbox.insert(END, ("Empleados con más ventas: "+str(key)))
    '''
    def saveGraph(self, filter, GRAPHS):
        for graph in GRAPHS:
            if filter.get() == graph:
                graphName = graph+'.png'
                imageName = graphName.replace(' ','_') 
                plt.savefig(imageName)'''

df = pd.read_csv('pedido.csv')

graphsObject = Graphs()

GRAPHS = ('Productos más vendidos (5 años)', 'Montos (3 meses)', 'Clientes-producto más vendido (5 años)', 'Empleados con más ventas (Último mes)')

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