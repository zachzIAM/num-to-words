# -*- coding: utf-8 -*-
"""
The module contains a 'client' type class Num2Words used to interface with
input files on the system, extract numbers (positive integers to be specific)
and give an English numeral representation of the number identified.

The input files can contain no more than 1 positive integer value. Multiple
integers, negative integers, and non-integer numeric values will result in
the client detecting an invalid number.
"""
from pathlib import Path
from num2words import WordNumeral, input_handler, InvalidNumber


class Num2Words:
    """
    Client class intended to handle file inputs, extract positive integer
    values, store all inputs as well as the English numeral representation of
    the number into an object property.

    Once instantiated the object is callable with a file path as input which
    it in turn processes and returns the English numeral value of the int
    contained within the file.
    """
    # region Constructor
    def __init__(self, handler=input_handler):
        """
        Constructor for the Num2Words class. It requires a handler function
        which takes 1 str argument and returns 1 int. In case the input string
        does not contain a valid integer value to be returned (according to the
        logic defined in the function) it should raise an InvalidNumber
        exception. If a different exception is raised it will be re-thrown by
        the Num2Words.__call__ function.

        :param handler: input handler function
        :type handler: function
        """
        self._handler = handler
        self._word_numeral = WordNumeral()
    # endregion

    # region Caller
    def __call__(self, file):
        """
        Calling an instance of an object with a valid input file path makes the
        object read the file, extract an integer value, store inputs and
        English numeral form of the number detected. If no valid number is
        found 'number invalid' is returned. This operation alters the object.

        :param file: path to input_file
        :type file: str
        :return: English numeral representation of valid input number
        :rtype: str
        """
        f = Path(file)
        assert f.exists(), f"{file} does not exist"
        assert f.is_file(), f"{file} is not a file"

        self._file_path = file
        file_contents = f.read_text(encoding="utf-8")

        try:
            num = self._handler(file_contents)
            self._file_contents = file_contents
        except InvalidNumber:
            return "number invalid"
        except Exception:
            raise

        return self._word_numeral(num)
    # endregion

    # region Properties
    @property
    def file_contents(self):
        return self._file_contents

    @property
    def file_path(self):
        return self._file_path

    @property
    def num(self):
        return self._word_numeral.num

    @property
    def word_numeral(self):
        return self._word_numeral.numeral
    # endregion

    # region Methods
    def text_to_numeral(self, text):
        try:
            num = self._handler(text)
        except InvalidNumber:
            return "number invalid"
        except Exception:
            raise
        return self._word_numeral.to_numeral(num)
    # endregion

    # region Display Overrides
    def __repr__(self):
        return f"Num2Words({self.__dict__['_handler']})"

    def __str__(self):
        f = "{0:>{width}} :\t{1}"
        align = len("file_contents") + 2
        txt = [f.format("file path", self.file_path, width=align)]
        txt += [f.format("file_contents",
                         self.file_contents.replace("\n", " "), width=align)]
        txt += [f.format("num", self.num, width=align)]
        txt += [f.format("word_numeral", self.word_numeral, width=align)]
        return "\n".join(txt)
    # endregion
