import numpy as np

def interior_point_algorithm(main_function: np.array, constraints_matrix: np.array, init_point: np.array, a) -> None:
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
        y = np.ones(A_prime_def_inverse.shape[0]) + a / v * c_proj

        x = D @ y
        # D_prev = D
        answer = x
        print("result:")
        print(answer)
        D = np.diag(x)
        # diff = D-D_prev
        # r = max(np.amax(diff), np.amin(diff), key=abs)
        diff = x - x_old
        r = np.linalg.norm(diff, ord=2)
        n += 1

def prepare_for_algorithm(c_array, A_array, b_vector, x):
    n = len(b_vector)
    c_array = np.append(c_array, [0] * n)
    # дописать как найти инишл
    x = 
    print(f"Feasible initial solution: {x}")
    return c_array, x


if __name__ == "__main__":
    # ПРИМЕРЫ
    # x =
    # A = np.array([[6, 15, 6, 1], [14, 42, 16, 1], [2, 8, 2, 1]], float)
    # c = np.array([10, -7, -5], float)

    # x = np.array( [ 1 , 1 , 1 , 315 , 174 , 169])
    # A = np.array([[18, 15, 12, 1, 0, 0], [6, 4, 8, 0, 1, 0], [5, 3, 3, 0, 0, 1]], float)
    # c = np.array([9, 10, 16, 0, 0, 0], float)

    # НАЧАЛО ИНПУТА
    # c = np.array(list(map(float, input("Enter the coefficients of the function:\n").split())))
    # A = []
    # num_of_constraints = int(input("How many constraints?\n"))
    # print("Enter the coefficients of variables in constraints:")
    # for i in range(num_of_constraints):
    #     A.append(list(map(float, input().split())))
    # A = np.array(A)
    # print("Enter the variables of right-hand side numbers in constraints:")
    # b = np.array(list(map(float, input().split())))
    #
    # approximation_accuracy = int(input("Enter the approximation accuracy:\n"))
    
    # дописать как к А добавить коэффициенты free variables 
    A = np.array([[2, 4, 1, 0], [1, 3, 0, -1]], float)
    c = np.array([1, 1], float)
    b = np.array([16, 9], float)
    alpha = 0.5
    x = []
    A_copy = np.copy(A)
    c, x = prepare_for_algorithm(c, A_copy, b, x)
    # запуск алгоритма
    # interior_point_algorithm(c, A, x, alpha)
