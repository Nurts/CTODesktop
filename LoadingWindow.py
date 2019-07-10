import tkinter as tk

class LoadingWindow(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Пожалуйста подождите")
        self.label = tk.Label(self, text = "Подождите пока идет процесс распознавания ...", font = "Arial 20", fg = 'gray')
        self.label.pack(side = tk.BOTTOM, pady = 200, padx = 200)

        self.update()