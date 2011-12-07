"""
Range of time stuff
"""

import bisect
import operator
import collections

__all__ = ('INFINITY', 'NEGATIVE_INFINITY',
           'RangeSet')

class _Indeterminate(object):
    pass

class _Infinity(_Indeterminate):
    def __cmp__(self, other):
        return 0 if other is self else 1
    def __str__(self):
        return 'inf'

class _NegativeInfinity(_Indeterminate):
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
        self.__ends = ((start, _START), (end, _END))

    def __merged_ends(self, *others):
        sorted_ends = list(self.__ends)
        for other in others:
            for end in RangeSet.__promote(other).__ends:
                bisect.insort(sorted_ends, end)
        return sorted_ends

    @classmethod
    def __promote(cls, value):
        if isinstance(value, RangeSet):
            return value
        else:
            return RangeSet(value[0], value[1])

    def __or__(self, *other):
        sorted_ends = self.__merged_ends(*other)
        new_ends = []
        for _, end, state in RangeSet.__iterate_state(sorted_ends):
            if state > 1 and end == _START:
                continue
            elif state > 0 and end == _END:
                continue
            new_ends.append((_, end))
        result = RangeSet(None, None)
        result.__ends = tuple(new_ends)
        return result

    union = __or__

    def __and__(self, *other):
        sorted_ends = self.__merged_ends(*other)
        new_ends = []
        for _, end, state in RangeSet.__iterate_state(sorted_ends):
            if state == 2 and end == _START:
                new_ends.append((_, end))
            elif state == 1 and end == _END:
                new_ends.append((_, end))
        result = RangeSet(None, None)
        result.__ends = tuple(new_ends)
        return result

    intersect = __and__

    def __ror__(self, other):
        return self.__or__(other)

    def __rand__(self, other):
        return self.__rand__(other)

    @classmethod
    def __iterate_state(cls, ends):
        state = 0
        for _, end in ends:
            if end == _START:
                state += 1
            else:
                state -= 1
            yield _, end, state

    def symmetric_difference(self, *other):
        sorted_ends = self.__merged_ends(*other)
        new_ends = []
        old_val = None
        for _, end, state in RangeSet.__iterate_state(sorted_ends):
            if state == 2 and end == _START:
                new_ends.append((_, _NEGATE[end]))
            elif state == 1 and end == _END:
                new_ends.append((_, _NEGATE[end]))
        result = RangeSet(None, None)
        result.__ends = tuple(new_ends)
        return result

    def __contains__(self, test):
        rangeset = None
        if isinstance(test, RangeSet):
            rangeset = test
        if hasattr(test, '__getitem__'):
            try:
                rangeset = RangeSet.__promote(test)
            except TypeError:
                pass
        if rangeset is not None:
            difference = rangeset - ~self
            return difference == rangeset

        last_val, last_end = None, None
        for _, end, state in RangeSet.__iterate_state(self.__ends):
            if last_val is not None and _ > test:
                return last_end == _START
            elif _ > test:
                return False
            last_val, last_end = _, end
        return False

    def __invert__(self):
        new_ends = list(self.__ends)
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
        result.__ends = tuple(head + new_ends + tail)
        return result

    invert = __invert__

    def __sub__(self, other):
        return self & ~other

    def subtract(self, other):
        return self.__sub__(other)

    def __rsub__(self, other):
        return RangeSet.__promote(other) - self

    def measure(self):
        if isinstance(self.__ends[0][0], _Indeterminate) or isinstance(self.__ends[-1][0], _Indeterminate):
            raise ValueError("Cannot compute range with unlimited bounds.")
        return reduce(operator.add, (self.__ends[i + 1][0] - self.__ends[i][0] for i in range(0, len(self.__ends), 2)))

    def range(self):
        if isinstance(self.__ends[0][0], _Indeterminate) or isinstance(self.__ends[-1][0], _Indeterminate):
            raise ValueError("Cannot compute range with unlimited bounds.")
        return self.__ends[-1][0] - self.__ends[0][0]

    def __str__(self):
        pieces = ["{} -- {}".format(self.__ends[i][0], self.__ends[i + 1][0])
                                    for i in range(0, len(self.__ends), 2)]
        return "<RangeSet {}>".format(", ".join(pieces))

    __repr__ = __str__

    def __eq__(self, other):
        if self is other:
            return True
        elif not isinstance(other, RangeSet):
            return False
        return self.__ends == other.__ends

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.__ends)

    @classmethod
    def mutual_overlaps(cls, *ranges):
        return cls.__promote(ranges[0]).intersect(*ranges[1:])

    @classmethod
    def mutual_union(cls, *ranges):
        return cls.__promote(ranges[0]).union(*ranges[1:])



_START = -1
_END = 1

_NEGATE = {_START: _END, _END: _START}
