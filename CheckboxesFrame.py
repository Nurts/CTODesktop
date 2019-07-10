import tkinter as tk
from VerticalScrolledFrame import VerticalScrolledFrame
import Widgets
import json

class Checkboxes(VerticalScrolledFrame):

    def __init__(self, parent):
        VerticalScrolledFrame.__init__(self, parent)

        check_image = tk.PhotoImage(file = "./images/small_checked.png")
        cross_image = tk.PhotoImage(file = "./images/small_crossed.png")

        data = None
        with open('CheckboxData.json',  encoding='utf-8') as f:
            data = json.load(f)
        
        total_amt = 0
        for key in data.keys():
            total_amt += len(data[key]) + 1; 

        max_rows = (total_amt // 3) +  (total_amt % 3 > 0)

        self.elements = []
        chbox_index = 0
        elem_index = 0
        tk.Grid.columnconfigure(self.interior, 0, weight=1)
        tk.Grid.columnconfigure(self.interior, 1, weight=1)
        tk.Grid.columnconfigure(self.interior, 2, weight=1)
        for key in data.keys():
            
            label = tk.Label(self.interior, text = key, font = 'Helvetica 12 bold', relief = tk.GROOVE)
            label.grid(row = elem_index % max_rows, column = elem_index // max_rows, sticky = "nsew")
            
            self.elements.append(label)
            elem_index += 1

            for section in data[key]:
                chbox_index += 1
                
                chbox = Widgets.Checkbox("{}. {}".format(chbox_index, section["name"]), self.interior, on_img = check_image, off_img = cross_image, changeable = section["changeable"])
                chbox.grid(row = elem_index % max_rows, column = elem_index // max_rows, sticky = "nsew")
                self.elements.append(chbox)
                elem_index += 1

        

        

