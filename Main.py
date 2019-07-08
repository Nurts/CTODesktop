import tkinter as tk
from ScrollFrame import ScrollFrame
from Widgets import Checkbox, Remarks
from CheckboxesFrame import Checkboxes

class MainApp():

    def __init__(self, window, title):
        self.window = window
        self.window.title(title)
        self.window.geometry("600x600")
        
        self.checkboxes = Checkboxes(self.window)
        self.checkboxes.pack(side = tk.TOP, fill = "both", expand = True, pady = 0)
        
        self.remarks = Remarks(self.window, "Замечания :")
        self.remarks.pack(side = tk.BOTTOM, fill = tk.X, expand = True, pady = 0)
        
app = MainApp(tk.Tk(), "CTO Demo")
app.window.mainloop()
