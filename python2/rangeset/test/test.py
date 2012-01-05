import unittest
import doctest
import glob
import os

def runtest():
    for f in glob.glob(os.path.join(os.path.dirname(__file__),
                                    '*.txt')):
        print "Testing {}".format(f)
        doctest.testfile(os.path.basename(f))

def suite():
    suite = unittest.TestSuite()
    for f in glob.glob(os.path.join(os.path.dirname(__file__),
                       '*.txt')):
        suite.addTest(doctest.DocFileSuite(os.path.basename(f)))
    return suite
        

if __name__ == '__main__':
    runtest()
