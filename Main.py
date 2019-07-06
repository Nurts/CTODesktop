import tkinter as tk
from ScrollFrame import ScrollFrame

class MainApp():

    def __init__(self, window, title):
        self.window = window
        self.window.title(title)
        

app = MainApp(tk.Tk(), "CTO Demo")
app.window.mainloop()
