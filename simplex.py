# import numpy as np
# from scipy.optimize import linprog

# # Koefisien fungsi tujuan
# c = np.array([-80000, -70000])  # Dikali -1 karena kita akan maksimalkan

# # Koefisien kendala
# A = np.array([
#     [75, 150],
#     [150, 150],
#     [80, 100],
#     [120, 50]
# ])
# b = np.array([10000, 15000, 20000, 10000])

# # Batas variabel
# x_bounds = [(0, None), (0, None)]

# # Menyelesaikan masalah pemrograman linear
# result = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method='simplex')

# # Menampilkan hasil
# x1, x2 = result.x
# z = -result.fun  # Kembali ke nilai maksimasi fungsi tujuan asli
# print("x1:", x1)
# print("x2:", x2)
# print("z:", z)
