import numpy as np


def north_west(supplies: np.array, costs: np.array, demand: np.array):
    """
    Solves the transportation problem using North-West algorithm

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
    row = column = 0
    while row != len(supplies) and column != len(demand):
        taken = min(demand[column], supplies[row])
        result[row, column] = costs[row, column] * taken
        demand[column] -= taken
        supplies[row] -= taken
        if demand[column] < supplies[row]:  # if demand point is satisfied
            column += 1  # move to next demand point
        else:  # otherwise, move to next supply point
            row += 1
    print(result)
    summary = np.sum(result)
    print(f"Total cost: {summary}")
    return summary


def main():
    s = np.array([140, 180, 160])
    costs = np.array([[2, 3, 4, 2, 4],
                      [8, 4, 1, 4, 1],
                      [9, 7, 3, 7, 2]]).astype(float)
    demand = np.array([60, 70, 120, 130, 100])
    north_west(s, costs, demand)


if __name__ == "__main__":
    main()
