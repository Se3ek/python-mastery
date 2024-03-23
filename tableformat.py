
def print_table(data, columns):
    lengths = {
        c: max([len(str(getattr(d, c))) for d in data] + [len(c)])+1 for c in columns
    }
    header = " ".join([f"{c:>{lengths[c]}}" for c in columns])
    sep = "".join([f"{'':->{lengths[c]+1}}" for c in columns])
    data = "\n".join([" ".join([f"{getattr(s, d):>{lengths[d]}}" for d in columns]) for s in data])
    print(header, sep, data, sep="\n")


if __name__ == "__main__":
    from stock import Stock
    portfolio = Stock.read_portfolio('Data/portfolio.csv')
    print_table(portfolio, ["name", "price", "shares"])
