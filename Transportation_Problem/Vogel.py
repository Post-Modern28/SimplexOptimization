import numpy as np


def vogel(supplies: np.array, costs: np.array, demand: np.array):
    """
    Solves the transportation problem using Vogel's approximation

    :param supplies:  array representing stations with supplies
    :param costs: matrix representing a price of moving 1 unit from i-th supply base to j-th destination point
    :param demand: array representing destination points and their demands
    :return: Total cost of achieved feasible solution
    """

    supplies = np.copy(supplies)
    demand = np.copy(demand)
    costs = np.copy(costs)
    if sum(supplies) != sum(demand):
        print("The problem is not balanced!")
        return -1
    result = np.zeros(costs.shape)

    while sum(demand) != 0:
        # find maximal difference among rows and columns
        row_diff = calculate_differences(costs, axis=1)
        column_diff = calculate_differences(costs, axis=0)
        col_max = max(column_diff)
        row_max = max(row_diff)
        # pick minimal element in row/column with maximal difference
        if col_max > row_max:
            j = np.argmax(column_diff)
            i = np.argmin(costs[:, j])
        else:
            i = np.argmax(row_diff)
            j = np.argmin(costs[i])
        taken = min(supplies[i], demand[j])
        result[i, j] = costs[i, j] * taken
        supplies[i] -= taken
        demand[j] -= taken
        if demand[j] == 0:  # if demand point is satisfied, nullify its column
            costs[:, j] = np.inf
        if supplies[i] == 0:  # if supply point is empty, nullify its row
            costs[i, :] = np.inf
    print(result)
    summary = np.sum(result)
    print(f"Total cost: {summary}")
    return summary


def calculate_differences(costs: np.array, axis=0) -> np.array:
    """
    Calculates differences between second minimal element in each column/row of a given matrix

    :param costs: matrix representing a price of moving 1 unit from i-th supply base to j-th destination point
    :param axis: 0 for column, 1 for row
    :return: vector representing differences between second minimal and minimal element in each column/row
    """
    np.seterr(all="ignore")
    if not axis:
        s = np.sort(costs, axis=0)
        diff = np.array([s[1, i]-s[0, i] for i in range(costs.shape[1])])
        diff = np.nan_to_num(diff, posinf=-5, nan=-1, neginf=0)
        for i in range(len(diff)):
            if diff[i] == -5:
                diff[i] = s[0, i]
        return np.array(diff)

    s = np.sort(costs, axis=1)
    diff = np.array([s[i, 1] - s[i, 0] for i in range(costs.shape[0])])
    diff = np.nan_to_num(diff, posinf=-5, nan=-1, neginf=0)
    for i in range(len(diff)):
        if diff[i] == -5:
            diff[i] = s[i, 0]
    return np.array(diff)


def main():
    s = np.array([140, 180, 160])
    costs = np.array([[2, 3, 4, 2, 4],
                      [8, 4, 1, 4, 1],
                      [9, 7, 3, 7, 2]]).astype(float)
    demand = np.array([60, 70, 120, 130, 100])
    vogel(s, costs, demand)


if __name__ == "__main__":
    main()
