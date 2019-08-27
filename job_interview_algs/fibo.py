def fibo(number):
    if not isinstance(number, int) or number < 1:
        print("N should be more than 0 and int...")
        return None
    if number in [1, 2]:
        return 1
    else:
        return fibo(number - 1) + fibo(number - 2)


if __name__ == "__main__":
    print(fibo(6))
    print(fibo("String"))
    print(fibo(-2))
    print(fibo(4))
