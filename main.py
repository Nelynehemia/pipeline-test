import os


def main(x):
    return x + 5


def test_method():
    assert main(3) == 8


if __name__ == "__main__":
    main(3)
