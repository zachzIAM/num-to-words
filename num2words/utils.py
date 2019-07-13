# -*- coding: utf-8 -*-


class Error(Exception):
    """Base class for other errors"""
    pass


class NumberTooLarge(Error):
    """Raises an error when the input number is too large"""
    pass


class InvalidNumber(Error):
    """Raises an error when the input string does not contain a valid number"""
    pass


def input_handler(input_string: str) -> int:
    """This utility takes a single piece of text, e.g. a sentence and looks
    for numeric values embedded in it. The expectation is that there is a max
    of one numeric value per input string. Additionally the number must be an
    integer and it must be made up of numeric characters only, i.e. no commas
    fullstops or spaces to denote decimals or thousands, millions, etc.

    :param input_string: text to search for a numeric value.
    :return: the number detected in the string
    :raise: InvalidNumber
    :example:

    >>> input_handler("The pump is 536 deep underground")
    536

    >>> input_handler("We processed 9121 records.")
    9121

    >>> input_handler("Variables reported as having a missing type #65678")
    InvalidNumber: ...

    >>> input_handler("Interactive and printable 10022 ZIP code.")
    10022

    >>> input_handler("The database has 66723107008 records.")
    66723107008

    >>> input_handler("I received 23 456,9 KGs.")
    InvalidNumber: ...
    """
    words = input_string.split()
    with_digits = [w for w in words if any(map(str.isdigit, list(w)))]
    numeric = [w for w in with_digits if w.isnumeric()]

    if len(numeric) != 1 or len(with_digits) != 1:
        raise InvalidNumber("none or multiple numeric words founds")

    num = int([w for w in with_digits if w.isnumeric()].pop())
    return num
