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
