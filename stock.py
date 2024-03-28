from __future__ import annotations

from csv import reader
from tableformat import print_table


class Stock:
    types = (str, int, float)

    def __init__(self, name: str, shares: int, price: float) -> None:
        self.name: str = name
        self.shares: int = shares
        self.price: float = price

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)

    def cost(self) -> float:
        return self.shares * self.price

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
        print_table(portfolio, ["name", "price", "shares"])


if __name__ == "__main__":
    port = Stock.read_portfolio("Data/portfolio.csv")
    Stock.print_portfolio(port)
