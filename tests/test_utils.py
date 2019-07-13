import pytest
from num2words.utils import input_handler, InvalidNumber


@pytest.mark.parametrize("input_str, answer", [
    ("The pump is 536 deep underground", 536),
    ("We processed 9121 records.", 9121),
    ("Interactive and printable 10022 ZIP code.", 10022),
    ("The database has 66723107008 records.", 66723107008),
    ("The speed of light is 299792458 meters per second", 299792458),
    ("In the year 681 things were different!", 681),
    ("The company generated 136819 million USD in revenue this year", 136819)
])
def test_input_handler(input_str, answer):
    assert input_handler(input_str) == answer


@pytest.mark.parametrize("input_str, answer", [
    ("Variables reported as having a missing type #65678", InvalidNumber),
    ("I received 23 456,9 KGs.", InvalidNumber),
    ("On average only 36% succeed", InvalidNumber),
    ("Planck's constant is 6.62607004 x 10^-34 m^2 kg / s", InvalidNumber),
    ("The speed of light is 299,792,458 meters per second", InvalidNumber),
    ("The speed of light is 299 792 458 meters per second", InvalidNumber),
    ("It is only 1/4th of an inch in length", InvalidNumber),
    ("Use 0.25 kilos, please", InvalidNumber),
])
def test_input_handler_error(input_str, answer):
    with pytest.raises(answer):
        input_handler(input_str)