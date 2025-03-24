# Addition of two number 


import tkinter as tk

class AplicationAdd:
    def __init__(self, root):
        self.root = root
        self.root.title("Addition")
        self.root.geometry("320x180")

        self.createApp()

    def createApp(self):
        tk.Label(self.root, text="Enter the First Number:").grid(row=0, column=0, padx=10)
        entr1 = tk.Entry(self.root)
        entr1.grid(row=0, column=1, padx=5)
        

        pass
    def addtion(self):
        pass

        

# main code 

root = tk.Tk()
app = AplicationAdd(root)

root.mainloop()