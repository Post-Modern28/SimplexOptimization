import numpy as np


def interior_point_algorithm(main_function: np.array, constraints_matrix: np.array, constraints_vector: np.array,
                             init_point: np.array, alpha) -> None:
    c = main_function
    A = constraints_matrix
    D = np.diag(init_point)
    D_prev = D - 100
    n = 1
    diff = D - D_prev
    x = init_point
    r = max(np.amax(diff), np.amin(diff), key=abs)
    while abs(r) > 0.0001:
        print(f"Iter {n}")
        x_old = x
        A_prime = A @ D
        c_prime = D @ c
        A_prime_def_inverse = A_prime.transpose() @ np.linalg.inv(A_prime @ A_prime.transpose()) @ A_prime
        I = np.eye(A_prime_def_inverse.shape[0])
        P = I - A_prime_def_inverse
        c_proj = P @ c_prime
        min_neg = np.min(c_proj)
        if min_neg >= 0:
            break
        v = abs(np.min(c_proj))
        y = np.ones(A_prime_def_inverse.shape[0]) + alpha/v * c_proj

        x = D @ y
        D_prev = D
        answ = x
        print("result:")
        print(answ)
        D = np.diag(x)
        # diff = D-D_prev
        # r = max(np.amax(diff), np.amin(diff), key=abs)
        diff = x - x_old
        r = np.linalg.norm(diff, ord=2)
        n += 1


if __name__ == "__main__":
    mf = np.array([1, 2, 0])
    constr = np.array([1, 1, 1])
    in_p = np.array([2, 2, 4])
    free_v = np.array([8])

    # x = np.array([1/2, 7/2, 1, 2])
    # A = np.array([[2, 4, 1, 0], [1, 3, 0, -1]])
    # c = np.array([1, 1, 0, 0])
    x = np.array( [ 1 , 1 , 1 , 315 , 174 , 169])
    A = np.array([[18, 15, 12, 1, 0, 0], [6, 4, 8, 0, 1, 0], [5, 3, 3, 0, 0, 1]], float)
    c = np.array([9, 10, 16, 0, 0, 0], float)

    #interior_point_algorithm(mf, constr, free_v, in_p, 0.5)
    interior_point_algorithm(c, A, [], x, 0.5)
