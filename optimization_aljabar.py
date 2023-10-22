import tkinter as tk
from tkinter import Label
from pulp import *

result_window = None


# Fungsi untuk melakukan optimasi maksimum dan menampilkan hasilnya
def optimize_and_aljabar_max(a_values, c_values):
    global result_window
    problem = LpProblem("x", LpMaximize)

    x = [LpVariable(f"x{i+1}", lowBound=0) for i in range(len(c_values))]

    # Menentukan fungsi tujuan yang akan dimaksimalkan
    problem += lpSum([a_values[i] * x[i] for i in range(len(a_values))])

    # Menambahkan kendala ke dalam permasalahan
    for j, c_row in enumerate(c_values):
        problem += lpSum([c_row[j] * x[j] for j in range(len(c_row) - 1)]) <= c_row[-1]
        print(problem)  # Output: Deskripsi masalah optimasi (problem)

    # Menyelesaikan permasalahan
    problem.solve()

    # Mendapatkan nilai variabel x yang optimal dan nilai optimal dari fungsi tujuan (Z)
    x_optimal = [x[i].varValue for i in range(len(x))]
    z_optimal = value(problem.objective)

    # Menampilkan hasil optimasi ke jendela terpisah
    result_window = tk.Toplevel()
    result_window.title("Hasil Optimasi")

    result_label = Label(result_window, text="Hasil Optimasi:")
    result_label.pack()

    # Menampilkan nilai variabel x yang optimal
    for i, x_val in enumerate(x_optimal):
        if x_val is not None:
            result_label = Label(result_window, text=f"x{i+1} = {x_val}")
            result_label.pack()

    # Menampilkan nilai optimal dari fungsi tujuan (Z)
    result_label = Label(
        result_window, text=f"Nilai Optimal Fungsi Tujuan (Z) = {z_optimal}"
    )
    result_label.pack()


# Fungsi untuk melakukan optimasi minimum dan menampilkan hasilnya
def optimize_and_aljabar_min(a_values, c_values):
    global result_window
    problem = LpProblem("x", LpMinimize)

    x = [LpVariable(f"x{i+1}", lowBound=0) for i in range(len(c_values))]

    # Menentukan fungsi tujuan yang akan diminimalkan
    problem += lpSum([a_values[i] * x[i] for i in range(len(a_values))])

    # Menambahkan kendala ke dalam permasalahan
    for j, c_row in enumerate(c_values):
        problem += lpSum([c_row[j] * x[j] for j in range(len(c_row) - 1)]) >= c_row[-1]

    # Menyelesaikan permasalahan
    problem.solve()

    # Mendapatkan nilai variabel x yang optimal dan nilai optimal dari fungsi tujuan (Z)
    x_optimal = [x[i].varValue for i in range(len(x))]
    z_optimal = value(problem.objective)

    # Menampilkan hasil optimasi ke jendela terpisah
    result_window = tk.Toplevel()
    result_window.title("Hasil Optimasi")

    result_label = Label(result_window, text="Hasil Optimasi:")
    result_label.pack()

    # Menampilkan nilai variabel x yang optimal
    for i, x_val in enumerate(x_optimal):
        if x_val is not None:
            result_label = Label(result_window, text=f"x{i+1} = {x_val}")
            result_label.pack()

    # Menampilkan nilai optimal dari fungsi tujuan (Z)
    result_label = Label(
        result_window, text=f"Nilai Optimal Fungsi Tujuan (Z) = {z_optimal}"
    )
    result_label.pack()
