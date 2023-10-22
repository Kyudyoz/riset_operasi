import matplotlib.pyplot as plt
import numpy as np
from pulp import *


# Fungsi untuk melakukan optimasi maksimum dan memplot hasilnya
def optimize_and_plot_max(a, b, c_values):
    # Inisialisasi permasalahan linear dengan tujuan maksimasi (LpMaximize)
    problem = LpProblem("x", LpMaximize)

    # Membuat variabel x1 dan x2 dengan batasan non-negatif
    x = [LpVariable(f"x{i+1}", lowBound=0) for i in range(len(c_values))]

    # Menentukan fungsi tujuan yang akan dimaksimalkan
    problem += a * x[0] + b * x[1]

    # Menambahkan kendala (constraints) ke permasalahan
    for i, c_row in enumerate(c_values):
        problem += sum(c_row[j] * x[j] for j in range(len(c_row) - 1)) <= c_row[-1]

    # Menyelesaikan permasalahan menggunakan solver PuLP
    problem.solve()

    # Mendapatkan nilai variabel x yang optimal dan nilai optimal dari fungsi tujuan (Z)
    x_optimal = [x[i].varValue for i in range(len(x))]
    z_optimal = value(problem.objective)

    # Plot batasan (constraints)
    x_values = np.linspace(0, 100, 100)

    plt.figure(figsize=(8, 6))

    for i, c_row in enumerate(c_values):
        y_values = (c_row[-1] - c_row[0] * x_values) / c_row[1]
        plt.plot(
            x_values,
            y_values,
            label="{}x1 + {}x2 <= {}".format(c_row[0], c_row[1], c_row[2]),
        )

    # Plot titik solusi optimal
    plt.scatter(
        x_optimal[0],
        x_optimal[1],
        color="red",
        marker="o",
        label="Optimal Solution (x1={}, x2={}, z={})".format(
            x_optimal[0], x_optimal[1], z_optimal
        ),
    )

    # Menambahkan label sumbu dan judul grafik
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.xlim(0, 100)
    plt.ylim(0, 100)

    # Menambahkan legenda dan judul grafik
    plt.legend()
    plt.title("Optimasi Maksimum")
    plt.grid(True)
    plt.show()


# Fungsi untuk melakukan optimasi minimum dan memplot hasilnya
def optimize_and_plot_min(a, b, c_values):
    # Inisialisasi permasalahan linear dengan tujuan minimasi (LpMinimize)
    problem = LpProblem("x", LpMinimize)

    # Membuat variabel x1 dan x2 dengan batasan non-negatif
    x = [LpVariable(f"x{i+1}", lowBound=0) for i in range(len(c_values))]

    # Menentukan fungsi tujuan yang akan diminimalkan
    problem += a * x[0] + b * x[1]

    # Menambahkan kendala (constraints) ke permasalahan
    for i, c_row in enumerate(c_values):
        problem += sum(c_row[j] * x[j] for j in range(len(c_row) - 1)) >= c_row[-1]

    # Menyelesaikan permasalahan menggunakan solver PuLP
    problem.solve()

    # Mendapatkan nilai variabel x yang optimal dan nilai optimal dari fungsi tujuan (Z)
    x_optimal = [x[i].varValue for i in range(len(x))]
    z_optimal = value(problem.objective)

    # Plot batasan (constraints)
    x_values = np.linspace(0, 100, 100)

    plt.figure(figsize=(8, 6))

    for i, c_row in enumerate(c_values):
        y_values = (c_row[-1] - c_row[0] * x_values) / c_row[1]
        plt.plot(
            x_values,
            y_values,
            label="{}x1 + {}x2 >= {}".format(c_row[0], c_row[1], c_row[2]),
        )

    # Plot titik solusi optimal
    plt.scatter(
        x_optimal[0],
        x_optimal[1],
        color="red",
        marker="o",
        label="Optimal Solution (x1={}, x2={}, z={})".format(
            x_optimal[0], x_optimal[1], z_optimal
        ),
    )

    # Menambahkan label sumbu dan judul grafik
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.xlim(0, 100)
    plt.ylim(0, 100)

    # Menambahkan legenda dan judul grafik
    plt.legend()
    plt.title("Optimasi Minimum")
    plt.grid(True)
    plt.show()
