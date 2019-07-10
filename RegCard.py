import tkinter as tk
from Widgets import RawFrame, Radiobuttons, ButtonWithFocus

class RegCard(tk.Frame):
    
    def __init__(self, parent, **kwargs):

        tk.Frame.__init__(self, parent, kwargs)
        
        self.elements = []
        tk.Grid.columnconfigure(self, 0, weight=1)
        tk.Grid.columnconfigure(self, 1, weight=1)
        tk.Grid.columnconfigure(self, 2, weight=1)
        row1 = RawFrame(self, bg = self["background"])
        labels = ["Идент. номер VIN", "Марка, модель", "год"]
        width = [20, 30, 10]
        row1.add(labels, width)
        row1.grid(row = 1,  column = 1, sticky = "nsew")

        row2 = RawFrame(self)
        labels = ["№ двигателя", "№ кузова", "№ шасси"]
        width = [20, 20, 20]
        row2.add(labels, width)
        row2.grid(row = 2, column = 1, sticky = "nsew")

        row3 = RawFrame(self)
        labels = ["Собственник транспортного средства"]
        width = [60]
        row3.add(labels, width)
        row3.grid(row = 3, column = 1, sticky = "nsew")

        row4 = RawFrame(self)
        labels = ["Представитель собственника ТС"]
        width = [60]
        row4.add(labels, width)
        row4.grid(row = 4, column = 1, sticky = "nsew")

        row5 = RawFrame(self)
        labels = ["Паспорт: серия", "номер", "Blank"]
        width = [10, 20, 25]
        row5.add(labels, width)
        row5.grid(row = 5, column = 1, sticky = "nsew")

        row6 = RawFrame(self)
        labels = ["Рег. документ", "серия", "номер"]
        width = [40, 10, 20]
        row6.add(labels, width)
        row6.grid(row = 6, column = 1, sticky = "nsew")

        row7 = RawFrame(self)
        labels = ["Зарегистрирован в ГИБДД"]
        width = [60]
        row7.add(labels, width)
        row7.grid(row = 7, column = 1, sticky = "nsew")

        row8 = RawFrame(self)
        labels = ["ОСАГО: серия", "номер", "выдан"]
        width = [10, 10, 40]
        row8.add(labels, width)
        row8.grid(row = 8, column = 1, sticky = "nsew")

        row9 = RawFrame(self)
        labels = ["Дата выдачи", "Вид топлива", "Руль"]
        width = [20, 30, 15]
        row9.add(labels, width)
        row9.grid(row = 9, column = 1, sticky = "nsew")

        self.elements.append(row1)
        self.elements.append(row2)
        self.elements.append(row3)
        self.elements.append(row4)
        self.elements.append(row5)
        self.elements.append(row6)
        self.elements.append(row7)
        self.elements.append(row8)
        self.elements.append(row9)

        self.image_file = tk.PhotoImage(file = "./images/car_sign.png")
        self.image = tk.Label(self, image = self.image_file)
        self.image.grid(column = 2, row = 1, rowspan = 9, sticky = "nsew", padx = 100)

        self.main_info = RawFrame(self)
        labels = ["Гос. номер", "Время осмотра", "Blank"]
        width = [15, 15, 20]
        self.main_info.add(labels, width)
        self.main_info.grid(row = 0, column = 1, sticky = "nsew")

        self.inspection_radiobutton = Radiobuttons(self)
        labels = ["Первичная проверка", "Повторная проверка"]
        self.inspection_radiobutton.add(labels)
        self.inspection_radiobutton.grid(column = 2, row = 0, sticky = "nsew", padx = 100)

        # self.print_icon  = tk.PhotoImage(file = "./images/print50x50.png")
        # self.print_button = ButtonWithFocus(self, text = "Печать", image = self.print_icon, width = 50)
        # self.print_button.grid(row = 0, column = 0, rowspan = 2, sticky = "nsew", padx = 20)
        

        