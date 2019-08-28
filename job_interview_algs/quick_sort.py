from random import randint


def quicksort(a):
    if len(a) <= 1:
        return a

    small, equal, larger = [], [], []
    pivot = a[randint(0, len(a)-1)]
    for i in a:
        if i < pivot:
            small.append(i)
        elif i == pivot:
            equal.append(i)
        else:
            larger.append(i)

    return quicksort(small) + equal + quicksort(larger)


if __name__ == "__main__":
    l = [99, 87, 129, 3, 27, 49, 11, 55]
    print(quicksort(l))
