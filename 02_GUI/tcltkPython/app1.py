
# Button Toggle 


import tkinter as tk
class CreateApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Toggle Button")
        self.root.geometry("300x200")
        self.app()

    def app(self):
        self.bt = tk.Button(self.root, text="TRUE", command=self.action)
        self.bt.pack(pady=10)
    def action(self):
        if self.bt['text'] == "TRUE":
            self.bt.config(text="FALSE", bg="RED", fg="BLACK")
        else:
            self.bt.config(text="TRUE", bg="GREEN", fg="BLACK")   

# main Code 
if __name__ == '__main__':
    root = tk.Tk()
    app = CreateApp(root)
    root.mainloop()