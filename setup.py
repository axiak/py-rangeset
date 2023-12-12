try:
    from setuptools import setup
    test = True
except ImportError:
    test = False
    from distutils.core import setup
import sys
import os

VERSION = '0.0.15'

kwargs = {}


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as f:
    long_description = f.read()

if test:
    kwargs['test_suite'] = 'rangeset.test.test.suite'


def main():
    setup(name='rangeset',
          version=VERSION,
          author='Mike Axiak',
          author_email='mike@axiak.net',
          url='https://github.com/axiak/py-rangeset/',
          description='A data structure for dealing with sets of ranges.',
          license='MIT',
          long_description=long_description,
          #package_dir= {'': 'python%s' % sys.version_info[0]},
          packages=['rangeset'],
          install_requires=[
            'sortedcontainers'
          ],
          classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Software Development :: Libraries',
            ],
          **kwargs
          )


if __name__ == '__main__':
    main()
