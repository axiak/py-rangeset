import doctest
import glob
import os

def runtest():
    for f in glob.glob(os.path.join(os.path.dirname(__file__),
                                    '*.txt')):
        print "Testing {}".format(f)
        doctest.testfile(os.path.basename(f))

if __name__ == '__main__':
    runtest()
