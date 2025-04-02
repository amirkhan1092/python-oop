

# import tkinter as tk 


# class Demo:
#     def __init__(self, root):
#         self.root = root
#         self.varStatus = tk.BooleanVar()
#         # self.varStatus.set(True)
#         self.createApp()

#     def createApp(self):
#         tk.Checkbutton(self.root, variable=self.varStatus).pack()
#         tk.Button(self.root, text="Get Status", command=self.action).pack()
#     def action(self):
#         print(self.varStatus.get())



# root = tk.Tk()
# Demo(root)
# root.mainloop()


import tkinter as tk 

root = tk.Tk() 
my_listbox = tk.Listbox(root) 
my_listbox.insert(1, "Red") 
my_listbox.insert(2, "Green") 
my_listbox.insert(3, "Blue") 
my_listbox.pack() 

selected_item = my_listbox.curselection() 
print(selected_item) 
root.mainloop() 
