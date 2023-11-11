import numpy as np
from NorthStar import NorthStar
np.seterr(all="ignore")


def Vogel(supplies: np.array, costs: np.array, demand: np.array):
    if sum(supplies) != sum(demand):
        print("The problem is not balanced!")
        return -1
    result = np.zeros(costs.shape)
    while sum(demand) != 0:
        row_diff = calculate_differences(costs, axis=1)
        column_diff = calculate_differences(costs, axis=0)
        col_max = max(column_diff)
        row_max = max(row_diff)
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
        if demand[j] == 0:
            costs[:, j] = np.inf
        if supplies[i] == 0:
            costs[i, :] = np.inf
    print(result)
    summary = np.sum(result)
    print(f"Total cost: {summary}")
    return summary


def calculate_differences(costs: np.array, axis=0) -> np.array:
    if not axis:
        s = np.sort(costs, axis=0)
        diff = np.array([s[1, i]-s[0, i] for i in range(costs.shape[1])])

        diff = np.nan_to_num(diff, posinf=0, nan=0, neginf=0)
        # print(diff)
        return np.array(diff)

    s = np.sort(costs, axis=1)

    diff = np.array([s[i, 1] - s[i, 0] for i in range(costs.shape[0])])
    diff = np.nan_to_num(diff, posinf=1, nan=0, neginf=0)

    # print(diff)
    return np.array(diff)



def main():
    s = np.array([160, 140, 170])
    costs = np.array([[7, 8, 1, 2],
                      [4, 5, 9, 8],
                      [9, 2, 3, 6]]).astype(float)
    demand = np.array([120, 50, 190, 110])
    Vogel(s, costs, demand)


if __name__ == "__main__":
    main()
