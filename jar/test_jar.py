import pytest
from jar import Jar

def test_init():
    assert Jar(5)
    assert Jar(0)

    with pytest.raises(ValueError):
        Jar(-1)
        Jar("cat")



def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(5)
    jar.deposit(5)
    jar.deposit(0)

    with pytest.raises(ValueError):
        jar.deposit(1)

    jar = Jar()

    with pytest.raises(ValueError):
        jar.deposit(13)

    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(4.3)

    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit("text")


def test_withdraw():
    jar = Jar(5)
    jar.deposit(5)

    jar.withdraw(5)
    jar.withdraw(0)

    with pytest.raises(ValueError):
        jar.withdraw(1)

    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(4.3)

    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit("dog")

