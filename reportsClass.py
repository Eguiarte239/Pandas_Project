from tkinter import END
from tkinter.ttk import *
import pandas as pd

class Reports():
    def __init__(self):
        pass

    def reportSelected(self, filter, OPTIONS, df, listbox):
        if filter.get() == OPTIONS[0]:
            self.firstReport(df, listbox)
    
        elif filter.get() == OPTIONS[1]:
            self.secondReport(df, listbox)

        elif filter.get() == OPTIONS[2]:
            self.thirdReport(df, listbox)
        
        elif filter.get() == OPTIONS[3]:
            self.fourthReport(df, listbox)
        
        elif filter.get() == OPTIONS[4]:
            self.fifthReport(df, listbox)
        
        elif filter.get() == OPTIONS[5]:
            self.sixthReport(df, listbox)
        
    def firstReport(self, df, listbox):
        listbox.delete(0,END)
        df['fecha'] = pd.date_range('11/22/2016', periods=1000, freq='D')
        mask = (df['fecha'] > '11/21/2017') & (df['fecha'] <= '11/21/2022')
        newDF = dict(df.loc[mask].value_counts(df['codigo_producto'])[:5])
        for key, value in newDF.items():
            listbox.insert(END, '--------------------------------------------------------')
            listbox.insert(END, ("Cantidad de productos vendidos: "+str(value)))

    def secondReport(self, df, listbox):
        listbox.delete(0,END)
        df['fecha'] = pd.date_range('8/21/2022', periods=1000, freq='D')
        mask = (df['fecha'] > '9/21/2022') & (df['fecha'] <= '11/21/2022')
        newDF = dict(df.loc[mask].value_counts(df['monto']))
        for key, value in newDF.items():
            listbox.insert(END, '--------------------------------------------------------')
            listbox.insert(END, ("Montos de pedidos: "+str(key)))
        
    def thirdReport(self, df, listbox):
        listbox.delete(0,END)
        df['fecha'] = pd.date_range('11/22/2016', periods=1000, freq='D')
        mask = (df['fecha'] > '11/21/2017') & (df['fecha'] <= '11/21/2022')
        newDF = dict(df.loc[mask].value_counts(df['codigo_cliente'])[:5])
        for key, value in newDF.items():
            listbox.insert(END, '-------------------------------------------------------------------------------')
            listbox.insert(END, ("Cliente que ha comprado el producto más vendido en cinco años: "+str(key)))
    
    def fourthReport(self, df, listbox):
        listbox.delete(0,END)
        df['fecha'] = pd.date_range('10/21/2022', periods=1000, freq='D')
        mask = (df['fecha'] > '10/21/2022') & (df['fecha'] <= '11/21/2022')
        newDF = dict(df.loc[mask].value_counts(df['codigo_empleado']))
        for key, value in newDF.items():
            listbox.insert(END, '--------------------------------------------------------')
            listbox.insert(END, ("Empleados con más ventas: "+str(key)))
    
    def fifthReport(self, df, listbox):
        listbox.delete(0,END)
        df['fecha'] = pd.date_range('1/1/2022', periods=1000, freq='D')
        mask = (df['fecha'] > '1/1/2022') & (df['fecha'] <= '11/21/2022')
        newDF = dict(df.loc[mask].value_counts(df['codigo_producto']))
        for key, value in newDF.items():
            listbox.insert(END, '--------------------------------------------------------')
            listbox.insert(END, ("Artículos más solicitados del primer semestre: "+str(key)))
    
    def sixthReport(self, df, listbox):
        listbox.delete(0,END)
        df['fecha'] = pd.date_range('1/1/2022', periods=1000, freq='D')
        mask = (df['fecha'] > '1/1/2022') & (df['fecha'] <= '11/21/2022')
        newDF = dict(df.loc[mask].value_counts(df['codigo_cliente']))
        for key, value in newDF.items():
            listbox.insert(END, '--------------------------------------------------------')
            listbox.insert(END, ("Clientes frecuentes del primer semestre: "+str(key)))