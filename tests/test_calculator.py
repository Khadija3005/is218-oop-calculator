import pytest
from calculator import Add, Subtract, History


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
def test_history_add():
    history = History()
    calculation = Add(10, 5)

    history.add(calculation)

    assert len(history.get_all()) == 1
    assert history.get_all()[0] is calculation


def test_history_remove():
    history = History()
    history.add(Add(10, 5))
    history.add(Subtract(20, 7))

    removed = history.remove(0)

    assert isinstance(removed, Add)
    assert len(history.get_all()) == 1
    assert isinstance(history.get_all()[0], Subtract)


def test_history_clear():
    history = History()
    history.add(Add(10, 5))

    history.clear()

    assert history.get_all() == []
def test_abstract_calculation():
    from calculator import Calculation

    with pytest.raises(TypeError):
        Calculation(10, 5)
