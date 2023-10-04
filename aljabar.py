import tkinter as tk
from tkinter import Label, Entry, Button, Toplevel
import optimization_aljabar

# Fungsi untuk membuat entri untuk kolom kendala (c)
def create_c_entries():
    range_i = int(range_i_entry.get())
    range_j = int(range_j_entry.get())

    # Iterasi untuk membuat entri untuk setiap kendala (c_ij)
    for i in range(range_i):
        c_row = []
        for j in range(range_j+1):
            label_text = f"kendala:"
            Label(second_window, text=label_text).grid(row=10, column=0)
            entry = Entry(second_window)
            entry.grid(row=10 + i, column=2 * j + 1)
            c_row.append(entry)
        c_entries.append(c_row)

# Fungsi untuk membuat entri untuk variabel (a)
def create_a_entries():
    range_j = int(range_j_entry.get())
    a_values.clear()  # Bersihkan list a_values sebelumnya

    # Iterasi untuk membuat entri untuk setiap variabel (x_j)
    for j in range(range_j):
        label_text = f"x{j+1}:"
        Label(second_window, text=label_text).grid(row=2 + j, column=0)
        entry = Entry(second_window)
        entry.grid(row=2 + j, column=1)
        a_values.append(entry)

# Fungsi untuk membuka jendela kedua
def open_second_window():
    global second_window
    second_window = Toplevel(window)
    second_window.title("Optimasi RO")

    create_a_entries()  # Panggil fungsi untuk membuat entri variabel (a)
    create_c_entries()  # Panggil fungsi untuk membuat entri kendala (c)

    # Buat tombol untuk optimasi maksimum dan minimum
    optimize_button = Button(second_window, text="Optimasi Maksimum", command=optimize_and_aljabar_max)
    optimize_button.grid(row=2, column=4+len(a_values))
    optimize_button = Button(second_window, text="Optimasi Minimum", command=optimize_and_aljabar_min)
    optimize_button.grid(row=3, column=4+len(a_values))

# Fungsi untuk melakukan optimasi maksimum dan menampilkan aljabarnya
def optimize_and_aljabar_max():
    a_values_list = [float(entry.get()) for entry in a_values]
    c_values = []

    # Mendapatkan nilai-nilai dari entri kendala (c_ij)
    for i in range(len(c_entries)):
        c_row = []
        for j in range(len(c_entries[i])):
            entry = c_entries[i][j]
            c_row.append(float(entry.get()))
        c_values.append(c_row)

    optimization_aljabar.optimize_and_aljabar_max(a_values_list, c_values)

# Fungsi untuk melakukan optimasi minimum dan menampilkan aljabarnya
def optimize_and_aljabar_min():
    a_values_list = [float(entry.get()) for entry in a_values]
    c_values = []

    # Mendapatkan nilai-nilai dari entri kendala (c_ij)
    for i in range(len(c_entries)):
        c_row = []
        for j in range(len(c_entries[i])):
            entry = c_entries[i][j]
            c_row.append(float(entry.get()))
        c_values.append(c_row)

    optimization_aljabar.optimize_and_aljabar_min(a_values_list, c_values)

# Inisialisasi jendela utama (GUI)
window = tk.Tk()
window.title("Optimasi RO")

# Membuat label dan entri untuk memasukkan jumlah variabel (a) dan kendala (c)
Label(window, text="Banyak Variabel:").grid(row=2, column=0)
range_j_entry = Entry(window)
range_j_entry.grid(row=2, column=1)

Label(window, text="Banyak Kendala:").grid(row=3, column=0)
range_i_entry = Entry(window)
range_i_entry.grid(row=3, column=1)

a_values = []  # Daftar entri untuk variabel (a)
c_entries = []  # Daftar daftar entri untuk kendala (c)

create_c_button = Button(window, text="Submit", command=open_second_window)
create_c_button.grid(row=100, column=1)

# Memulai loop utama untuk menampilkan GUI
window.mainloop()
