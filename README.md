# rangeset - A utility belt for operations on sets of ranges #

## Overview ##

Rangeset is a package that allows for easy manipulation of sets of ranges. These ranges can contain any ordered elements, be they numbers, tuples, or even datetime objects.

## Installation ##

    python setup.py install

- or -

    pip install rangeset

## Basic Usage ##

    import rangeset

    # Create a rangeset
    >>> r = RangeSet(1, 3) | RangeSet(5, 6)

    # negate
    >>> (~r) & RangeSet(0, 10)
    <RangeSet 0 -- 1, 3 -- 5, 6 -- 10>

    # "measure" - How much distance is in the ranges, minus the gaps
    >>> ((~r) & RangeSet(0, 10)).measure()
    7

    # range - Total distance between start and end
    >>> ((~r) & RangeSet(0, 10)).range()
    10
