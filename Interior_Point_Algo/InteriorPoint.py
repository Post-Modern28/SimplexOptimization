import numpy as np

def interior_point_algorithm(main_function: np.array, constraints_matrix: np.array, init_point: np.array, a) -> None:
    print("When a = " + str(a) + ":")
    c = main_function
    A = constraints_matrix
    D = np.diag(init_point)
    D_prev = D - 100
    n = 1
    diff = D - D_prev
    x = init_point
    r = max(np.amax(diff), np.amin(diff), key=abs)
    while abs(r) > 0.0001:
        # print(f"Iteration {n}:")
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
        answer = x
        # print(answer)
        D = np.diag(x)
        diff = x - x_old
        r = np.linalg.norm(diff, ord=2)
        n += 1

    print("After the " + str(n) + " iterations" + " the final answer is:")
    num_of_constraints = 2
    for i in range(num_of_constraints):
        print(f"x{i + 1} = {answer[i]}")
    print("---------------------------")

def prepare_for_algorithm(c_array, A_array, b_vector):
    n = len(b_vector)
    c_array = np.append(c_array, [0] * n)
    x, residuals, _, _ = np.linalg.lstsq(A_array, b_vector, rcond=None)
    if np.all(residuals):
        print(f"The initial solution is: {x}")
        print("---------------------------")
    else:
        print("The method is not applicable!")
    return c_array, x


if __name__ == "__main__":
    # INPUT
    A = []
    c = np.array(list(map(float, input("Enter the coefficients of the function:\n").split())))
    num_of_constraints = int(input("How many constraints?\n"))
    print("Enter the coefficients of variables in constraints:")
    for i in range(num_of_constraints):
        A.append(list(map(float, input().split())))
        for j in range(num_of_constraints):
            if i == j:
                A[i].append(1)
            else:
                A[i].append(0)
    A = np.array(A)
    print("Enter the variables of right-hand side numbers in constraints:")
    b = np.array(list(map(float, input().split())))
    approximation_accuracy = int(input("Enter the approximation accuracy:\n"))

    alpha_1 = 0.5
    alpha_2 = 0.9

    # flag = int(input("maximize or minimize? [1/2]: "))
    # if flag == 1:
    # # what will be???
    # elif flag == 2:
    # # what will be????

    c, x = prepare_for_algorithm(c, A, b)
    interior_point_algorithm(c, A, x, alpha_1)
    interior_point_algorithm(c, A, x, alpha_2)
