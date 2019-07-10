import tkinter as tk
from ScrollFrame import ScrollFrame
from Widgets import Checkbox, Remarks, ButtonWithFocus
from CheckboxesFrame import Checkboxes
from RegCard import RegCard
from LoadingWindow import LoadingWindow
import time

class MainApp():

    def __init__(self, window, title):
        self.window = window
        self.window.title(title)
        self.window.geometry("1200x700")
        self.window.minsize(1200, 700)
        self.window.state('zoomed')

        self.reg_card = RegCard(self.window)
        self.reg_card.pack(side = tk.TOP, fill =  tk.Y, expand = False, pady = 0)

        self.checkboxes = Checkboxes(self.window)
        self.checkboxes.pack(side = tk.TOP, fill = "both", expand = True, pady = 0)
        
        self.detect_plate_btn  = ButtonWithFocus(self.window, text = "Начать определение номера", command = self.analyze)
        self.detect_plate_btn.pack(side = tk.LEFT, fill = "both", expand = True)

        self.two_btns = tk.Frame(self.window)
        self.two_btns.pack(side = tk.RIGHT, fill = "both", expand = True)

        self.send_btn  = ButtonWithFocus(self.two_btns, text = "Отправить")
        self.send_btn.pack(side = tk.RIGHT, fill = "both", expand = True)

        self.print_icon  = tk.PhotoImage(file = "./images/print50x50.png")
        self.print_button = ButtonWithFocus(self.two_btns, text = "Печать", image = self.print_icon, width = 50)
        self.print_button.pack(side = tk.LEFT, fill = tk.Y, expand = False)

        self.remarks = Remarks(self.window, "Замечания :")
        self.remarks.pack(side = tk.BOTTOM, fill = tk.X, expand = False, pady = 10, padx = 10)

        
    
    def analyze(self):
        self.window.grab_set()
        splash = LoadingWindow(self.window)

        time.sleep(5)
        splash.destroy()

        self.window.grab_release()




app = MainApp(tk.Tk(), "CTO Demo")
app.window.mainloop()
