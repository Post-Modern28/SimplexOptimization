import numpy as np
from Vogel import vogel
from Russel import russel
from NorthStar import north_west


def main():
    supply_num = int(input("How many supply points?\n"))
    supplies = np.array(list(map(int, input("Enter amount of supply in each point, separated by space:\n").split()))).astype(float)
    demand_num = int(input("How many demand points?\n"))
    demands = np.array(list(map(int, input("Enter demand in each point, separated by space:\n").split()))).astype(float)
    print("Enter costs matrix:")
    costs_matrix = []
    for i in range(supply_num):
        row = list(map(int, input().split()))
        costs_matrix.append(row)
    costs_matrix = np.array(costs_matrix).astype(float)
    print("Solution with North-Star algorithm:")
    north_west(supplies, costs_matrix, demands)
    print("Solution with Vogel's approximation:")
    vogel(supplies, costs_matrix, demands)
    print("Solution with Russel's approximation:")
    russel(supplies, costs_matrix, demands)


if __name__ == "__main__":
    main()
