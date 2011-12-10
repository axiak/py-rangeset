# rangeset - A utility belt for operations on sets of ranges #

## Overview ##

Rangeset is a package that allows for easy manipulation of sets of ranges. These ranges can contain any ordered elements, be they numbers, tuples, or even datetime objects.

## Installation ##

Use either:

    python setup.py install


or:

    pip install rangeset

## Documentation ##

See http://axiak.github.com/py-rangeset

## License ##

It's licensed under the MIT License. Please see the license file for more:
https://github.com/axiak/py-rangeset/blob/master/LICENSE

## Basic Usage ##

```python
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
```

For more usage examples, see the doctests at https://github.com/axiak/py-rangeset/tree/master/python2/rangeset/test