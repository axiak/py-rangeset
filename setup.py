from distutils.core import setup
import sys
import os

pkgdir = {'': 'python%s' % sys.version_info[0]}
VERSION = '0.0.4'


def run_test():
    sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                    pkgdir['']))
    from rangeset.test import test
    test.runtest()

def main():
    if 'test' in sys.argv[1:]:
        return run_test()
    setup(name='rangeset',
          version=VERSION,
          author='Mike Axiak',
          author_email='mike@axiak.net',
          url='https://github.com/axiak/py-rangeset/',
          description='A data structure for dealing with sets of ranges.',
          license='MIT',
          long_description=""" """,
          package_dir=pkgdir,
          packages=['rangeset'],
          #package_data={'rangeset': ['*.txt']},
          classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Software Development :: Libraries',
            ],
          )

if __name__ == '__main__':
    main()
