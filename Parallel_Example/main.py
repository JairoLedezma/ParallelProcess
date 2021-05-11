import multiprocessing as mp
print("Number of processors: ", mp.cpu_count())

import numpy as np
from time import time


def howmany_within_range(row, minimum, maximum):
    """Returns how many numbers lie within `maximum` and `minimum` in a given `row`"""
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return count



if __name__ == '__main__':
    # Prepare data
    np.random.RandomState(100)
    arr = np.random.randint(0, 10, size=[200000, 5])
    data = arr.tolist()
    data[:5]

    results = []
    for row in data:
        results.append(howmany_within_range(row, minimum=4, maximum=8))
    pool = mp.Pool(mp.cpu_count())

    results = pool.starmap(howmany_within_range, [(row, 4, 8) for row in data])

    pool.close()
    print(results[:10])
    # > [3, 1, 4, 4, 4, 2, 1, 1, 3, 3]
