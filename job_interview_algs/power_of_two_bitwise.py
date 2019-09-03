# complexity O(1)
def is_power_of_two(n):
    if not isinstance(n, int) or n < 1:
        return False

    if n & (n - 1) == 0:
        return True
    return False

if __name__ == "__main__":
    print(is_power_of_two(1))
    print(is_power_of_two(7))
    print(is_power_of_two(64))
    print(is_power_of_two(1024))
