from random import random
from numba import jit


@jit(nopython=True)
def monte_carlo_pi(n):
    counter = 0
    for _ in range(n+1):
        x = random()
        y = random()
        if (x ** 2 + y ** 2) < 1:
            counter += 1
    return 4 * counter / n


if __name__ == "__main__":
    print(monte_carlo_pi(10000))
