from season import Duration
import pytest

def test_normal_response():
    assert str(Duration.DOB_Date("2006-06-09")) == "ten million, three hundred and forty thousand, six hundred and forty" # str() calls __str__ inside class
    assert str(Duration.DOB_Date("1998-01-15")) == "fourteen million, seven hundred and fifty-seven thousand, one hundred and twenty"


def test_invalid_form():
    with pytest.raises(SystemExit) as exc:
        Duration.DOB_Date("2006 Jan 01")
    assert exc.value.code == "Invalid date"

    with pytest.raises(SystemExit) as exc:
        Duration.DOB_Date("2006:06:09")
    assert exc.value.code == "Invalid date"

    with pytest.raises(SystemExit) as exc:
        Duration.DOB_Date("2006:06-09")
    assert exc.value.code == "Invalid date"

    with pytest.raises(SystemExit) as exc:
        Duration.DOB_Date("2006:06 09")
    assert exc.value.code == "Invalid date"


def test_other_invalid_form():
    with pytest.raises(SystemExit) as exc:
        Duration.DOB_Date("")
    assert exc.value.code == "Invalid date"

    with pytest.raises(SystemExit) as exc:
        Duration.DOB_Date("cat")
    assert exc.value.code == "Invalid date"