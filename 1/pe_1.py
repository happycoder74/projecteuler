def get_data(max=1000):
    data = [i for i in range(max)]
    return data


def solve(data):

    number_list = set()

    for number in data:
        if (number % 3 == 0) or (number % 5 == 0):
            number_list.add(number)

    return sum(number_list)


def test_solve():
    data = get_data(10)
    assert solve(data) == 23


def main():
    data = get_data()

    print(f"Solution: {solve(data)=}")


if __name__ == "__main__":
    main()
