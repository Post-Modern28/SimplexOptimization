import numpy as np
import Simplex

def main():
    C = np.array(list(map(int, input().split())))
    A = []
    for i in range(len(C)):
        A.append(list(map(int, input().split())))
    A = np.array(A)
    b = np.array(list(map(int, input().split())))
    approximation_accuracy = int(input())
    #b = np.expand_dims(b, axis=0)
    #A = np.hstack((A, np.eye(len(C))))
    #A = np.hstack((A, b.transpose()))
    #C = np.hstack((C, np.zeros(len(C))))
    Simplex.apply_simplex_maximization(C, A, b)


if __name__ == "__main__":
    main()
