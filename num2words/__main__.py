# -*- coding: utf-8 -*-
"""Entry point for the package"""
import argparse
from num2words import WordNumeral, Num2Words

parser = argparse.ArgumentParser(description="Process a file for numerals")
group = parser.add_mutually_exclusive_group()
group.add_argument('-f', type=str, help="path for the input file",
                   dest="file_path", nargs="?")
group.add_argument('-n', type=int, help="number to be parsed to numeral",
                   dest="number", nargs="?")
args = parser.parse_args()


def main():
    if args.number is None and args.file_path is None:
        parser.print_help()
        return 0
    elif args.number is not None:
        print(WordNumeral.to_numeral(args.number))
    elif args.file_path is not None:
        client = Num2Words()
        print(client(args.file_path))
    else:
        return 1


if __name__ == '__main__':
    main()
