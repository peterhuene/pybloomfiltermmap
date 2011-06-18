import sys
import os

try:
    import Cython
    # may need to work around setuptools bug by providing a fake Pyrex
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "fake_pyrex"))
except ImportError:
     pass

try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup
    from distutils.extension import Extension

ext_files = ["src/mmapbitarray.c",
             "src/bloomfilter.c",
             "src/primetester.c",
             ]

kwargs = {}

try:
    from Cython.Distutils import build_ext
    print "Building from Cython"
    ext_files.append("src/pybloomfilter.pyx")
    kwargs['cmdclass'] = {'build_ext': build_ext}
except ImportError:
    ext_files.append("src/pybloomfilter.c")
    print "Building from C"

ext_modules = [Extension("pybloomfilter",
                         ext_files)]

setup(
  name = 'pybloomfiltermmap',
  version = "0.2.0",
  author = "Michael Axiak, Rob Stacey",
  author_email = "mike@axiak.net",
  url = "http://github.com/axiak/pybloomfiltermmap/",
  description = "A Bloom filter (bloomfilter) for Python built on mmap",
  license = "MIT License",
  ext_modules = ext_modules,
  classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: C',
        'Programming Language :: Cython',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
  **kwargs
)
 
