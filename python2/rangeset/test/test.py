import doctest
import glob
import os

if __name__ == '__main__':
    for f in glob.glob(os.path.join(os.path.dirname(__file__),
                                    '*.txt')):
        print "Testing {}".format(f)
        doctest.testfile(os.path.basename(f))
