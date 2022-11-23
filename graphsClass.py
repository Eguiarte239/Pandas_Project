# Modules that will be used
from tkinter import END
from tkinter.ttk import *
import pandas as pd
from matplotlib import pyplot as plt

# Define our class to generate all Graphs
class Graphs():
    def __init__(self):
        pass
    
    # Get the option selected anc compare it to the tuple to call the correct method and then generate a graph
    def graphSelected(self, filter, GRAPHS, df):
        if filter.get() == GRAPHS[0]:
            self.firstGraph(GRAPHS, df)
    
        elif filter.get() == GRAPHS[1]:
            self.secondGraph(GRAPHS, df)

        elif filter.get() == GRAPHS[2]:
            self.thirdGraph(GRAPHS, df)
        
        elif filter.get() == GRAPHS[3]:
            self.fourthGraph(GRAPHS, df)
        
        elif filter.get() == GRAPHS[4]:
            self.fifthGraph(GRAPHS, df)
        
        elif filter.get() == GRAPHS[5]:
            self.sixthGraph(GRAPHS, df)
        
    # From now on it's pretty much the same for every method
    def firstGraph(self, GRAPHS, df):
        # Define a date range to get info from that range
        df['fecha'] = pd.date_range('11/22/2016', periods=1000, freq='D')
        mask = (df['fecha'] > '11/21/2017') & (df['fecha'] <= '11/21/2022')
        # Get certain info that appears the most in that range, convert that info into a dict to manipulate it in a better way
        newDF = dict(df.loc[mask].value_counts(df['codigo_producto'])[:5])
        # The next five rows are for generate a correct graph (no empty values in the X axis)
        x = range(len(newDF.keys()))
        fig, ax = plt.subplots()
        # This row in specific is to setup the info that will be shown in the X axis and Y axis
        ax.bar(x, newDF.values())
        ax.set_xticks(x)
        _ = ax.set_xticklabels(newDF.keys())
        # Set the graph name based on the option selected. Give the X axis and Y axis a label and show the graph in a new window
        plt.title(GRAPHS[0])
        plt.xlabel('Producto')
        plt.ylabel("Cantidad")
        plt.show()

    def secondGraph(self, GRAPHS, df):
        df['fecha'] = pd.date_range('8/21/2022', periods=1000, freq='D')
        mask = (df['fecha'] > '9/21/2022') & (df['fecha'] <= '11/21/2022')
        newDF = dict(df.loc[mask].value_counts(df['monto']))
        x = range(len(newDF.values()))
        fig, ax = plt.subplots()
        ax.bar(x, newDF.keys())
        ax.set_xticks(x)
        _ = ax.set_xticklabels(newDF.values())
        plt.title(GRAPHS[1])
        plt.xlabel('Montos de los pedidos')
        plt.show()
        
    def thirdGraph(self, GRAPHS, df):
        df['fecha'] = pd.date_range('11/22/2016', periods=1000, freq='D')
        mask = (df['fecha'] > '11/21/2017') & (df['fecha'] <= '11/21/2022')
        newDF = dict(df.loc[mask].value_counts(df['codigo_cliente'])[:5])
        x = range(len(newDF.keys()))
        fig, ax = plt.subplots()
        ax.bar(x, newDF.values())
        ax.set_xticks(x)
        _ = ax.set_xticklabels(newDF.keys())
        plt.title(GRAPHS[2])
        plt.xlabel('Clientes')
        plt.ylabel("Cantidad")
        plt.show()
    
    def fourthGraph(self, GRAPHS, df):
        df['fecha'] = pd.date_range('10/21/2022', periods=1000, freq='D')
        mask = (df['fecha'] > '10/21/2022') & (df['fecha'] <= '11/21/2022')
        newDF = dict(df.loc[mask].value_counts(df['codigo_empleado']))
        x = range(len(newDF.keys()))
        fig, ax = plt.subplots()
        ax.bar(x, newDF.values())
        ax.set_xticks(x)
        _ = ax.set_xticklabels(newDF.keys())
        plt.title(GRAPHS[3])
        plt.xlabel('Empleados')
        plt.ylabel("Ventas")
        plt.show()
    
    def fifthGraph(self, GRAPHS, df):
        df['fecha'] = pd.date_range('1/1/2022', periods=1000, freq='D')
        mask = (df['fecha'] > '1/1/2022') & (df['fecha'] <= '11/21/2022')
        newDF = dict(df.loc[mask].value_counts(df['codigo_producto']))
        x = range(len(newDF.keys()))
        fig, ax = plt.subplots()
        ax.bar(x, newDF.values())
        ax.set_xticks(x)
        _ = ax.set_xticklabels(newDF.keys())
        plt.title(GRAPHS[4])
        plt.xlabel('Artículos')
        plt.ylabel("Cantidad")
        plt.show()
    
    def sixthGraph(self, GRAPHS, df):
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
        plt.ylabel("Compras")
        plt.show()

    # With this method you'll be able to donwload the graph in the same folder where you have the code
    def saveGraph(self, filter, GRAPHS):
        # See through the options to get a match
        for graph in GRAPHS:
            if filter.get() == graph:
                # Replace empty spaces with _ to create the name of the PNG file and save it
                graphName = graph+'.png'
                imageName = graphName.replace(' ','_') 
                plt.savefig(imageName)