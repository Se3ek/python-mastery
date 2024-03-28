class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()

    def row(self, rowdata):
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-' * 10 + ' ') * len(headers))

    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))


class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join([str(d) for d in rowdata]))


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        string = f"<tr> <th>{'</th> <th>'.join(headers)}</th> </tr>"
        print(string)

    def row(self, rowdata):
        string = f"<tr> <td>{'</td> <td>'.join([str(d) for d in rowdata])}</td> </tr>"
        print(string)


def print_table(data, columns, formattr: TableFormatter):
    formattr.headings(columns)
    for r in data:
        rowdata = [getattr(r, fieldname) for fieldname in columns]
        formattr.row(rowdata)


def create_formatter(form):
    mapping = {
        "text": TextTableFormatter,
        "html": HTMLTableFormatter,
        "csv": CSVTableFormatter
    }

    return mapping[form]()


if __name__ == "__main__":
    from stock import Stock

    portfolio = Stock.read_portfolio('Data/portfolio.csv')

    text_formatter = create_formatter("text")
    csv_formatter = create_formatter("csv")
    html_formatter = create_formatter("html")

    print_table(portfolio, ["name", "shares", "price"], text_formatter)
    print_table(portfolio, ["name", "shares", "price"], csv_formatter)
    print_table(portfolio, ["name", "shares", "price"], html_formatter)

