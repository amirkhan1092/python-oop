# 

import tkinter as tk

class ItemListApp:
    def __init__(self, root):
        self.root = root
        self.root.title('List Items')
        self.createApp()
    def createApp(self):
        self.entry1 = tk.Entry(self.root)
        self.entry1.pack()
        tk.Button(self.root, text='Add', command=self.addItem).pack()
        tk.Button(self.root, text='Remove', command=self.removeItem).pack()
        self.list = tk.Listbox(self.root)
        self.list.pack()
    def addItem(self):
        pass
    def removeItem(self):
        pass
if __name__ == '__main__':
    root = tk.Tk()
    app = ItemListApp(root)
    root.mainloop()