from itertools import cycle


def cycled(arr=None):
    if not arr:
        return list()
    pool = cycle(arr)
    for item in pool:
        yield item


if __name__ == "__main__":
    l = ["a", "b", "c"]
    inf = cycled(l)
    for _ in range(6):
        print(next(inf))
