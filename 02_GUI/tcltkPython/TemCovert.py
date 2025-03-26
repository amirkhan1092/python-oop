# # Temperature Converter 

# import tkinter as tk
# # from tkinter import *

# class TempConvert:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("300x200")
#         self.title("Temperature Converter")

#         self.createApp()

#     def createApp(self):
#         tk.Label(self.root, text=)




# if __name__ == '__main__':
#     # pass
#     root = tk.Tk()
#     app = TempConvert(root)


# import tkinter as tk
# from tkinter import ttk

# def celsius_to_fahrenheit():
#     try:
#         celsius = float(entry.get())
#         fahrenheit = (celsius * 9/5) + 32
#         result_label.config(text=f"{fahrenheit:.2f} °F")
#     except ValueError:
#         result_label.config(text="Invalid input")

# def fahrenheit_to_celsius():
#     try:
#         fahrenheit = float(entry.get())
#         celsius = (fahrenheit - 32) * 5/9
#         result_label.config(text=f"{celsius:.2f} °C")
#     except ValueError:
#         result_label.config(text="Invalid input")

# # Create main window
# root = tk.Tk()
# root.title("Temperature Converter")
# root.geometry("300x200")

# # Create widgets
# entry_label = tk.Label(root, text="Enter Temperature:")
# entry_label.pack(pady=5)

# entry = tk.Entry(root)
# entry.pack(pady=5)

# convert_to_f_button = ttk.Button(root, text="Convert to °F", command=celsius_to_fahrenheit)
# convert_to_f_button.pack(pady=5)

# convert_to_c_button = ttk.Button(root, text="Convert to °C", command=fahrenheit_to_celsius)
# convert_to_c_button.pack(pady=5)

# result_label = tk.Label(root, text="Result will be shown here", font=("Arial", 12, "bold"))
# result_label.pack(pady=10)

# # Run the application
# root.mainloop()



import tkinter as tk
from tkinter import ttk

def celsius_to_fahrenheit():
    try:
        celsius = float(celsius_entry.get())
        fahrenheit = (celsius * 9/5) + 32
        fahrenheit_entry.delete(0, tk.END)
        fahrenheit_entry.insert(0, f"{fahrenheit:.2f}")
    except ValueError:
        result_label.config(text="Invalid input")

def fahrenheit_to_celsius():
    try:
        fahrenheit = float(fahrenheit_entry.get())
        celsius = (fahrenheit - 32) * 5/9
        celsius_entry.delete(0, tk.END)
        celsius_entry.insert(0, f"{celsius:.2f}")
    except ValueError:
        result_label.config(text="Invalid input")

# Create main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("350x200")

# Create widgets
celsius_label = tk.Label(root, text="Celsius:")
celsius_label.grid(row=0, column=0, padx=10, pady=5)

celsius_entry = tk.Entry(root)
celsius_entry.grid(row=0, column=1, padx=10, pady=5)

fahrenheit_label = tk.Label(root, text="Fahrenheit:")
fahrenheit_label.grid(row=1, column=0, padx=10, pady=5)

fahrenheit_entry = tk.Entry(root)
fahrenheit_entry.grid(row=1, column=1, padx=10, pady=5)

convert_to_f_button = ttk.Button(root, text="Convert to °F", command=celsius_to_fahrenheit)
convert_to_f_button.grid(row=2, column=0, padx=10, pady=5)

convert_to_c_button = ttk.Button(root, text="Convert to °C", command=fahrenheit_to_celsius)
convert_to_c_button.grid(row=2, column=1, padx=10, pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
