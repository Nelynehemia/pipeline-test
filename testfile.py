from main import main


def test_method():
    assert main(3) == 8
    assert main(2) != 8


test_method()
