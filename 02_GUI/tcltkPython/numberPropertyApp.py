import tkinter as tk

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 != 0

def is_perfect(n):
    if n <= 1:
        return False
    sum_div = 1
    sqrt_n = int(n**0.5)
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            sum_div += i
            other = n // i
            if other != i:
                sum_div += other
    return sum_div == n

def is_armstrong(n):
    if n <= 0:
        return False
    num_str = str(n)
    length = len(num_str)
    sum_p = sum(int(d)**length for d in num_str)
    return sum_p == n

def calculate():
    num_str = entry.get()
    try:
        num = int(num_str)
    except ValueError:
        result_label.config(text="Please enter a valid integer")
        return

    results = []
    if var_prime.get():
        results.append(f"Prime: {is_prime(num)}")
    if var_even.get():
        results.append(f"Even: {is_even(num)}")
    if var_odd.get():
        results.append(f"Odd: {is_odd(num)}")
    if var_perfect.get():
        results.append(f"Perfect: {is_perfect(num)}")
    if var_armstrong.get():
        results.append(f"Armstrong: {is_armstrong(num)}")

    if not results:
        result_label.config(text="Select at least one check")
    else:
        result_label.config(text=", ".join(results))

# Create main window
root = tk.Tk()
root.title("Number Checker")

# Entry widget
entry = tk.Entry(root, width=30)
entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Checkboxes variables
var_prime = tk.BooleanVar()
var_even = tk.BooleanVar()
var_odd = tk.BooleanVar()
var_perfect = tk.BooleanVar()
var_armstrong = tk.BooleanVar()

# Checkboxes
tk.Checkbutton(root, text="Prime", variable=var_prime).grid(row=1, column=0, sticky='w')
tk.Checkbutton(root, text="Even", variable=var_even).grid(row=2, column=0, sticky='w')
tk.Checkbutton(root, text="Odd", variable=var_odd).grid(row=3, column=0, sticky='w')
tk.Checkbutton(root, text="Perfect Number", variable=var_perfect).grid(row=4, column=0, sticky='w')
tk.Checkbutton(root, text="Armstrong", variable=var_armstrong).grid(row=5, column=0, sticky='w')

# Button
tk.Button(root, text="Check", command=calculate).grid(row=6, column=0, columnspan=2, pady=10)

# Result label
result_label = tk.Label(root, text="")
result_label.grid(row=7, column=0, columnspan=2)

root.mainloop()



