import pytest
from num2words import Num2Words


@pytest.mark.parametrize("file_path, answer", [
    ("test_inputs/test1.txt", "five hundred and thirty six"),
    ("test_inputs/test2.txt", "nine thousand, one hundred and twenty one"),
    ("test_inputs/test3.txt", "ten thousand and twenty two"),
    ("test_inputs/test4.txt", "sixty six billion, seven hundred and twenty "
                              "three million, one hundred and seven thousand "
                              "and eight"),
    ("test_inputs/test5.txt", "two hundred and ninety nine million, seven "
                              "hundred and ninety two thousand, four hundred "
                              "and fifty eight"),
    ("test_inputs/test6.txt", "six hundred and eighty one"),
    ("test_inputs/test7.txt", "one hundred and thirty six thousand, eight "
                              "hundred and nineteen"),
    ("test_inputs/test17.txt", "one quintillion, two hundred and thirty four "
                               "quadrillion, five hundred and sixty seven "
                               "trillion, eight hundred and ninety billion, "
                               "nine hundred and eighty seven million, six "
                               "hundred and fifty four thousand, three "
                               "hundred and twenty one"),
    ("test_inputs/test8.txt", "number invalid"),
    ("test_inputs/test9.txt", "number invalid"),
    ("test_inputs/test10.txt", "number invalid"),
    ("test_inputs/test11.txt", "number invalid"),
    ("test_inputs/test12.txt", "number invalid"),
    ("test_inputs/test13.txt", "number invalid"),
    ("test_inputs/test14.txt", "number invalid"),
    ("test_inputs/test15.txt", "number invalid"),
    ("test_inputs/test16.txt", "number invalid"),
    ("test_inputs/test18.txt", "number invalid"),
    ("test_inputs/test19.txt", "number invalid")
])
def test_num2words(file_path, answer):
    n2w = Num2Words()
    assert n2w(file_path) == answer


@pytest.mark.parametrize("file_path, answer", [
    ("test_inputs", AssertionError),
    ("test_inputs/NOT_HERE.txt", AssertionError)
])
def test_num2words(file_path, answer):
    n2w = Num2Words()
    with pytest.raises(answer):
        n2w(file_path)


@pytest.mark.parametrize("input_string, answer", [
    ("The pump is 536 deep underground", "five hundred and thirty six"),
    ("We processed 9121 records.", "nine thousand, one hundred and twenty one"),
    ("Interactive and printable 10022 ZIP code.", "ten thousand and twenty "
                                                  "two"),
    ("The database has 66723107008 records.", "sixty six billion, seven "
                                              "hundred and twenty three "
                                              "million, one hundred and seven "
                                              "thousand and eight"),
    ("The speed of light is 299792458 meters per second",
     "two hundred and ninety nine million, seven hundred and ninety two "
     "thousand, four hundred and fifty eight"),
    ("In the year 681 things were different!", "six hundred and eighty one"),
    ("The company generated 136819 million USD in revenue this year",
     "one hundred and thirty six thousand, eight hundred and nineteen"),
    ("trying out whether a new line character 1234567890987654321\nhas an "
     "effect on recognizing the number",
     "one quintillion, two hundred and thirty four quadrillion, five hundred "
     "and sixty seven trillion, eight hundred and ninety billion, nine hundred "
     "and eighty seven million, six hundred and fifty four thousand, three "
     "hundred and twenty one"),
    ("Variables reported as having a missing type #65678", "number invalid"),
    ("I received 23 456,9 KGs.", "number invalid"),
    ("On average only 36% succeed", "number invalid"),
    ("Planck's constant is 6.62607004 x 10^-34 m^2 kg / s", "number invalid"),
    ("The speed of light is 299,792,458 meters per second", "number invalid"),
    ("The speed of light is 299 792 458 meters per second", "number invalid"),
    ("It is only 1/4th of an inch in length", "number invalid"),
    ("Use 0.25 kilos, please", "number invalid"),
    ("This is a test text file that does not contain numbers",
     "number invalid"),
    ("The car travelled 200 mile and it took 3 hours to get to the city.",
     "number invalid"),
    ("The temperature is -40 degrees Celsius.", "number invalid")
])
def test_num2words(input_string, answer):
    n2w = Num2Words()
    assert n2w.text_to_numeral(input_string) == answer
