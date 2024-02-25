
from __future__ import annotations

from csv import reader


class Stock:
    def __init__(self, name: str, shares: int, price: float) -> None:
        self.name: str = name
        self.shares: int = shares
        self.price: float = price

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
                portfolio_list.append(cls(
                    line[header.index("name")],
                    int(line[header.index("shares")]),
                    float(line[header.index("price")])
                ))

        return portfolio_list

    @classmethod
    def print_portfolio(cls, portfolio: list[Stock]) -> None:
        """
        Print a given portfolio in table format
        """
        header = f"""{"name":>5} {"shares":>8} {"price":>10}\n"""
        data = "\n".join([f"""{s.name:>5} {s.shares:>8} {s.price:>10.2f}""" for s in portfolio])
        print(header + data)


if __name__ == "__main__":
    port = Stock.read_portfolio("Data/portfolio.csv")
    Stock.print_portfolio(port)