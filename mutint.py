# mutint.py
from __future__ import annotations

from functools import total_ordering


@total_ordering
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        """
        Return a stringified object
        """
        return str(self.value)

    def __repr__(self) -> str:
        """
        Return the object's representation
        """
        return f'MutInt({self.value!r})'

    def __format__(self, fmt) -> str:
        """
        Format the value according to the input
        """
        return format(self.value, fmt)

    def __add__(self, other) -> MutInt:
        """
        Adding MutInts or regular ints
        """
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else:
            return NotImplemented

    __radd__ = __add__  # Reverse adding

    def __iadd__(self, other) -> MutInt:
        """
        In place adding (+=)
        """
        return self.__add__(other)

    def __eq__(self, other) -> bool:
        """
        Check for equality between MutInt and MutInt or int
        """
        if isinstance(other, MutInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented

    def __lt__(self, other) -> bool:
        """
        Check for less than given other
        """
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented

    def __gt__(self, other) -> bool:
        """
        Check for greater than
        """
        return not self.__lt__(other)

    def __int__(self) -> int:
        """
        Convert to int
        """
        return self.value

    def __float__(self) -> float:
        """
        Convert to float
        """
        return float(self.value)

    __index__ = __int__  # Give index function integer value
