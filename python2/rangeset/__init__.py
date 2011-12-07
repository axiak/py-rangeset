"""
Range of time stuff
"""

import bisect
import collections

class _Infinity(object):
    def __cmp__(self, other):
        return 0 if other is self else 1
    def __str__(self):
        return 'inf'

class _NegativeInfinity(object):
    def __cmp__(self, other):
        return 0 if other is self else -1
    def __str__(self):
        return '-inf'


INFINITY = _Infinity()
NEGATIVE_INFINITY = _NegativeInfinity()

class RangeSet(object):
    def __init__(self, start, end):
        if start > end:
            start, end = end, start
        self.__ends = [(start, _START), (end, _END)]

    def __merged_ends(self, other):
        sorted_ends = self.__ends[:]
        for end in other.__ends:
            bisect.insort(sorted_ends, end)
        return sorted_ends

    def __or__(self, other):
        sorted_ends = self.__merged_ends(other)
        state = 0
        new_ends = []
        for _, end in sorted_ends:
            if end == _START:
                state += 1
            else:
                state -= 1
            if state > 1 and end == _START:
                continue
            elif state > 0 and end == _END:
                continue
            new_ends.append((_, end))
        result = RangeSet(None, None)
        result.__ends = new_ends
        return result

    union = __or__

    def __and__(self, other):
        sorted_ends = self.__merged_ends(other)
        state = 0
        new_ends = []
        for _, end in sorted_ends:
            if end == _START:
                state += 1
            else:
                state -= 1
            if state == 2 and end == _START:
                new_ends.append((_, end))
            elif state == 1 and end == _END:
                new_ends.append((_, end))
        result = RangeSet(None, None)
        result.__ends = new_ends
        return result

    intersect = __and__

    def __invert__(self):
        new_ends = self.__ends[:]
        head, tail = [], []
        if new_ends[0][0] == NEGATIVE_INFINITY:
            new_ends.pop(0)
        else:
            head = [(NEGATIVE_INFINITY, _START)]
        if new_ends[-1][0] == INFINITY:
            new_ends.pop(-1)
        else:
            tail = [(INFINITY, _END)]
        for i, value in enumerate(new_ends):
            new_ends[i] = (value[0], _NEGATE[value[1]])
        result = RangeSet(None, None)
        result.__ends = head + new_ends + tail
        return result

    def measure(self):
        if self.__ends[0] in _INDETERMINATE or self.__ends[-1] in _INDETERMINATE:
            raise ValueError("Cannot compute range with unlimited bounds.")
        return sum(self.__ends[i + 1][0] - self.__ends[i][0] for i in range(0, len(self.__ends), 2))

    def range(self):
        if self.__ends[0] in _INDETERMINATE or self.__ends[-1] in _INDETERMINATE:
            raise ValueError("Cannot compute range with unlimited bounds.")
        return self.__ends[-1][0] - self.__ends[0][0]

    def __str__(self):
        pieces = ["{} -- {}".format(self.__ends[i][0], self.__ends[i + 1][0])
                                    for i in range(0, len(self.__ends), 2)]
        return "<RangeSet {}>".format(", ".join(pieces))

    __repr__ = __str__


_INDETERMINATE = (INFINITY, NEGATIVE_INFINITY)

_START = -1
_END = 1

_NEGATE = {_START: _END, _END: _START}
