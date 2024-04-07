from __future__ import annotations

import sys

from csv import reader

import tableformat
from tableformat import print_table, create_formatter


class Stock:
    __slots__ = ("_name", "_shares", "_price")
    _types = (str, int, float)

    def __init__(self, name: str, shares: int, price: float) -> None:
        self._name: str = name
        self._shares: int = shares
        self._price: float = price

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)

    @property
    def name(self) -> str:
        return self._name

    @property
    def cost(self) -> float:
        return self._shares * self._price

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value) -> None:
        if not isinstance(value, self._types[2]) or value < 0:
            raise ValueError("price must be a positive float")
        else:
            self._price = value

    @property
    def shares(self) -> int:
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, self._types[1]) or value < 0:
            raise ValueError("shares must be a positive int")

    def sell(self, nshares: int) -> None:
        """
        Sell the specified number of shares
        """
        self.shares -= nshares

    @classmethod
    def read_portfolio(cls, file_path: str) -> list[Stock]:
        """
        Read a portfolio from a csv file and return a list of stock objects
        """
        portfolio_list: list[Stock] = []
        with open(file_path, "r") as f:
            read = reader(f)
            header: list[str] = next(read)
            for line in read:
                portfolio_list.append(cls.from_row(line))

        return portfolio_list

    @classmethod
    def print_portfolio(cls, portfolio: list[Stock]) -> None:
        """
        Print a given portfolio in table format
        """
        from tableformat import create_formatter
        fmtr = create_formatter("text")
        print_table(portfolio, ["name", "price", "shares"], fmtr)

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"

    def __eq__(self, other):
        return isinstance(other, Stock) and ((self.name, self.shares, self.price) ==
                                             other.name, other.shares, other.price)


if __name__ == "__main__":
    port = Stock.read_portfolio("Data/portfolio.csv")
    Stock.print_portfolio(port)
    print(repr(port))
