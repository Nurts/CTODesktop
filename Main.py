import tkinter as tk
from ScrollFrame import ScrollFrame
from Widgets import Checkbox
from CheckboxesFrame import Checkboxes

class MainApp():

    def __init__(self, window, title):
        self.window = window
        self.window.title(title)
        self.window.geometry("600x600")
        self.checkboxes = Checkboxes(self.window)
        self.checkboxes.pack(side = tk.TOP, fill = "both", expand = True)

app = MainApp(tk.Tk(), "CTO Demo")
app.window.mainloop()
