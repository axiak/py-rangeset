try:
    from setuptools import setup
    test = True
except ImportError:
    test = False
    from distutils.core import setup
import sys
import os

pkgdir = {'': 'python%s' % sys.version_info[0]}

sys.path.insert(0, pkgdir[''])

VERSION = '0.0.7'

kwargs = {}

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
          long_description=""" """,
          package_dir=pkgdir,
          packages=['rangeset'],
          install_requires=[
            'blist'
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
