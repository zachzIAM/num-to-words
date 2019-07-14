# Num2Words 
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.6-blue.svg)

Convert a number to words. The goal of this repo is to provide a simple 
interface allowing users to convert an integer into its plain English numeral
form. 

This is an exercise based on the [instructions.pdf](instructions.pdf) included
in this repo.

## Getting Started
### Installation
#### Just the package
You can get started quickly by installing the package straight from Github:

```python
pip install git+https://github.com/zachzIAM/num-to-words.git@master
```

In case the above command is failing, please try using the `--user` flag to 
avoid user-level permissions issues.

```python
pip install --user git+https://github.com/zachzIAM/num-to-words.git@master
```

#### Clone the repo
You can also grab the package by cloning the repo and playing and exploring the
modules directly. Cloning the repo would let you install the package using 
setup-tools too. You can navigate to the root of the cloned repo via terminal /
CMD and run:

```python
pip install -e .
```

#### Running the tests
If you do clone the repo you may want to create a new virtual environment for 
the repo and install `pytest` in it. `pytest` can then be run on the entire 
**tests** folder. Navigate to the root of the repository and run:

```python
python -m pytest tests/
```

## Usage
### Command line tool
Once installed the package exposes a CLI utility called `num2words`.
Usage help can be obtained by running:
```python
num2words --help
``` 

`num2words` has two possible mutually exclusive flags, `-n` and `-f`, which
correspond to operating on a file and operating on an integer passed via the
command line. 

#### Parsing `int`s
Setting the `-n` flag primes the utility for work with integers. Here are some
example calls:

```bash
num2words -n 1
num2words -n 12
num2words -n 600
num2words -n 456
num2words -n 123456
num2words -n 198745665132684
num2words -n 8641563128941534135183451587453354586453141
```

Each of these calls will output to terminal the English numeral form of the 
argument.

#### Parsing files
The utility can also work with text file input. Certain rules / assumptions 
apply:

* the file must contain text rather than binary data
* only positive integer values embedded in the text will be captured; decimals
percentages, fractions, big marks, hex values prepended by `#`, scientific 
notation, etc. will all yield an **invalid input** response
* only one numeric value must be present in the input otherwise it will be 
detected as invalid, e.g. cannot have a valid integer and also a decimal 
somewhere else in the same text

Using `num2words` on files is as follows:
```bash
num2words -f ./tests/test_inputs/test1.txt
num2words -f ./tests/test_inputs/test17.txt
num2words -f ./tests/test_inputs/test18.txt
```

### Package
There are two classes the package exposes.

```python
from num2words import WordNumeral, Num2Words
```

#### The `WordNumeral` class 
It handles the conversion from a positive `int` into a plain English numeral. 
Creating a new instance of the object requires a positive integer as input:

```python
# create object
n = WordNumeral(456123)

# print will display the English numeral form
print(n)

# properties
n.num                                       # original number
n.numeral                                   # numeral form

# class method - can be called directly from the class
n.to_numeral(9876543210)                    # from class instance
WordNumeral.to_numeral(9876543210)          # directly from class

# instances are callable but calls modify them
print(n.num, ":\t", n.numeral)              # before call
n(123)                                      # call
print(n.num, ":\t", n.numeral)              # after call

# comparison operations
n2 = WordNumeral(15)
n2 >= n
n2 == n
n2 < n
n2 != n

# binary operators
print(n + n2)
print(n - n2)                               # if negative error will be thrown
print(n * n2)
print(n // n2)                              # '/' gives floats so not available
print(n % n2)
print(n % n2)
print(n ** n2)
print(n << n2)                              # left bit-shift operator
print(n >> n2)                              # right bit-shift operator
print(n & n2)                               # bitwise and
print(n | n2)                               # bitwise or
print(n ^ n2)                               # bitwise xor
```

**NOTE! Extended Assignments or Unary operators are currently not implemented!**

#### the `Num2Words` class 
This is a **client** class which is composed of 

* a `WordNumeral` instance stored as a property called `word_numeral`
* a text `handler` function which takes a string and returns a single integer 
value extracted from the input

To create an instance of this object the constructor can be called as usual and
takes an optional custom text `handler` function. This package has a simple 
default function which can be replaced with custom one of more sophisticated 
behaviour. It is important that any custom definition of the `handler` function

* takes a single argument of type `str`
* returns a single object of type `int`
* if a valid int value to be returned cannot be detected, an 
`InvalidNumber` (accessible from `num2words` module) exception must be raised 
in order to be properly handled by the `Num2Words` class.


