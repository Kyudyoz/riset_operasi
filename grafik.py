# import tkinter as tk
# from tkinter import Label, Entry, Button
# import numpy as np
# import optimization

# def create_c_entries():
#     range_i = int(range_i_entry.get())
        
#     for i in range(range_i):
#         c_row = []
#         for j in range(3):
#             label_text = f"kendala:"
#             Label(window, text=label_text).grid(row=10, column=0)
#             entry = Entry(window)
#             entry.grid(row=10 + i, column=2 * j + 1)
#             c_row.append(entry)
#         c_entries.append(c_row)

# def optimize_and_plot_max():
#     a = float(a_entry.get())
#     b = float(b_entry.get())
#     c_values = []

        
#     for i in range(len(c_entries)):
#         c_row = []
#         for j in range(len(c_entries[i])):
#             entry = c_entries[i][j]
#             c_row.append(float(entry.get()))
#         c_values.append(c_row)

#     optimization.optimize_and_plot_max(a,b, c_values)
    
# def optimize_and_plot_min():
#     a = float(a_entry.get())
#     b = float(b_entry.get())
#     c_values = []

        
#     for i in range(len(c_entries)):
#         c_row = []
#         for j in range(len(c_entries[i])):
#             entry = c_entries[i][j]
#             c_row.append(float(entry.get()))
#         c_values.append(c_row)

#     optimization.optimize_and_plot_min(a,b, c_values)

# window = tk.Tk()
# window.title("Optimasi Grafik")

# Label(window, text="x1:").grid(row=2, column=0)
# a_entry = Entry(window)
# a_entry.grid(row=2, column=1)

# Label(window, text="x2:").grid(row=3, column=0)
# b_entry = Entry(window)
# b_entry.grid(row=3, column=1)



# Label(window, text="Banyak Kendala:").grid(row=0, column=0)
# range_i_entry = Entry(window)
# range_i_entry.grid(row=0, column=1)

# c_entries = []

# create_c_button = Button(window, text="Buat Kolom Kendala", command=create_c_entries)
# create_c_button.grid(row=0, column=4)

# optimize_button = Button(window, text="Optimasi Maksimum", command=optimize_and_plot_max)
# optimize_button.grid(row=100, column=4)
# optimize_button = Button(window, text="Optimasi Minimum", command=optimize_and_plot_min)
# optimize_button.grid(row=100, column=5)

# window.mainloop()

import tkinter as tk
from tkinter import Label, Entry, Button, Toplevel
import numpy as np
import optimization_grafik

def create_c_entries():
    range_i = int(range_i_entry.get())
    range_j = int(range_j_entry.get())
    

    for i in range(range_i):
        c_row = []
        for j in range(range_j+1):
            label_text = f"kendala:"
            Label(second_window, text=label_text).grid(row=10, column=0)
            entry = Entry(second_window)
            entry.grid(row=10 + i, column=2 * j + 1)
            c_row.append(entry)
        c_entries.append(c_row)

def create_a_entries():
    range_j = int(range_j_entry.get())
    a_values.clear()  # Bersihkan list a_values sebelumnya

    for j in range(range_j):
        label_text = f"x{j+1}:"
        Label(second_window, text=label_text).grid(row=2 + j, column=0)
        entry = Entry(second_window)
        entry.grid(row=2 + j, column=1)
        a_values.append(entry)

def open_second_window():
    global second_window
    second_window = Toplevel(window)
    second_window.title("Optimasi RO")

    create_a_entries()  # Buat entri a_values sesuai dengan range_j
    create_c_entries()  # Buat entri kendala sesuai dengan range_i

    optimize_button = Button(second_window, text="Optimasi Maksimum", command=optimize_and_plot_max)
    optimize_button.grid(row=15 + len(a_values), column=4)
    optimize_button = Button(second_window, text="Optimasi Minimum", command=optimize_and_plot_min)
    optimize_button.grid(row=17 + len(a_values), column=4)

def optimize_and_plot_max():
    a_values_list = [float(entry.get()) for entry in a_values]
    c_values = []

    for i in range(len(c_entries)):
        c_row = []
        for j in range(len(c_entries[i])):
            entry = c_entries[i][j]
            c_row.append(float(entry.get()))
        c_values.append(c_row)

    optimization_grafik.optimize_and_plot_max(a_values_list, c_values)

def optimize_and_plot_min():
    a_values_list = [float(entry.get()) for entry in a_values]
    c_values = []

    for i in range(len(c_entries)):
        c_row = []
        for j in range(len(c_entries[i])):
            entry = c_entries[i][j]
            c_row.append(float(entry.get()))
        c_values.append(c_row)

    optimization_grafik.optimize_and_plot_min(a_values_list, c_values)

window = tk.Tk()
window.title("Optimasi RO")

Label(window, text="Banyak Variabel:").grid(row=2, column=0)
range_j_entry = Entry(window)
range_j_entry.grid(row=2, column=1)

Label(window, text="Banyak Kendala:").grid(row=3, column=0)
range_i_entry = Entry(window)
range_i_entry.grid(row=3, column=1)

a_values = []  # Menyimpan entri untuk a_values
c_entries = []

create_c_button = Button(window, text="Buat Kolom Kendala", command=open_second_window)
create_c_button.grid(row=3, column=4)

window.mainloop()

