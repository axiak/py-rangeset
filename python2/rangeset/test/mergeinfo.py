import timeit
import random
import bisect
import operator

test_data = [None]

def generate_test_data(size=200, lists=2):
    results = []
    for _ in range(lists):
        l = []
        for i in range(size / 2):
            l.append((random.random(), -1))
            l.append((random.random(), 1))
        l.sort()
        results.append(tuple(l))
    test_data[0] = results
    return results

def bisect_test():
    data = test_data[0]
    merged = list(data[0])
    for other in data[1:]:
        for end in other:
            bisect.insort(merged, end)
    return merged

def chain_and_sort():
    data = test_data[0]
    merged = list(reduce(operator.add, data))
    merged.sort()
    return merged

def build_manually():
    data = test_data[0]
    result = [None] * sum(len(x) for x in data)
    current_index = len(result) - 1
    indexes = [len(x) - 1 for x in data]
    while current_index >= 0:
        m, index = max((data[i][indexes[i]], i) for i in range(len(indexes))
                       if indexes[i] >= 0)
        result[current_index] = m
        current_index -= 1
        indexes[index] -= 1

if __name__ == '__main__':
    generate_test_data()
    for test in ('bisect_test', 'chain_and_sort', 'build_manually'):
        t = timeit.Timer("%s()" % test, "from __main__ import %s" % test)
        print t.timeit(number=10000)
