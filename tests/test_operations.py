from src import addition, multiply, subtraction, divide


def test_addition():
    assert addition(2, 3) == 5


def test_subtraction():
    assert subtraction(5, 3) == 2


def test_multiply():
    assert multiply(2, 3) == 6

def test_divide():
    assert divide(6, 3) == 2
    try:
        divide(5, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero."
    else:
        assert False, "Expected ValueError for division by zero"