from distutils.core import setup
import sys

pkgdir = {'': 'python%s' % sys.version_info[0]}
VERSION = '0.0.1'

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
