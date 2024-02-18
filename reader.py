# reader.py
from __future__ import annotations

import csv
import tracemalloc
import time

from sys import intern
from typing import overload


INPUT_PATH = "Data/ctabus.csv"


def read_csv_as_dicts(input_path: str, types: list) -> list[dict]:
    """
    read a csv file and return it as a list of dicts
    """
    output: list = []
    with open(input_path, "r") as f:
        reader = csv.reader(f)
        headers = next(reader)
        for row in reader:
            output.append(
                {name: func(val) for name, func, val in zip(headers, types, row)}
            )

    return output


class DataCollection:
    """
        Stores any data from a csv file with specified data types
        """

    def __init__(self, input_path: str = None, types: list = None, **kwargs):

        if not input_path:
            # For manual data creation
            self._data = kwargs["_data"]
            self.headers = kwargs["_headers"]
            self._width = len(self.headers)
            return

        # Save the types list
        self.types = types

        # Get the data from the file
        with open(input_path, "r") as f:
            reader = csv.reader(f)
            self.headers = next(reader)  # Save the headers for keeping to keep the order for reference
            self._width = len(self.headers)  # Save how many columns there are
            if not self.types:
                # If no types were specified, everything will be strings
                self.types = [str for _ in range(self._width)]
            self._data = {head: [] for head in self.headers}  # Create the base dict with empty lists
            for row in reader:
                for i in range(self._width):
                    self._data[self.headers[i]].append(self.types[i](row[i]))

    def __len__(self):
        return self._width

    @overload
    def __getitem__(self, item: int) -> dict:
        ...

    @overload
    def __getitem__(self, item: slice) -> DataCollection:
        ...

    def __getitem__(self, item):
        if isinstance(item, int):
            return {
                h: self._data[h][item] for h in self.headers
            }
        if isinstance(item, slice):
            return DataCollection(
                _headers=self.headers,
                _data={
                    head: self._data[head][item] for head in self.headers
                }
            )

    def append(self, record: dict | list[dict]):
        """
        Add information to the data manually
        """
        if isinstance(record, dict):
            for k in record.keys():
                self._data[k].append(record[k])
        if isinstance(record, list):
            for i in record:
                for k in i.keys():
                    self._data[k].append(record[k])


def read_csv_as_columns(input_path: str, types: list = None) -> DataCollection:
    """
    Reads a csv file and saves it as columns but returns it as a DataCollection object
    """
    return DataCollection(input_path, types)


def test_memory_caching():
    """
    Test memory usages
    """
    # No caching
    no_cache_time = time.time()
    tracemalloc.start()
    no_cache = read_csv_as_dicts(INPUT_PATH, [str, str, str, int])
    no_cache_score = max(tracemalloc.get_traced_memory())
    tracemalloc.stop()
    no_cache_time = time.time() - no_cache_time

    # One cached input
    one_cache_time = time.time()
    tracemalloc.start()
    one_cache = read_csv_as_dicts(INPUT_PATH, [intern, str, str, int])
    one_cache_score = max(tracemalloc.get_traced_memory())
    tracemalloc.stop()
    one_cache_time = time.time() - one_cache_time

    # Two cached inputs
    two_cache_time = time.time()
    tracemalloc.start()
    two_cache = read_csv_as_dicts(INPUT_PATH, [intern, intern, str, int])
    two_cache_score = max(tracemalloc.get_traced_memory())
    tracemalloc.stop()
    two_cache_time = time.time() - two_cache_time

    # Three cached inputs
    three_cache_time = time.time()
    tracemalloc.start()
    three_cache = read_csv_as_dicts(INPUT_PATH, [intern, intern, intern, int])
    three_cache_score = max(tracemalloc.get_traced_memory())
    tracemalloc.stop()
    three_cache_time = time.time() - three_cache_time

    # Display results
    print(
        f"{no_cache_score = :,} in {no_cache_time:.3} s"
        f"\n{one_cache_score = :,} in {one_cache_time:.3} s"
        f"\n{two_cache_score = :,} in {two_cache_time:.3} s"
        f"\n{three_cache_score = :,} in {three_cache_time:.3} s"
    )


if __name__ == "__main__":
    test_memory_caching()
