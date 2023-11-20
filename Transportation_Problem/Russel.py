import numpy as np


def russel(supplies: np.array, costs: np.array, demand: np.array):

    """
    Solves the transportation problem using Russel's approximation

    :param supplies:  array representing stations with supplies
    :param costs: matrix representing a price of moving 1 unit from i-th supply base to j-th destination point
    :param demand: array representing destination points and their demands
    :return: Total cost of achieved feasible solution

    """

    supplies = np.copy(supplies)
    demand = np.copy(demand)
    if sum(supplies) != sum(demand):
        print("The problem is not balanced!")
        return -1
    result = np.zeros(costs.shape)
    row_costs = np.max(costs, axis=1)  # find maximal element in each row
    col_costs = np.max(costs, axis=0)  # find maximal element in each column
    diff_matrix = costs - (row_costs.reshape(-1, 1) + col_costs.reshape(1, -1))  # construct a matrix diff_matrix,
    # where diff_matrix[i][j] = costs[i][j] - (row_costs[i] + col_costs[j])

    while sum(demand) != 0:
        # take the indices of minimal element in diff_matrix
        i, j = np.unravel_index(np.argmin(diff_matrix), diff_matrix.shape)
        taken = min(supplies[i], demand[j])
        result[i, j] = costs[i, j] * taken
        supplies[i] -= taken
        demand[j] -= taken

        if supplies[i] == 0:  # if supply point is empty, nullify its row
            diff_matrix[i, :] = np.inf
        if demand[j] == 0:  # if demand point is satisfied, nullify its column
            diff_matrix[:, j] = np.inf
    print(result)
    summary = np.sum(result)
    print(f"Total cost: {summary}")
    return summary


def main():
    s = np.array([160, 140, 170])
    costs = np.array([[7, 8, 1, 2],
                      [4, 5, 9, 8],
                      [9, 2, 3, 6]]).astype(float)
    demand = np.array([120, 50, 190, 110])
    russel(s, costs, demand)


if __name__ == "__main__":
    main()

