# -*- coding: utf-8 -*-
"""
This module contains a Numeral class to encapsulate a positive integer and
provide representation for it in plain English numeral form.
"""

from num2words import NumberTooLarge

# region Module Variables

_SMALL_NUMS = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}
"""dict: numerals for numbers < 20 and multiples of 10"""

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
    9: "octillion",
    10: "nonillion",
    11: "decillion",
    12: "undecillion",
    13: "duodecillion",
    14: "tredecillion",
    15: "quattuordecillion",
    16: "quinquadecillion",
    17: "sexdecillion",
    18: "septendecillion",
    19: "octodecillion",
    20: "novemdecillion",
    21: "vigintillion",
    22: "unvigintillion",
    23: "duovigintillion",
    24: "tresvigintillion",
    25: "quattuorvigintillion",
    26: "quinquavigintillion",
    27: "sesvigintillion",
    28: "septemvigintillion",
    29: "octovigintillion",
    30: "novemvigintillion",
    31: "trigintillion",
    32: "untrigintillion",
    33: "duotrigintillion",
    34: "trestrigintillion",
    35: "quattuortrigintillion",
    36: "quinquatrigintillion",
    37: "sestrigintillion",
    38: "septentrigintillion",
    39: "octotrigintillion",
    40: "noventrigintillion",
    41: "quadragintillion",
    42: "unquadragintillion",
    43: "duoquadragintillion",
    44: "tresquadragintillion",
    45: "quattuorquadragintillion",
    46: "quinquaquadragintillion",
    47: "sesquadragintillion",
    48: "septenquadragintillion",
    49: "octoquadragintillion",
    50: "novenquadragintillion"
}
"""dict: significance units when dividing a number by 1000, e.g. thousand"""

# endregion


