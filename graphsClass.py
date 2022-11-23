from tkinter import END
from tkinter.ttk import *
import pandas as pd
from matplotlib import pyplot as plt

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
        
        elif filter.get() == GRAPHS[4]:
            self.fifthGraph(GRAPHS, df, listbox)
        
        elif filter.get() == GRAPHS[5]:
            self.sixthGraph(GRAPHS, df, listbox)
        
    def firstGraph(self, GRAPHS, df, listbox):
        listbox.delete(0,END)
        df['fecha'] = pd.date_range('11/22/2016', periods=1000, freq='D')
        mask = (df['fecha'] > '11/21/2017') & (df['fecha'] <= '11/21/2022')
        newDF = dict(df.loc[mask].value_counts(df['codigo_producto'])[:5])
        x = range(len(newDF.keys()))
        fig, ax = plt.subplots()
        ax.bar(x, newDF.values())
        ax.set_xticks(x)
        _ = ax.set_xticklabels(newDF.keys())
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
        mask = (df['fecha'] > '9/21/2022') & (df['fecha'] <= '11/21/2022')
        newDF = dict(df.loc[mask].value_counts(df['monto']))
        x = range(len(newDF.keys()))
        fig, ax = plt.subplots()
        ax.bar(x, newDF.values())
        ax.set_xticks(x)
        _ = ax.set_xticklabels(newDF.keys())
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
        x = range(len(newDF.keys()))
        fig, ax = plt.subplots()
        ax.bar(x, newDF.values())
        ax.set_xticks(x)
        _ = ax.set_xticklabels(newDF.keys())
        plt.title(GRAPHS[3])
        plt.xlabel('Clients')
        plt.ylabel("Amount")
        plt.show()
        for key, value in newDF.items():
            listbox.insert(END, '--------------------------------------------------------')
            listbox.insert(END, ("Empleados con más ventas: "+str(key)))
    
    def fifthGraph(self, GRAPHS, df, listbox):
        listbox.delete(0,END)
        df['fecha'] = pd.date_range('1/1/2022', periods=1000, freq='D')
        mask = (df['fecha'] > '1/1/2022') & (df['fecha'] <= '11/21/2022')
        newDF = dict(df.loc[mask].value_counts(df['codigo_producto']))
        x = range(len(newDF.keys()))
        fig, ax = plt.subplots()
        ax.bar(x, newDF.values())
        ax.set_xticks(x)
        _ = ax.set_xticklabels(newDF.keys())
        plt.title(GRAPHS[4])
        plt.xlabel('Clients')
        plt.ylabel("Amount")
        plt.show()
        for key, value in newDF.items():
            listbox.insert(END, '--------------------------------------------------------')
            listbox.insert(END, ("Empleados con más ventas: "+str(key)))
    
    def sixthGraph(self, GRAPHS, df, listbox):
        listbox.delete(0,END)
        df['fecha'] = pd.date_range('1/1/2022', periods=1000, freq='D')
        mask = (df['fecha'] > '1/1/2022') & (df['fecha'] <= '11/21/2022')
        newDF = dict(df.loc[mask].value_counts(df['codigo_cliente']))
        x = range(len(newDF.keys()))
        fig, ax = plt.subplots()
        ax.bar(x, newDF.values())
        ax.set_xticks(x)
        _ = ax.set_xticklabels(newDF.keys())
        plt.title(GRAPHS[5])
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