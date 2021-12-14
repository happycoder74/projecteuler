import math


def is_prime(number):
    if number <= 1:
        return False
    for n in range(2, number // 2):
        if number % n == 0:
            return False
    return True


def solve(number):
    factors = []
    for n in range(math.floor(math.sqrt(number)), 2, -1):
        if number % n == 0:
            if is_prime(n):
                return n




def main():
    number = 600851475143

    print(f"{solve(number)=}")


def test_solve():
    number = 13195
    assert solve(number) == 29


if __name__ == "__main__":
    main()


