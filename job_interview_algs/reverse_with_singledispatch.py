import functools


def swap_it(arr):
    i = 0
    j = -1
    for _ in range(len(arr)//2):
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr


@functools.singledispatch
def reverse_it(seq):
    return swap_it(seq)


@reverse_it.register(list)
def _(arr):
    return swap_it(arr)


@reverse_it.register(str)
def _(text):
    s = list(text)
    return ''.join(swap_it(s))


@reverse_it.register(tuple)
def _(t):
    s = list(t)
    return tuple(swap_it(s))


if __name__ == "__main__":
    l1 = [1, 2, 3, 4, 5, 6, 7, 8]
    l2 = ('раз', 'два', 'три', 'четыре', 'пять', )
    l3 = 'abracadabra'
    print(reverse_it(l1))
    print(reverse_it(l2))
    print(reverse_it(l3))
