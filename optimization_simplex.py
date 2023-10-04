import tkinter as tk
from tkinter import Label, ttk
import numpy as np
from pulp import *
import scipy.optimize as opt

result_window = None
# Fungsi untuk melakukan optimasi maksimum dan menampilkan hasilnya
def optimize_and_simplex_max(a_values, c_values):
    global result_window 
    
    c_values = np.array(c_values)
    a_values = np.array(a_values)

    # Mendefinisikan batas kendala dalam bentuk tupel (lower_bound, upper_bound)
    bounds = tuple((0, None) for _ in range(len(a_values)))

    # Fungsi tujuan yang akan dimaksimalkan (-1 * fungsi tujuan karena linprog bekerja dengan minimum)
    obj_coefficients = -1 * a_values

    # Kendala dalam bentuk Ax <= b
    A = c_values[:, :-1]
    b = c_values[:, -1]

    # Melakukan optimasi menggunakan linprog
    result = opt.linprog(c=obj_coefficients, A_ub=A, b_ub=b, bounds=bounds, method="highs")

    # Mendapatkan hasil optimasi
    x_optimal = result.x
    z_optimal = -result.fun  # -result.fun karena linprog bekerja dengan minimum
    iterasi = result.nit  # Jumlah iterasi

    # Menampilkan hasil optimasi ke jendela terpisah
    display_optimization_result_max(x_optimal, z_optimal, iterasi)

# Fungsi untuk melakukan optimasi minimum dan menampilkan hasilnya
def optimize_and_simplex_min(a_values, c_values):
    global result_window 
    
    c_values = np.array(c_values)
    a_values = np.array(a_values)

    # Mendefinisikan batas kendala dalam bentuk tupel (lower_bound, upper_bound)
    bounds = tuple((0, None) for _ in range(len(a_values)))

    # Fungsi tujuan yang akan diminimalkan
    obj_coefficients = a_values

    # Kendala dalam bentuk Ax >= b
    A = -c_values[:, :-1]  # Perlu negatif karena linprog bekerja dengan <=
    b = -c_values[:, -1]    # Perlu negatif karena linprog bekerja dengan <=

    # Melakukan optimasi menggunakan linprog
    result = opt.linprog(c=obj_coefficients, A_ub=A, b_ub=b, bounds=bounds, method="highs")

    # Mendapatkan hasil optimasi
    x_optimal = result.x
    z_optimal = result.fun
    iterasi = result.nit  # Jumlah iterasi

    # Menampilkan hasil optimasi ke jendela terpisah
    display_optimization_result_min(x_optimal, z_optimal,iterasi)


# Fungsi untuk menampilkan hasil optimasi dalam jendela terpisah
def display_optimization_result_max(x_optimal, z_optimal,iterasi):
    global result_window 
    result_window = tk.Toplevel()
    result_window.title("Hasil Optimasi")
    
    result_label = Label(result_window, text="Hasil Optimasi:")
    result_label.pack()
    
    # Membuat tabel Treeview
    tree = ttk.Treeview(result_window, columns=("Variabel", "Nilai"))
    tree.heading("#1", text="Variabel")
    tree.heading("#2", text="Nilai")
    tree.pack()

    # Menambahkan hasil optimasi ke dalam tabel
    for i, x_val in enumerate(x_optimal):
        if x_val is not None:
            tree.insert("", "end", values=(f"x{i+1}", x_val))
    
    tree.insert("", "end", values=("Nilai Optimal Z", z_optimal))
    
    tree.insert("", "end", values=("Jumlah Iterasi", iterasi))


# Fungsi untuk menampilkan hasil optimasi dalam jendela terpisah
def display_optimization_result_min(x_optimal, z_optimal, iterasi):
    global result_window 
    result_window = tk.Toplevel()
    result_window.title("Hasil Optimasi")
    
    result_label = Label(result_window, text="Hasil Optimasi:")
    result_label.pack()
    
    # Membuat tabel Treeview
    tree = ttk.Treeview(result_window, columns=("Variabel", "Nilai"))
    tree.heading("#1", text="Variabel")
    tree.heading("#2", text="Nilai")
    tree.pack()

    # Menambahkan hasil optimasi ke dalam tabel
    for i, x_val in enumerate(x_optimal):
        if x_val is not None:
            tree.insert("", "end", values=(f"x{i+1}", x_val))
    
    tree.insert("", "end", values=("Nilai Optimal Z", z_optimal))
    
    tree.insert("", "end", values=("Jumlah Iterasi", iterasi))