Any instance is callable and the implemented behaviour is modifying. When called
a `file` path argument is required and things happen as follows:

1. contents of the file are are read
2. `handler` attempts to extract a valid number from contents
3. the `word_numeral` object is called with the extracted number
4. file path, file contents, handler, word numeral with it's new properties are 
all stored in the client object

```python
# create an instance
client = Num2Words()                            # using default handler
client("./tests/test_inputs/test1.txt")

# print object
client                                          # representation of object
print(client)                                   # custom print method

# properties
client.num
client.word_numeral
client.file_path
client.file_contents

# instances are callable but calls modify them
print(client)
client("./tests/test_inputs/test17.txt")
print(client)

# use instance method for non-modifying behaviour
sample_input = "In the year 900 BC an important event took place."
client.text_to_numeral(sample_input)
```

## Outline of approach
In order to parse an integer into English numerals we need to recognise that 
humans do this by reading the number in increments of ![inc][increment] - 
thousands, millions, billions, trillions, quadrillions, etc. As we ascend the 
value parsing the ![n][n]-th increment the rules for converting the number to a
numeral do not change, e.g thousands range from 1 to 999, so do millions, 
billions, etc. 

This type of problem lends itself very nicely to recursion. The problem can be 
reduced to the following algorithm:

1. start from the right with significance level 0 (i.e. less than a thousand)
2. obtain the quotient and remainder for the number when divided by 1000
3. if the quotient > 0
    1. call function recursively with quotient and significance level 
    incremented by 1
    2. otherwise treat as empty string
4. if remainder > 0
    1. **convert to words** and **append significance name**
    2. otherwise treat as empty string
5. append return value of recursive call to return value of remainder 
conversion and return the combined value


![parse-algorithm][parse-algorithm]


As the recursion goes deeper we ascend the value until there is no large number
to process. As the recursion unwinds we obtain the remainder word numeral for
the highest significance first appending it to the significance name and to the
the next significance decrement result down. The recursion unwinds completely 
when the remainder conversion with significance level 0 occurs. 

Two helper dictionaries have been set up:

* `_SIG_UNITS` to convert the significance levels to words; and
* `_SMALL_NUMS` to convert numbers < 1000 to words


## TODO
### Subclassing `int`
The API for WordNumeral can be simplified of the class inherits from int. We
will lose some niceties like `__init__` because int is immutable, but it is 
worth forgoing this for the benefit of not having to override every logical
and arithmetic operator.

**NOTE! Only Comparison and Binary Operators are currently implemented. As
there is a significant number of [them][magic-methods] to implement** we have
even more incentive to extend `int` rather than build a class around it. 

### Allowing negative integers
It may also be conceptually cleaner if we allowed for negative integers to be 
valid input for the `WordNumeral` objects. Not to mention that it is trivial
to achieve this. The task of capturing and extracting the negative number from
a body of text is trickier.

### Sphinx documentation
Although best effort has been put into populating all docstrings as a form of
documentation, if the package is to be used extensively it may warrant proper 
documentation using [Sphinx][sphinx-getting-started] and 
[ReadTheDocs][read-the-docs].

### Even larger numbers
Currently the program can handle numbers as large as ![largest][largest] but no
larger. I am not certain about the incremental value of this but the 
significance (thousand, million, billion, etc.) words can be abstracted further 
past decillion (![decillion][decillion]) as there is a pattern to how they are 
composed - [Extensions of the standard dictionary numbers][number-extensions]. 
This logic can be implemented fairly easily by altering the significance 
dictionary to include the component unit names.

### CI / CD
It would be great to automate building, testing and releasing of the package
using tools like [Travis][travis], [Codecov][codecov], etc. This will 
significantly improve future development and maintenance. 

[sphinx-getting-started]: https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html
[read-the-docs]: https://docs.readthedocs.io/en/stable/features.html
[magic-methods]: https://www.python-course.eu/python3_magic_methods.php
[increment]: http://latex.codecogs.com/gif.latex?10^3
[n]: http://latex.codecogs.com/gif.latex?n
[largest]: http://latex.codecogs.com/gif.latex?10^153-1
[decillion]: http://latex.codecogs.com/gif.latex?10^33
[number-extensions]: https://en.wikipedia.org/wiki/Names_of_large_numbers#Extensions_of_the_standard_dictionary_numbers
[travis]: https://travis-ci.org/
[codecov]: https://codecov.io/
[parse-algorithm]: https://media.giphy.com/media/KectTqjqKOwwsIWYO1/giphy.gif