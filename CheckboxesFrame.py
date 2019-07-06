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
        
        self.elements = []

        for key in data.keys():

            label = tk.Label(self.interior, text = key, font = 'Helvetica 12 bold')
            label.pack(side = tk.TOP, fill = tk.X)
            
            self.elements.append(label)

            for section in data[key]:
                
                chbox = Widgets.Checkbox(section["name"], self.interior, on_img = check_image, off_img = cross_image, changeable = section["changeable"])
                chbox.pack(side = tk.TOP, fill = tk.X)
                self.elements.append(chbox)

        

        

