import tkinter as tk
from tkinter import filedialog
import pandas as pd


class ExcelClass(): #Class to create tkinter GUI for simple importing of excel files.
    def __init__(self):
        
        self.data = None
        
        self.root = tk.Tk()
        canvas1 = tk.Canvas(self.root, width = 300, height = 300, bg = 'lightsteelblue')
        canvas1.pack()
        browseButton_Excel = tk.Button(text='Import Production Log',
                                       command=self.getExcel, bg='green',
                                       fg='white', font=('helvetica',
                                                         12,
                                                         'bold'))
        canvas1.create_window(150, 150, window=browseButton_Excel)
      
    def getExcel(self):
    
        import_file_path = filedialog.askopenfilename()
        self.data = pd.read_excel (import_file_path) #Create the pandadataframe from the excel file, store it in the class (self.data).
        
