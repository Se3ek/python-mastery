from os import path

# Constants
FILE_PATH = path.join("Data", "portfolio3.dat")


def read_data(path) -> dict[str, tuple[float, float]]:
    """
    Read data from the file and return as dict containing tuple of number and price
    """
    data = dict()
    errors = list()

    # Reading loop
    with open(path, "r") as f:
        for line in f:
            info = line.split()

            try:
                data[info[0]] = (float(info[1]), float(info[2]))
            except ValueError:
                errors.append(line)

    if errors:
        error_string = ''.join(errors)
        print(f"WARNING - The following line could not be parsed:\n{error_string}")

    return data


def calc_total(data: dict[str, tuple[float, float]]) -> float:
    """
    Take a dictionary of items with (number, price) tuples und calculate the overall total
    """

    return sum([v[0] * v[1] for v in data.values()])


def portfolio_cost(path: str) -> None:
    """
    Take in a path as string and print the total portfolio cost
    """
    data = read_data(path)
    total = calc_total(data)
    print(f"Total portfolio cost: {total}")


if __name__ == "__main__":
    total = calc_total(read_data(FILE_PATH))
    print(f"Total portfolio cost: {total}")
