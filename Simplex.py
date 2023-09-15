from typing import Optional, List

import numpy as np


def apply_simplex_maximization(main_function, constraints_matrix,
                               constraints_vector, approx=0):
    n = len(main_function)
    init_func = main_function[:]
    # Doing some concatenation operations to create a big matrix
    constraints_vector = np.expand_dims(constraints_vector, axis=0)
    constraints_matrix = np.hstack((constraints_matrix, np.eye(constraints_matrix.shape[0])))
    constraints_matrix = np.hstack((constraints_matrix, constraints_vector.transpose()))
    main_function = np.hstack((main_function, np.zeros(constraints_matrix.shape[0] + 1)))
    constraints_matrix = np.vstack((main_function, constraints_matrix))
    shp = constraints_matrix.shape
    basis_indices = list(range(n, 2 * n))
    iter_num = 1
    while np.any(constraints_matrix[0, : shp[1] - 1] > 0):
        pivot_index = np.argmax(constraints_matrix[0, :shp[1] - 1])
        ratios = np.divide(constraints_matrix[1:, -1],  constraints_matrix[1:, pivot_index])
        ratios[ratios < 0] = np.inf
        pivot_row_index = np.argmin(ratios) + 1
        constraints_matrix[pivot_row_index] = constraints_matrix[pivot_row_index] / constraints_matrix[pivot_row_index][pivot_index]
        for i in range(shp[0]):
            if i == pivot_row_index:
                continue
            constraints_matrix[i] = constraints_matrix[i] - (constraints_matrix[pivot_row_index] * constraints_matrix[i][pivot_index])
        print(f"Step {iter_num}:")
        print(constraints_matrix)
        basis_indices[pivot_row_index-1] = pivot_index
        iter_num += 1
    resulting_vals = [0 for i in range(n)]
    for i in range(n):
        if basis_indices[i] < n:
            resulting_vals[basis_indices[i]] = constraints_matrix[i+1, -1]
    for i in range(n):
        print(f"x{i+1} = {round(resulting_vals[i], approx)}", end='')
        if i != n-1:
            print(", ", end='')
    resulting_vals = np.array(resulting_vals)
    z = resulting_vals @ init_func
    print(f'\nMaximal value of the function: {z}')



