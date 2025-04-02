# List box based Example 
# ToDoList
import tkinter as tk

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("TO DO List")
        self.root.geometry("300x200")

        self.createApp()

    def createApp(self):
        self.entry1 = tk.Entry(self.root)
        self.entry1.pack()

        tk.Button(self.root, text="Add", command=self.addItem).pack()
        tk.Button(self.root, text="Remove", command=self.removeItem).pack()

        self.listbox = tk.Listbox(self.root)
        self.listbox.pack()

    def addItem(self):
        if self.entry1.get() != '':
            self.listbox.insert(tk.END, self.entry1.get())
            self.entry1.delete(0, tk.END)

    def removeItem(self):
        self.listbox.delete(tk.ANCHOR)


# main code 
if __name__ == '__main__':
    root = tk.Tk()
    app = ToDoList(root)
    root.mainloop()