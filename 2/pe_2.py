
def solve():
    fib = [1, 2]
    even = [2]
    while sum(fib[-2:]) <= 4000000:
        number = sum(fib[-2:])
        if number % 2:
            even.append(number)
        fib.append(number)

    return sum(even)


def main():
    print(f"{solve()=}")


if __name__ == "__main__":
    main()


