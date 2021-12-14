
def is_palindrome(number):
    str_num = str(number)
    return str_num == str_num[::-1]


def solve(max_limit):
    max_palindrome = 0
    for i in range(max_limit, max_limit // 10, -1):
        for j in range(max_limit, max_limit // 10, -1):
            if is_palindrome(i * j) and (i * j) > max_palindrome:
                max_palindrome = i * j
    return max_palindrome


def main():
    print(f"{solve(999)=}")


def test():
    assert solve(99) == 9009


if __name__ == "__main__":
    main()
