import pytest
from random import randint
from num2words import WordNumeral, NumberTooLarge


@pytest.mark.parametrize("num, answer", [
    (1, "one"), (2, "two"), (3, "three"), (4, "four"), (5, "five"), (6, "six"),
    (7, "seven"), (8, "eight"), (9, "nine"), (10, "ten"), (11, "eleven"),
    (12, "twelve"), (13, "thirteen"), (14, "fourteen"), (15, "fifteen"),
    (16, "sixteen"), (17, "seventeen"), (18, "eighteen"), (19, "nineteen"),
    (20, "twenty"), (21, "twenty one"), (30, "thirty"), (32, "thirty two"),
    (40, "forty"), (43, "forty three"), (50, "fifty"), (54, "fifty four"),
    (60, "sixty"), (65, "sixty five"), (70, "seventy"), (76, "seventy six"),
    (80, "eighty"), (87, "eighty seven"), (90, "ninety"), (98, "ninety eight"),
    (100, "one hundred"), (101, "one hundred and one"),
    (113, "one hundred and thirteen"), (140, "one hundred and forty"),
    (168, "one hundred and sixty eight"), (634, "six hundred and thirty four"),
    (3000, "three thousand"), (4006, "four thousand and six"),
    (5011, "five thousand and eleven"), (6100, "six thousand, one hundred"),
    (8207, "eight thousand, two hundred and seven"),
    (10312, "ten thousand, three hundred and twelve"),
    (16003, "sixteen thousand and three"),
    (46950, "forty six thousand, nine hundred and fifty"),
    (101003, "one hundred and one thousand and three"),
    (513647, "five hundred and thirteen thousand, six hundred and forty seven"),
    (1000006, "one million and six"),
    (11000048, "eleven million and forty eight"),
    (22000350, "twenty two million, three hundred and fifty"),
    (101003006, "one hundred and one million, three thousand and six"),
    (318028059, "three hundred and eighteen million, twenty eight thousand and "
                "fifty nine"),
    (630555633, "six hundred and thirty million, five hundred and fifty five "
                "thousand, six hundred and thirty three"),
    (3000000000, "three billion"),
    (10036666573, "ten billion, thirty six million, six hundred and sixty six "
                  "thousand, five hundred and seventy three"),
    (123456789123, "one hundred and twenty three billion, four hundred and "
                   "fifty six million, seven hundred and eighty nine thousand, "
                   "one hundred and twenty three"),
    (700000000000, "seven hundred billion"),
    (40000000000004, "forty trillion and four"),
    (650321654987312, "six hundred and fifty trillion, three hundred and "
                      "twenty one billion, six hundred and fifty four million, "
                      "nine hundred and eighty seven thousand, three hundred "
                      "and twelve"),
    (398525558734094299496535528255714668113128660339400468162519894880769612043962312675511368364999419156244693054935773660625717798991457689614863028491901,
     'three hundred and ninety eight novenquadragintillion, five hundred and '
     'twenty five octoquadragintillion, five hundred and fifty eight '
     'septenquadragintillion, seven hundred and thirty four '
     'sesquadragintillion, ninety four quinquaquadragintillion, two hundred '
     'and ninety nine quattuorquadragintillion, four hundred and ninety six '
     'tresquadragintillion, five hundred and thirty five duoquadragintillion, '
     'five hundred and twenty eight unquadragintillion, two hundred and fifty '
     'five quadragintillion, seven hundred and fourteen noventrigintillion, '
     'six hundred and sixty eight octotrigintillion, one hundred and thirteen '
     'septentrigintillion, one hundred and twenty eight sestrigintillion, six '
     'hundred and sixty quinquatrigintillion, three hundred and thirty nine '
     'quattuortrigintillion, four hundred trestrigintillion, four hundred and '
     'sixty eight duotrigintillion, one hundred and sixty two untrigintillion, '
     'five hundred and nineteen trigintillion, eight hundred and ninety four '
     'novemvigintillion, eight hundred and eighty octovigintillion, seven '
     'hundred and sixty nine septemvigintillion, six hundred and twelve '
     'sesvigintillion, forty three quinquavigintillion, nine hundred and sixty '
     'two quattuorvigintillion, three hundred and twelve tresvigintillion, six '
     'hundred and seventy five duovigintillion, five hundred and eleven '
     'unvigintillion, three hundred and sixty eight vigintillion, three '
     'hundred and sixty four novemdecillion, nine hundred and ninety nine '
     'octodecillion, four hundred and nineteen septen-decillion, one hundred '
     'and fifty six sexdecillion, two hundred and forty four quinquadecillion, '
     'six hundred and ninety three quattuordecillion, fifty four tredecillion, '
     'nine hundred and thirty five duodecillion, seven hundred and seventy '
     'three undecillion, six hundred and sixty decillion, six hundred and '
     'twenty five nonillion, seven hundred and seventeen octillion, seven '
     'hundred and ninety eight septillion, nine hundred and ninety one '
     'sextillion, four hundred and fifty seven quintillion, six hundred and '
     'eighty nine quadrillion, six hundred and fourteen trillion, eight '
     'hundred and sixty three billion, twenty eight million, four hundred '
     'and ninety one thousand, nine hundred and one')
])
def test_to_numeral(num, answer):
    assert WordNumeral.to_numeral(num) == answer


@pytest.mark.parametrize("num, answer", [
    (0.5, TypeError), (-136, ValueError), (-0.7, TypeError),
    ("test", TypeError), (10**153, NumberTooLarge),
    (randint(10**153, 10**154), NumberTooLarge),
    (randint(10**153, 10**160), NumberTooLarge)
])
def test_to_numeral_error(num, answer):
    with pytest.raises(answer):
        WordNumeral.to_numeral(num)
