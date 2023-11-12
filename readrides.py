import csv, tracemalloc, os, typing

FILE_PATH = os.path.join("Data", "ctabus.csv")

def read_as_tuple() -> tuple[str, str, str, int]:
    """
    Read the file and return the data as a tuple
    """
    with open(FILE_PATH, "r") as f:
        rows = csv.reader(f)
        headings = next(rows)
        row = next(rows)
        data = (row[0], row[1], row[2], int(row[3]))
    return data

def read_as_dict() -> dict[str, str, str, int]:
    """
    Read the file and return the data as a dictionary
    """
    data = dict()
    with open(FILE_PATH, "r") as f:
        rows = csv.reader(f)
        headings = next(rows)
        row = next(rows)
        data["route"] = row[0]
        data["date"] = row[1]
        data["daytype"] = row[2]
        data["rides"] = int(row[3])
    return data

class ride_record:
    def __init__(self, route: str, date: str, daytype: str, rides: int):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

def read_as_class() -> ride_record:
    """
    Read the file and return the data as a record object
    """
    with open(FILE_PATH, "r") as f:
        rows = csv.reader(f)
        headings = next(rows)
        row = next(rows)
        data = ride_record(row[0], row[1], row[2], int(row[3]))
    return data

class nt_record(typing.NamedTuple):
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
        headings = next(rows)
        row = next(rows)
        nt = nt_record(row[0], row[1], row[2], int(row[3]))
    return nt

class ride_slots:
    __slots__ = ["route", "date", "daytype", "rides"]
    def __init__(self, route: str, date: str, daytype: str, rides: int):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

def record_with_slots() -> ride_slots:
    """
    Ride the file and return the data as a class with slots
    """
    with open(FILE_PATH, "r") as f:
        rows = csv.reader(f)
        headings = next(rows)
        row = next(rows)
        slts = nt_record(row[0], row[1], row[2], int(row[3]))
    return slts

if __name__ == "__main__":
    mem_data = dict()
    # Representation as a tuple:
    tracemalloc.start()
    tup = read_as_tuple()
    mem_data["Tuple"] = tracemalloc.get_traced_memory()
    tracemalloc.stop

    # Representation as a dictionary
    tracemalloc.start()
    dic = read_as_dict()
    mem_data["Dictionary"] = tracemalloc.get_traced_memory()
    tracemalloc.stop

    # Representation as a class
    tracemalloc.start()
    cls = read_as_class()
    mem_data["Class"] = tracemalloc.get_traced_memory()
    tracemalloc.stop

    # Representation as a named tuple
    tracemalloc.start()
    ntup = named_tuples()
    mem_data["Named tuple"] = tracemalloc.get_traced_memory()
    tracemalloc.stop

    # Representation as a class with slots
    tracemalloc.start()
    slots = record_with_slots()
    mem_data["Class with slots"] = tracemalloc.get_traced_memory()
    tracemalloc.stop

    # Print the results
    sorted_dict = dict(sorted(mem_data.items(), key=lambda item: item[1]))
    for k, v in sorted_dict.items():
        print(f"{k}: {v}")
