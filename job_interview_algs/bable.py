# complexity O(n ** 2) because of a nested loop
import copy


def bable_sort(arr=list()):
    if not arr:
        return list()

    list_to_sort = copy.deepcopy(arr)
    n = len(list_to_sort)
    for i in range(n-1):
        for j in range(n-i-1):
            if list_to_sort[j] > list_to_sort[j+1]:
                list_to_sort[j], list_to_sort[j+1] = list_to_sort[j+1], list_to_sort[j]
    return list_to_sort


if __name__ == "__main__":
    l = [99, 55, 1, 7, 25, 66, 128, 129, 3]
    print(bable_sort(l))
