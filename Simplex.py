from typing import Optional, List
import numpy as np


def apply_simplex_maximization(main_function, constraints_matrix,
                               constraints_vector, approx=0) -> None:
    n = len(main_function)
    eps = 10 ** -9
    constraints_matrix = make_matrix(main_function, constraints_matrix, constraints_vector)
    shp = constraints_matrix.shape
    basis_indices = list(range(n, n + constraints_matrix.shape[0]-1))
    iter_num = 1
    print("Step 0:")
    print(constraints_matrix)
    while np.any(constraints_matrix[0, : shp[1] - 1] < 0):
        pivot_index = np.argmin(constraints_matrix[0, :shp[1] - 1])
        ratios = np.divide(constraints_matrix[1:, -1],  constraints_matrix[1:, pivot_index])
        ratios[ratios <= 0+eps] = np.inf
        if np.all(ratios == np.inf):
            print("Method is not applicable!")
            return
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
    resulting_vals = [0 for _ in range(n)]
    for i in range(n):
        if basis_indices[i] < n:
            resulting_vals[basis_indices[i]] = constraints_matrix[i+1, -1]
    for i in range(n):
        print(f"x{i+1} = {round(resulting_vals[i], approx)}", end='')
        if i != n-1:
            print(", ", end='')
    z = constraints_matrix[0][-1]
    print(f'\nMaximal value of the function: {round(z, approx)}')


def apply_simplex_minimization(main_function, constraints_matrix,
                               constraints_vector, approx=0) -> None:
    eps = 10**-9
    n = len(main_function)
    constraints_matrix = make_matrix(main_function, constraints_matrix, constraints_vector)
    shp = constraints_matrix.shape
    basis_indices = list(range(n, n + constraints_matrix.shape[0]-1))
    iter_num = 1
    print("Step 0:")
    print(constraints_matrix)
    while np.any(constraints_matrix[0, : shp[1] - 1] > 0):
        pivot_index = np.argmax(constraints_matrix[0, :shp[1] - 1])
        ratios = np.divide(constraints_matrix[1:, -1],  constraints_matrix[1:, pivot_index])
        ratios[ratios <= 0+eps] = np.inf
        if np.all(ratios == np.inf):
            print("Method is not applicable!")
            return
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
    resulting_vals = [0 for _ in range(n)]
    for i in range(n):
        if basis_indices[i] < n:
            resulting_vals[basis_indices[i]] = constraints_matrix[i+1, -1]
    for i in range(n):
        print(f"x{i+1} = {round(resulting_vals[i], approx)}", end='')
        if i != n-1:
            print(", ", end='')
    z = constraints_matrix[0][-1]
    print(f'\nMaximal value of the function: {round(z, approx)}')


def make_matrix(function, constraints, constraints_free_variables):
    constraints_free_variables = np.expand_dims(constraints_free_variables, axis=0)
    constraints = np.hstack((constraints, np.eye(constraints.shape[0])))
    constraints = np.hstack((constraints, constraints_free_variables.transpose()))
    function *= -1
    function = np.hstack((function, np.zeros(constraints.shape[0]+1)))
    constraints = np.vstack((function, constraints))
    return constraints
