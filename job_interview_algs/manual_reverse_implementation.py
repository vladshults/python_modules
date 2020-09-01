def swap_it(arr):
    i = 0
    j = -1
    for _ in range(len(arr)//2):
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr


def reverse_it(seq):
    if isinstance(seq, list):
        return swap_it(seq)
    elif isinstance(seq, str):
        s = list(seq)
        return ''.join(swap_it(s))
    elif isinstance(seq, tuple):
        s = list(seq)
        return tuple(swap_it(s))


if __name__ == "__main__":
    l1 = [1, 2, 3, 4, 5, 6, 7, 8]
    l2 = ('раз', 'два', 'три', 'четыре', 'пять', )
    l3 = 'abracadabra'
    print(reverse_it(l1))
    print(reverse_it(l2))
    print(reverse_it(l3))
