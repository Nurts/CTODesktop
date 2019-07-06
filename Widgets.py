import tkinter as tk
# Entry with placeholder
class PlaceholderEntry(tk.Entry):
    def foc_in(self, event):
        if self.get() == self.placeholder :
            self.configure(fg = 'black')
            self.delete(0, tk.END)

    def foc_out(self, event):
        if self.get() == '':
            self.configure(fg = 'gray25')
            self.insert(0, self.placeholder)

    def __init__(self, parent, placeholder, **kwargs):

        tk.Entry.__init__(self, parent, kwargs, fg = 'gray25')

        self.placeholder = placeholder
        
        self.insert(0, self.placeholder)
        self.bind("<FocusIn>", self.foc_in)
        self.bind('<FocusOut>', self.foc_out)
        

    def get_data(self):
        data = tk.Entry.get(self)
        if(data == self.placeholder):
            return ''
        else:
            return data

# Class for password Entry
class PasswordEntry(tk.Entry):
    def foc_in(self, event):
        if self.get() == self.placeholder :
            self.configure(show = '*', fg = 'black')
            self.delete(0, tk.END)

    def foc_out(self, event):
        if self.get() == '':
            self.configure(show = '', fg = 'gray25')
            self.insert(0, self.placeholder)

    def __init__(self, parent, placeholder, **kwargs):

        tk.Entry.__init__(self, parent, kwargs, fg = 'gray25')

        self.placeholder = placeholder

        self.insert(0, self.placeholder)
        self.bind("<FocusIn>", self.foc_in)
        self.bind('<FocusOut>', self.foc_out)
    
    def get_data(self):
        data = tk.Entry.get(self)
        if(data == self.placeholder):
            return ''
        else:
            return data

# Class for set of multiple addable widgets
class PlusEntryFrame(tk.Frame):
    def __init__(self, parent, entry_name,  widget_class, widget_params, **kwargs):
        tk.Frame.__init__(self, parent, kwargs)
        widget_params['parent'] = self
        
        self.entries  = []
        self.widget_class = widget_class
        self.widget_params = widget_params
        entry = widget_class(**widget_params)
        entry.pack(side = tk.TOP, pady = 5)
        self.entries.append(entry)

        self.addBtn = tk.Button(self, bg  = self['background'], fg = 'white', text = "+ Add another {}".format(entry_name), relief = tk.FLAT, command = self.add_entry )
        self.addBtn.pack(side = tk.BOTTOM)
    
    def add_entry(self):
        entry = self.widget_class(**self.widget_params)
        entry.pack(side = tk.TOP, pady = 5)
        self.entries.append(entry)

    def get_data(self): # only if widget class has method get_data
        data = []
        for entry in self.entries:
            data.append(entry.get_data())
        return data
