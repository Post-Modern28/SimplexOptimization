import numpy as np


def main():
    C = np.array(list(map(int, input().split())))
    A = []
    for i in range(len(C)):
        A.append(list(map(int, input().split())))
    A = np.array(A)
    b = np.array(list(map(int, input().split())))
    approximation_accuracy = int(input())


if __name__ == "__main__":
    main()
