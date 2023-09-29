# import matplotlib.pyplot as plt
# import numpy as np
# from pulp import *

# def optimize_and_plot_max(a,b, c_values):
#     problem = LpProblem("Kue", LpMaximize)

#     x = [LpVariable(f"Kue{i+1}", lowBound=0) for i in range(len(c_values))]

#     problem += a * x[0] + b * x[1]

#     # for i, a_row in enumerate(a_values):
#     #     problem += sum(a_row[j] * x[j] for j in range(len(a_row) - 1))
    
#     for i, c_row in enumerate(c_values):
#         problem += sum(c_row[j] * x[j] for j in range(len(c_row) - 1)) <= c_row[-1]

#     problem.solve()

#     x_optimal = [x[i].varValue for i in range(len(x))]
#     z_optimal = value(problem.objective)

#     # Plot constraints
#     x_values = np.linspace(0, 100, 100)

#     plt.figure(figsize=(8, 6))

#     for i, c_row in enumerate(c_values):
#         y_values = (c_row[-1] - c_row[0] * x_values) / c_row[1]
#         plt.plot(x_values, y_values, label="{}x1 + {}x2 <= {}".format(c_row[0], c_row[1], c_row[2]))

#     # Plot optimal solution point
#     plt.scatter(x_optimal[0], x_optimal[1], color='red', marker='o',
#                 label='Optimal Solution (x1={}, x2={}, z={})'.format(x_optimal[0], x_optimal[1], z_optimal))

#     plt.xlabel("x1")
#     plt.ylabel("x2")
#     plt.xlim(0, 100)
#     plt.ylim(0, 100)

#     plt.legend()
#     plt.title("Optimasi Maksimum")
#     plt.grid(True)
#     plt.show()

# def optimize_and_plot_min(a,b, c_values):
#     problem = LpProblem("Kue", LpMinimize)

#     x = [LpVariable(f"Kue{i+1}", lowBound=0) for i in range(len(c_values))]

#     problem += a * x[0] + b * x[1]

#     # for i, a_row in enumerate(a_values):
#     #     problem += sum(a_row[j] * x[j] for j in range(len(a_row) - 1))
    
#     for i, c_row in enumerate(c_values):
#         problem += sum(c_row[j] * x[j] for j in range(len(c_row) - 1)) >= c_row[-1]

#     problem.solve()

#     x_optimal = [x[i].varValue for i in range(len(x))]
#     z_optimal = value(problem.objective)

#     # Plot constraints
#     x_values = np.linspace(0, 100, 100)

#     plt.figure(figsize=(8, 6))

#     for i, c_row in enumerate(c_values):
#         y_values = (c_row[-1] - c_row[0] * x_values) / c_row[1]
#         plt.plot(x_values, y_values, label="{}x1 + {}x2 >= {}".format(c_row[0], c_row[1], c_row[2]))

#     # Plot optimal solution point
#     plt.scatter(x_optimal[0], x_optimal[1], color='red', marker='o',
#                 label='Optimal Solution (x1={}, x2={}, z={})'.format(x_optimal[0], x_optimal[1], z_optimal))

#     plt.xlabel("x1")
#     plt.ylabel("x2")
#     plt.xlim(0, 100)
#     plt.ylim(0, 100)

#     plt.legend()
#     plt.title("Optimasi Minimum")
#     plt.grid(True)
#     plt.show()



# import tkinter as tk
# from tkinter import Label, Button, messagebox
# import matplotlib.pyplot as plt
# import numpy as np
# from pulp import *


# def optimize_and_plot_max(a_values, c_values):
#     problem = LpProblem("Optimasi", LpMaximize)

#     x = [LpVariable(f"Optimasi{i+1}", lowBound=0) for i in range(len(c_values))]

#     # Menggunakan a_values sesuai dengan panjangnya
#     problem += lpSum([a_values[i] * x[i] for i in range(len(a_values))])

#     for i, c_row in enumerate(c_values):
#         problem += lpSum([c_row[j] * x[j] for j in range(len(c_row) - 1)]) <= c_row[-1]

#     problem.solve()
    
#     x_optimal = [x[i].varValue for i in range(len(x))]
#     z_optimal = value(problem.objective)

#     print("Hasil Optimasi (Maksimum):")
#     print("Nilai Optimal x:")
    
