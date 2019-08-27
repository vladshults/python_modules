def factorial(number):
    if not isinstance(number, int) or number < 0:
        print("N should be not negative and int...")
        return None
    if number == 1:
        return 1
    elif number == 0:
        return 1
    else:
        return number * factorial(number - 1)


if __name__ == "__main__":
    print(factorial(6))
    print(factorial("String"))
    print(factorial(-2))
    print(factorial(0))
