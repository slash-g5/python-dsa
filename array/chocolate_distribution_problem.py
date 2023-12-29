# problem link https://www.geeksforgeeks.org/chocolate-distribution-problem/
import sys


def solve(choco_packs, num_students):
    choco_packs.sort()
    num_packs = len(choco_packs)
    if num_packs < num_students:
        return -1
    if num_students == 1:
        return 0
    min_dif = sys.maxsize
    for i in range(num_students - 1, num_packs):
        if min_dif > (choco_packs[i] - choco_packs[i + 1 - num_students]):
            min_dif = choco_packs[i] - choco_packs[i + 1 - num_students]
    return min_dif


if __name__ == '__main__':
    choco_packs = [1, 6, 8, 9, 12]
    print(solve(choco_packs, 3))
    print(solve(choco_packs, 5))
    print(solve([5, 1, 6, 2, 9, 0, 4, 121, 13, 2], 4))
