import unittest
from int_joukko import IntJoukko


def main():
    joukko = IntJoukko()

    joukko.lisaa(1)
    joukko.lisaa(2)
    joukko.lisaa(3)
    joukko.lisaa(2)
    joukko.lisaa(7)
    joukko.lisaa(9)
    joukko.poista(1)

    print(joukko.to_int_list())


if __name__ == "__main__":
    main()
