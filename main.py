import numpy as np
from scipy import ndimage


def count_groups(arr):
    arr = np.array(arr)
    labels, num_groups = ndimage.label(arr)
    sizes = ndimage.sum(arr, labels, range(1, num_groups+1))
    return num_groups, sorted([int(x) for x in sizes], reverse=True), int(sizes.sum())


def main():
    test = [[1, 1, 0, 0, 0, 0, 1, 1],

            [1, 1, 0, 1, 1, 0, 1, 1],

            [0, 0, 0, 1, 1, 0, 0, 0],

            [1, 1, 0, 1, 1, 0, 1, 1],

            [1, 1, 0, 0, 0, 0, 1, 1]]

    num_groups, sizes, total = count_groups(test)
    print('{} teams of {} totaling {}'.format(num_groups, sizes, total))


main()
