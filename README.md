# rangeset - A utility belt for operations on sets of ranges #

[![Build Status](https://secure.travis-ci.org/axiak/py-rangeset.png?branch=master)](http://travis-ci.org/axiak/py-rangeset)

## Overview ##

Rangeset is a package that allows for easy manipulation of sets of ranges. These ranges can contain any ordered elements, be they numbers, tuples, or even datetime objects.

## Installation ##

Use either:

    python setup.py install


or:

    pip install rangeset

## Documentation ##

See http://axiak.github.com/py-rangeset

## Basic Usage ##

```python
import rangeset

# Create a rangeset
>>> r = RangeSet(1, 3) | (5, 6)

# negate
>>> (~r) & (0, 10)
<RangeSet 0 -- 1, 3 -- 5, 6 -- 10>

# "measure" - How much distance is in the ranges, minus the gaps
>>> ((~r) & (0, 10)).measure()
7

# range - Total distance between start and end
>>> ((~r) & (0, 10)).range()
10
```

For more usage examples, see the doctests at https://github.com/axiak/py-rangeset/tree/master/python2/rangeset/test

## License ##

It's licensed under the MIT License. Please see the license file for more:
https://github.com/axiak/py-rangeset/blob/master/LICENSE
