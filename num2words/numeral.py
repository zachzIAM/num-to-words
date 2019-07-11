# -*- coding: utf-8 -*-
"""
Parse the number in thousands.

Will need a dictionary of significance, e.g.

{
    1: "thousand",
    2: "million",
    3: "billion",
    4: "trillion",
    ...
}

Use typing for parsing function to ensure that an integer is passed.


The function should probably be internal / hidden and take 2 arguments - num and sig -  e.g. _parse_int(num, sig)
It can be recursive returns a string (or an array of strings?)
    First we check if the number is 0, and if so return empty string

    Then we call the function (recursively) passing num // 1000 and sig + 1.

    Then parse the remainder - num % 1000 - and join to the corresponding significance dictionary value, e.g. thousand
        When parsing the remainder we need to add an 'and' between the hundreds and tens if the number
        is > 100. By design this number will always be < 1000.
        Additionally, if the number < 100, sig == 0 and the recursive call returns
        a non-empty string we should have an 'and' preceding the number words.

    This logic should lead to the following outcomes:
        1100 - one thousand one hundred (and not one thousand and one hundred)
        1025 - one thousand and twenty five
        137  - one hundred and thirty seven
        106  - one hundred and six

"""

_SIG_UNITS = {
    0: "",
    1: "thousand",
    2: "million",
    3: "billion",
    4: "trillion",
    5: "quadrillion",
    6: "quintillion",
    7: "sextillion",
    8: "septillion",
    9: "octillion"

}
"""dict: significance units when dividing a number by 1000, e.g. thousand"""


class Numeral:
    """This is a class for english numerals.

    It can be used to get a given integer's representation in plain English.
    """

    def __init__(self, num):
        """Initialise a Numeral

        :param num: positive number to be represented as a numeral
        :type num: int
        """
        assert isinstance(num, int)
        assert num > 0
        self.num = num
        self.numeral = self.to_numeral(num)

    @classmethod
    def to_numeral(cls, num):
        """Class method which parses a positive integer and returns its English
        numeral. It can be used both from an instance and from the class itself

        :param num: positive integer to be converted to an English numeral
        :type num: int
        :return:
        """
        return "some text"

    @classmethod
    def __parse_small(cls, num):
        """Helper class method which parses numbers less than 1000

        :param num: positive integer less than 1000
        :type num: int
        :return:
        """
        pass

    @classmethod
    def __parse_large(cls, num, sig):
        """Helper class method which handles parsing numbers into numerals

        This is the workhorse of the converter

        :param num:
        :param sig:
        :return:
        """
        pass

    def __repr__(self):
        return f'Numeral({self.num})'

    def __str__(self):
        return self.numeral

    def __lt__(self, other):
        assert isinstance(other, Numeral)
        return self.num < other.num

    def __le__(self, other):
        assert isinstance(other, Numeral)
        return self.num <= other.num

    def __eq__(self, other):
        assert isinstance(other, Numeral)
        return self.num == other.num

    def __ne__(self, other):
        assert isinstance(other, Numeral)
        return self.num != other.num

    def __gt__(self, other):
        assert isinstance(other, Numeral)
        return self.num > other.num

    def __ge__(self, other):
        assert isinstance(other, Numeral)
        return self.num >= other.num