class WordNumeral:
    """This is a class for english numerals.

    It can be used to get a given integer's representation in plain English.
    The constructor requires a single positive integer value argument and
    returns an object with two read-only attributes
        - ``num`` representing the value passed in
        - ``numeral`` which is the English numeral equivalent of the number

    A class method ``to_numeral`` is exposed and can be used to convert any
    number to a numeral representation.

    Calling an instance of a object re-assigns the num and numeral properties
    to correspond to the ``num`` argument passed and returns the English
    numeral representation.
    """
    # region Constructor
    # TODO consider inheriting from int instead; will simplify the API as we
    #   won't have to override all of the basic operators
    def __init__(self, num=0):
        """Initialise a Numeral object

        :param num: positive number to be represented as a numeral
        :type num: int
        :return: An object of type Numeral representing the num input
        :rtype: Numeral
        """
        self._num = num
        self._numeral = self.to_numeral(num)
    # endregion

    # region Caller
    def __call__(self, num):
        self._num = num
        self._numeral = self.to_numeral(num)
        return self.numeral
    # endregion

    # region Properties
    @property
    def num(self):
        return self._num

    @property
    def numeral(self):
        return self._numeral
    # endregion

    # region Class Methods
    @classmethod
    def to_numeral(cls, num):
        """Class method which translates a positive integer to English numeral.

        It parses the number recursively ascending the value at 10^3 increments.
        The num argument is split into a quotient and remainder with divisor
        equal to 1000. The quotient is passed onto the recursive call along
        with an incremented significance level. The remainder gets parsed and
        appended and its significance numeral appended to it.

        :param num: positive integer to be converted to an English numeral
        :type num: int
        :return: English numeral representation of the number
        :rtype: str

        :example:

        >>> WordNumeral.to_numeral(1400)
        'one thousand four hundred'

        >>> WordNumeral.to_numeral(15025)
        'fifteen thousand and twenty five'

        >>> WordNumeral.to_numeral(337)
        'three hundred and thirty seven'

        >>> WordNumeral.to_numeral(563202086)
        'five hundred and sixty three million two hundred and two thousand and eighty six'
        """
        return " ".join(cls._parse_large(num, 0))

    @classmethod
    def _parse_small(cls, num):
        """Helper class method which parses numbers less than 1000

        :param num: positive number to convert
        :type num: int
        :return: English numeral representation of the number
        :rtype: list[str]
        """
        numeral = []

        h, r = divmod(num, 100)

        if h:
            numeral += [f'{_SMALL_NUMS[h]} hundred']

        if r and h:
            numeral += ['and']

        if r < 20:
            numeral += [_SMALL_NUMS[r]]
        else:
            numeral += [_SMALL_NUMS[(r // 10) * 10], _SMALL_NUMS[r % 10]]

        return numeral

    @classmethod
    def _parse_large(cls, num, sig):
        """Helper class method which handles parsing numbers into numerals

        This is the workhorse of the converter where large numbers are handled.
        It parses the number recursively ascending the value at 10^3 increments.
        The num argument is split into a quotient and remainder with divisor
        equal to 1000. The quotient is passed onto the recursive call along
        with an incremented significance level. The remainder gets parsed and
        appended and its significance numeral appended to it.

        :param num: positive number to convert
        :type num: int
        :param sig: current significance level
        :type sig: int
        :return: English numeral representation of the number
        :rtype: list[str]
        :raises: TypeError, ValueError, NumberTooLarge
        """
        if not isinstance(num, int):
            raise TypeError(f"'num' must be int, not {type(num)}")

        # TODO making this work with negative numbers is trivial
        if num < 0:
            raise ValueError(f"argument {num} is < 0; positive int expected")

        if sig > max(_SIG_UNITS.keys()):
            max_sig = _SIG_UNITS[max(_SIG_UNITS.keys())]
            raise NumberTooLarge(f"can only handle up to {max_sig}s")

        if num == 0 and sig == 0:
            return ["zero"]

        lrg, rem = divmod(num, 1000)

        if lrg == 0:
            numeral = [""]
        else:
            numeral = cls._parse_large(lrg, sig + 1)

        if (0 < rem < 100) and (sig == 0) and (lrg != 0):
            numeral += ["and"]
        elif lrg != 0 and ((sig > 0 and rem > 0) or (sig == 0 and rem >= 100)):
            numeral[-1] = numeral[-1] + ","

        if rem > 0:
            numeral += cls._parse_small(rem) + [_SIG_UNITS[sig]]

        return [x for x in numeral if x != ""]
    # endregion

    # region Display Overrides
    def __repr__(self):
        return f'Numeral({self.num})'

    def __str__(self):
        return self.numeral
    # endregion

    # region Logical Operator Overrides
    def __lt__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(f"must compare with another {type(self)}")
        return self.num < other.num

    def __le__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(f"must compare with another {type(self)}")
        return self.num <= other.num

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(f"must compare with another {type(self)}")
        return self.num == other.num

    def __ne__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(f"must compare with another {type(self)}")
        return self.num != other.num

    def __gt__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(f"must compare with another {type(self)}")
        return self.num > other.num

    def __ge__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(f"must compare with another {type(self)}")
        return self.num >= other.num
    # endregion

    # region Arithmetic Operator Overrides
    def __add__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(f"must compare with another {type(self)}")
        return WordNumeral(self.num + other.num)

    def __sub__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(f"must compare with another {type(self)}")
        return WordNumeral(self.num - other.num)

    def __mul__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(f"must compare with another {type(self)}")
        return WordNumeral(self.num * other.num)

    def __truediv__(self, other):
        raise NotImplementedError("cannot guarantee an integer. use // instead")

    def __floordiv__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(f"must compare with another {type(self)}")
        return WordNumeral(self.num // other.num)

    def __mod__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(f"must compare with another {type(self)}")
        return WordNumeral(self.num % other.num)

    def __divmod__(self, other):
        return self.__floordiv__(other), self.__mod__(other)

    def __pow__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(f"must compare with another {type(self)}")
        return WordNumeral(self.num**other.num)

    def __lshift__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(f"must compare with another {type(self)}")
        return WordNumeral(self.num << other.num)

    def __rshift__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(f"must compare with another {type(self)}")
        return WordNumeral(self.num >> other.num)

    def __and__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(f"must compare with another {type(self)}")
        return WordNumeral(self.num & other.num)

    def __or__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(f"must compare with another {type(self)}")
        return WordNumeral(self.num | other.num)

    def __xor__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(f"must compare with another {type(self)}")
        return WordNumeral(self.num ^ other.num)
    # endregion

