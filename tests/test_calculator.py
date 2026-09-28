from calculator import Add, Subtract


def test_add():
    calculation = Add(10, 5)

    assert calculation.a == 10
    assert calculation.b == 5
    assert calculation.calculate() == 15


def test_subtract():
    calculation = Subtract(10, 5)

    assert calculation.a == 10
    assert calculation.b == 5
    assert calculation.calculate() == 5