import csv
import os
import tracemalloc
import typing

FILE_PATH = os.path.join("Data", "ctabus.csv")


def read_as_tuple() -> tuple[str, str, str, int]:
    """
    Read the file and return the data as a tuple
    """
    with open(FILE_PATH, "r") as f:
        rows = csv.reader(f)
        next(rows)  # remove headings
        row = next(rows)
        data = (row[0], row[1], row[2], int(row[3]))
    return data


def read_as_dict(linenum: int = 0) -> list[dict[str, str | int]]:
    """
    Read the file and return the data as a dictionary
    """
    linenum += 1    # Add 1 to counter since we'll be skipping the header
    results = list()
    with open(FILE_PATH, "r") as f:
        rows = csv.reader(f)
        next(rows)  # remove headings
        for row in rows:
            data = dict()
            data["route"] = row[0]
            data["date"] = row[1]
            data["daytype"] = row[2]
            data["rides"] = int(row[3])
            results.append(data)
            # Stop iterating if line number from input is reached unless all lines are called for
            if linenum != 1 and rows.line_num >= linenum:
                break
    return results


class RideRecord:
    def __init__(self, route: str, date: str, daytype: str, rides: int):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


def read_as_class() -> RideRecord:
    """
    Read the file and return the data as a record object
    """
    with open(FILE_PATH, "r") as f:
        rows = csv.reader(f)
        next(rows)  # remove headings
        row = next(rows)
        data = RideRecord(row[0], row[1], row[2], int(row[3]))
    return data


class NtRecord(typing.NamedTuple):
    route: str
    date: str
    daytype: str
    rides: int


def named_tuples() -> typing.NamedTuple:
    """
    Read the file and return the data as a named tuple
    """
    with open(FILE_PATH, "r") as f:
        rows = csv.reader(f)
        next(rows)  # remove headings
        row = next(rows)
        nt = NtRecord(row[0], row[1], row[2], int(row[3]))
    return nt


class RideSlots:
    __slots__ = ["route", "date", "daytype", "rides"]

    def __init__(self, route: str, date: str, daytype: str, rides: int):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


def record_with_slots() -> NtRecord:
    """
    Ride the file and return the data as a class with slots
    """
    with open(FILE_PATH, "r") as f:
        rows = csv.reader(f)
        next(rows)  # remove headings
        row = next(rows)
        slts = NtRecord(row[0], row[1], row[2], int(row[3]))
    return slts


if __name__ == "__main__":
    mem_data = dict()
    # Representation as a tuple:
    tracemalloc.start()
    tup = read_as_tuple()
    mem_data["Tuple"] = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Representation as a dictionary
    tracemalloc.start()
    dic = read_as_dict(1)[0]    # Returns a tuple, list so have one entry made and select it
    mem_data["Dictionary"] = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Representation as a class
    tracemalloc.start()
    cls = read_as_class()
    mem_data["Class"] = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Representation as a named tuple
    tracemalloc.start()
    ntup = named_tuples()
    mem_data["Named tuple"] = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Representation as a class with slots
    tracemalloc.start()
    slots = record_with_slots()
    mem_data["Class with slots"] = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Print the results
    sorted_dict = dict(sorted(mem_data.items(), key=lambda item: item[1]))
    for k, v in sorted_dict.items():
        print(f"{k}: {v}")