#     # display_optimization_result(x_optimal, z_optimal, c_values)
    
#     x_values = np.linspace(0, 100, 100)

#     plt.figure(figsize=(8, 6))

#     for i, c_row in enumerate(c_values):
#         a = c_row[0]
#         b = c_row[1]
#         c = c_row[2]
#         y_values = (c - a * x_values) / b
#         plt.plot(x_values, y_values, label="{}x1 + {}x2 <= {}".format(a, b, c))

#     plt.scatter(x_optimal[0], x_optimal[1], color='red', marker='o',
#                 label='Optimal Solution (x1={}, x2={}, z={})'.format(x_optimal[0], x_optimal[1], z_optimal))

#     plt.xlabel("x1")
#     plt.ylabel("x2")
#     plt.xlim(0, 100)
#     plt.ylim(0, 100)

#     plt.legend()
#     plt.title("Optimasi (Maksimum)")
#     plt.grid(True)
#     plt.show()
    
# def optimize_and_plot_min(a_values, c_values):
#     problem = LpProblem("Kue", LpMinimize)

#     x = [LpVariable(f"Kue{i+1}", lowBound=0) for i in range(len(c_values))]

#     # Menggunakan a_values sesuai dengan panjangnya
#     problem += lpSum([a_values[i] * x[i] for i in range(len(a_values))])

#     for i, c_row in enumerate(c_values):
#         problem += lpSum([c_row[j] * x[j] for j in range(len(c_row) - 1)]) >= c_row[-1]

#     problem.solve()

#     x_optimal = [x[i].varValue for i in range(len(x))]
#     z_optimal = value(problem.objective)

#     x_values = np.linspace(0, 100, 100)

#     plt.figure(figsize=(8, 6))

#     for i, c_row in enumerate(c_values):
#         y_values = (c_row[-1] - sum(c_row[j] * x_values for j in range(len(c_row) - 1))) / c_row[-1]
#         plt.plot(x_values, y_values, label="{}x1 + {}x2 >= {}".format(c_row[0], c_row[1], c_row[2]))

#     plt.scatter(x_optimal[0], x_optimal[1], color='red', marker='o',
#                 label='Optimal Solution (x1={}, x2={}, z={})'.format(x_optimal[0], x_optimal[1], z_optimal))

#     plt.xlabel("x1")
#     plt.ylabel("x2")
#     plt.xlim(0, 100)
#     plt.ylim(0, 100)

#     plt.legend()
#     plt.title("Optimasi (Minimum)")
#     plt.grid(True)
#     plt.show()


import tkinter as tk
from tkinter import Label, Button, ttk
import matplotlib.pyplot as plt
import numpy as np
from pulp import *

result_window = None

# Fungsi untuk menampilkan hasil optimasi dalam jendela terpisah
def display_optimization_result_max(x_optimal, z_optimal, c_values, a_values):
    global result_window 
    result_window = tk.Toplevel()
    result_window.title("Hasil Optimasi")
    
    result_label = Label(result_window, text="Hasil Optimasi:")
    result_label.pack()

    # # Menampilkan nilai variabel x yang optimal
    # for i, x_val in enumerate(x_optimal):
    #     if x_val is not None:
    #         result_label = Label(result_window, text=f"x{i+1} = {x_val}")
    #         result_label.pack()
    
    # # Menampilkan nilai optimal dari fungsi tujuan (Z)
    # result_label = Label(result_window, text=f"Nilai Optimal Fungsi Tujuan (Z) = {z_optimal}")
    # result_label.pack()
    
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


    # Jika jumlah variabel kurang dari atau sama dengan 2, tampilkan tombol Tampilkan Grafik untuk menampilkan grafik
    if len(a_values) <= 2:
        graph_button = Button(result_window, text="Tampilkan Grafik", command=lambda: show_graph_max(x_optimal, z_optimal, c_values))
        graph_button.pack()

