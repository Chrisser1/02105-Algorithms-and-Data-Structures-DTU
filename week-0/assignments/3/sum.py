def read_two_integers() -> tuple[int, int]:
    str = input()

    # If the input is not in the correct format, raise an error
    if len(str.split()) != 2:
        raise ValueError("Input must contain two integers separated by a space")

    try:
        a, b = map(int, str.split())
    except ValueError:
        raise ValueError("Input must contain two integers separated by a space")
    return a, b

if __name__ == "__main__":
    a, b = read_two_integers()
    print(a + b)
