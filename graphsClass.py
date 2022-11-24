# Modules that will be used
from tkinter.ttk import *
import pandas as pd
from matplotlib import pyplot as plt

# Define our class to generate all Graphs
class Graphs():
    def __init__(self):
        pass
    
    # Get the option selected and call the correct method to generate a graph
    def graphSelected(self, options, df):
        if options.current() == 0:
            self.firstGraph(options, df)
    
        elif options.current() == 1:
            self.secondGraph(options, df)

        elif options.current() == 2:
            self.thirdGraph(options, df)
        
        elif options.current() == 3:
            self.fourthGraph(options, df)
        
        elif options.current() == 4:
            self.fifthGraph(options, df)
        
        elif options.current() == 5:
            self.sixthGraph(options, df)
        
    # From now on it's pretty much the same for every method
    def firstGraph(self, options, df):
        # Define a date range to get info from that range
        df['fecha'] = pd.date_range('11/22/2017', periods=1000, freq='D')
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
        plt.title(options.get())
        plt.xlabel('Producto')
        plt.ylabel("Cantidad")
        plt.show()

    def secondGraph(self, options, df):
        df['fecha'] = pd.date_range('8/21/2022', periods=1000, freq='D')
        mask = (df['fecha'] > '9/21/2022') & (df['fecha'] <= '11/21/2022')
        newDF = dict(df.loc[mask].value_counts(df['monto']))
        x = range(len(newDF.values()))
        fig, ax = plt.subplots()
        ax.bar(x, newDF.keys())
        ax.set_xticks(x)
        _ = ax.set_xticklabels(newDF.values())
        plt.title(options.get())
        plt.show()
        
    def thirdGraph(self, options, df):
        df['fecha'] = pd.date_range('11/22/2016', periods=1000, freq='D')
        mask = (df['fecha'] > '11/21/2017') & (df['fecha'] <= '11/21/2022')
        newDF = dict(df.loc[mask].value_counts(df['codigo_cliente'])[:5])
        x = range(len(newDF.keys()))
        fig, ax = plt.subplots()
        ax.bar(x, newDF.values())
        ax.set_xticks(x)
        _ = ax.set_xticklabels(newDF.keys())
        plt.title(options.get())
        plt.xlabel('Clientes')
        plt.ylabel("Cantidad")
        plt.show()
    
    def fourthGraph(self, options, df):
        df['fecha'] = pd.date_range('10/21/2022', periods=1000, freq='D')
        mask = (df['fecha'] > '10/21/2022') & (df['fecha'] <= '11/21/2022')
        newDF = dict(df.loc[mask].value_counts(df['codigo_empleado']))
        x = range(len(newDF.keys()))
        fig, ax = plt.subplots()
        ax.bar(x, newDF.values())
        ax.set_xticks(x)
        _ = ax.set_xticklabels(newDF.keys())
        plt.title(options.get())
        plt.xlabel('Empleados')
        plt.ylabel("Ventas")
        plt.show()
    
    def fifthGraph(self, options, df):
        df['fecha'] = pd.date_range('1/1/2022', periods=1000, freq='D')
        mask = (df['fecha'] > '1/1/2022') & (df['fecha'] <= '6/21/2022')
        newDF = dict(df.loc[mask].value_counts(df['codigo_producto']))
        x = range(len(newDF.keys()))
        fig, ax = plt.subplots()
        ax.bar(x, newDF.values())
        ax.set_xticks(x)
        _ = ax.set_xticklabels(newDF.keys())
        plt.title(options.get())
        plt.xlabel('Artículos')
        plt.ylabel("Cantidad")
        plt.show()
    
    def sixthGraph(self, options, df):
        df['fecha'] = pd.date_range('1/1/2022', periods=1000, freq='D')
        mask = (df['fecha'] > '1/1/2022') & (df['fecha'] <= '6/21/2022')
        newDF = dict(df.loc[mask].value_counts(df['codigo_cliente']))
        x = range(len(newDF.keys()))
        fig, ax = plt.subplots()
        ax.bar(x, newDF.values())
        ax.set_xticks(x)
        _ = ax.set_xticklabels(newDF.keys())
        plt.title(options.get())
        plt.xlabel('Clientes')
        plt.ylabel("Compras")
        plt.show()

    # With this method you'll be able to donwload the graph in the same folder where you have the code
    def saveGraph(self, options):
        # Replace empty spaces with _ to create the name of the PNG file and save it
        graphName = options.get()+'.png'
        imageName = graphName.replace(' ','_') 
        plt.savefig(imageName)