# Fungsi untuk menampilkan grafik hasil optimasi
def show_graph_max(x_optimal, z_optimal, c_values):
    global result_window 
    result_window.destroy()
    x_values = np.linspace(0, 100, 100)

    plt.figure(figsize=(8, 6))

    # Menampilkan batasan kendala dalam bentuk garis pada grafik
    for i, c_row in enumerate(c_values):
        a = c_row[0]
        b = c_row[1]
        c = c_row[2]
        y_values = (c - a * x_values) / b
        plt.plot(x_values, y_values, label="{}x1 + {}x2 <= {}".format(a, b, c))

    # Menampilkan titik optimal pada grafik
    plt.scatter(x_optimal[0], x_optimal[1], color='red', marker='o',
                label='Solusi Optimal (x1={}, x2={}, z={})'.format(x_optimal[0], x_optimal[1], z_optimal))

    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.xlim(0, 100)
    plt.ylim(0, 100)

    plt.legend()
    plt.title("Optimasi (Maksimum)")
    plt.grid(True)
    plt.show()
# Fungsi untuk menampilkan hasil optimasi dalam jendela terpisah
def display_optimization_result_min(x_optimal, z_optimal, c_values, a_values):
    global result_window 
    result_window = tk.Toplevel()
    result_window.title("Hasil Optimasi")
    
    result_label = Label(result_window, text="Hasil Optimasi:")
    result_label.pack()

    # # Menampilkan nilai variabel x yang optimal
    # for i, x_val in enumerate(x_optimal):
    #     if x_val is not None:
    #         result_label = Label(result_window, text=f"x{i+1} = {x_val}")
    #         result_label.pack()
    
    # # Menampilkan nilai optimal dari fungsi tujuan (Z)
    # result_label = Label(result_window, text=f"Nilai Optimal Fungsi Tujuan (Z) = {z_optimal}")
    # result_label.pack()
    
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


    # Jika jumlah variabel kurang dari atau sama dengan 2, tampilkan tombol Tampilkan Grafik untuk menampilkan grafik
    if len(a_values) <= 2:
        graph_button = Button(result_window, text="Tampilkan Grafik", command=lambda: show_graph_min(x_optimal, z_optimal, c_values))
        graph_button.pack()

# Fungsi untuk menampilkan grafik hasil optimasi
def show_graph_min(x_optimal, z_optimal, c_values):
    global result_window 
    result_window.destroy()
    x_values = np.linspace(0, 100, 100)

    plt.figure(figsize=(8, 6))

    # Menampilkan batasan kendala dalam bentuk garis pada grafik
    for i, c_row in enumerate(c_values):
        a = c_row[0]
        b = c_row[1]
        c = c_row[2]
        y_values = (c - a * x_values) / b
        plt.plot(x_values, y_values, label="{}x1 + {}x2 >= {}".format(a, b, c))

    # Menampilkan titik optimal pada grafik
    plt.scatter(x_optimal[0], x_optimal[1], color='red', marker='o',
                label='Solusi Optimal (x1={}, x2={}, z={})'.format(x_optimal[0], x_optimal[1], z_optimal))

    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.xlim(0, 100)
    plt.ylim(0, 100)

    plt.legend()
    plt.title("Optimasi (Minimum)")
    plt.grid(True)
    plt.show()

# Fungsi untuk melakukan optimasi maksimum dan menampilkan hasilnya
def optimize_and_plot_max(a_values, c_values):
    global result_window 
    problem = LpProblem("Optimasi", LpMaximize)

    x = [LpVariable(f"Optimasi{i+1}", lowBound=0) for i in range(len(c_values))]

    # Menentukan fungsi tujuan yang akan dimaksimalkan
    problem += lpSum([a_values[i] * x[i] for i in range(len(a_values))])

    # Menambahkan kendala ke dalam permasalahan
    for j, c_row in enumerate(c_values):
        problem += lpSum([c_row[j] * x[j] for j in range(len(c_row) - 1)]) <= c_row[-1]

    # Menyelesaikan permasalahan
    problem.solve()
    
    # Mendapatkan nilai variabel x yang optimal dan nilai optimal dari fungsi tujuan (Z)
    x_optimal = [x[i].varValue for i in range(len(x))]
    z_optimal = value(problem.objective)

    # Menampilkan hasil optimasi ke jendela terpisah
    display_optimization_result_max(x_optimal, z_optimal, c_values, a_values)
    
# Fungsi untuk melakukan optimasi minimum dan menampilkan hasilnya
def optimize_and_plot_min(a_values, c_values):
    global result_window 
    problem = LpProblem("Optimasi", LpMinimize)

    x = [LpVariable(f"Optimasi{i+1}", lowBound=0) for i in range(len(c_values))]

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
    display_optimization_result_min(x_optimal, z_optimal, c_values, a_values)
