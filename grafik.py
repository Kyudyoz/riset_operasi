import tkinter as tk
from tkinter import Label, Entry, Button
import optimization_grafik


# Fungsi untuk membuat entri untuk kolom kendala (c)
def create_c_entries():
    range_i = int(range_i_entry.get())  # Input: Jumlah kendala (range_i)

    for i in range(range_i):
        c_row = []
        for j in range(3):
            label_text = f"kendala:"
            Label(window, text=label_text).grid(row=10, column=0)
            entry = Entry(window)
            entry.grid(row=10 + i, column=2 * j + 1)
            c_row.append(entry)
        c_entries.append(c_row)  # Output: Matriks koefisien kendala (c_entries)


# Fungsi untuk melakukan optimasi maksimum dan menampilkan grafiknya
def optimize_and_plot_max():
    a = float(a_entry.get())  # Input: Koefisien variabel x1 (a)
    b = float(b_entry.get())  # Input: Koefisien variabel x2 (b)
    c_values = []

    for i in range(len(c_entries)):
        c_row = []
        for j in range(len(c_entries[i])):
            entry = c_entries[i][j]
            c_row.append(float(entry.get()))
        c_values.append(c_row)  # Input: Matriks koefisien kendala (c_values)

    optimization_grafik.optimize_and_plot_max(a, b, c_values)


# Fungsi untuk melakukan optimasi minimum dan menampilkan grafiknya
def optimize_and_plot_min():
    a = float(a_entry.get())  # Input: Koefisien variabel x1 (a)
    b = float(b_entry.get())  # Input: Koefisien variabel x2 (b)
    c_values = []

    for i in range(len(c_entries)):
        c_row = []
        for j in range(len(c_entries[i])):
            entry = c_entries[i][j]
            c_row.append(float(entry.get()))
        c_values.append(c_row)  # Input: Matriks koefisien kendala (c_values)

    optimization_grafik.optimize_and_plot_min(a, b, c_values)


window = tk.Tk()
window.title("Optimasi Grafik")

Label(window, text="x1:").grid(row=2, column=0)
a_entry = Entry(window)
a_entry.grid(row=2, column=1)

Label(window, text="x2:").grid(row=3, column=0)
b_entry = Entry(window)
b_entry.grid(row=3, column=1)

Label(window, text="Banyak Kendala:").grid(row=0, column=0)
range_i_entry = Entry(window)
range_i_entry.grid(row=0, column=1)

c_entries = []  # Daftar daftar entri untuk kendala (c_entries)

create_c_button = Button(window, text="Buat Kolom Kendala", command=create_c_entries)
create_c_button.grid(row=0, column=4)

optimize_button = Button(
    window, text="Optimasi Maksimum", command=optimize_and_plot_max
)
optimize_button.grid(row=100, column=4)
optimize_button = Button(window, text="Optimasi Minimum", command=optimize_and_plot_min)
optimize_button.grid(row=100, column=5)

window.mainloop()
