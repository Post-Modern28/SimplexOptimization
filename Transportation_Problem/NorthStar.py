import numpy as np


def NorthStar(supplies: np.array, costs: np.array, demand: np.array):
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
        if demand[column] < supplies[row]:
            column += 1
        else:
            row += 1
    print(result)
    summary = np.sum(result)
    print(f"Total cost: {summary}")
    return summary


def main():
    s = np.array([160, 140, 170])
    costs = np.array([[7, 8, 1, 2],
                      [4, 5, 9, 8],
                      [9, 2, 3, 6]]).astype(float)
    print(np.max(costs, axis=1))
    demand = np.array([120, 50, 190, 110])
    NorthStar(s, costs, demand)


if __name__ == "__main__":
    main()
