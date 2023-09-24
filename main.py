import numpy as np
import Simplex


def main():
    C = np.array(list(map(int, input("Enter the coefficients of the function:\n").split())))
    A = []
    num_of_constraints = int(input("How many constraints?\n"))
    print("Enter the coefficients of variables:")
    for i in range(num_of_constraints):
        A.append(list(map(int, input().split())))
    A = np.array(A)
    print("Enter the free variables of the constraints:")
    b = np.array(list(map(int, input().split())))

    approximation_accuracy = int(input("Enter the approximation accuracy:\n"))
    flag = int(input("maximize or minimize? [1/2]: "))
    if flag == 1:
        Simplex.apply_simplex_maximization(C, A, b, approximation_accuracy)
    elif flag == 2:
        #Simplex.apply_simplex_maximization(C*(-1), A, b, approximation_accuracy)
        Simplex.apply_simplex_minimization(C, A, b, approximation_accuracy)


if __name__ == "__main__":
    main()
