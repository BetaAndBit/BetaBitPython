# !/usr/bin/env python

NAME = "betabit"
DESCRIPTION = "Incredible Adventures of Beta and Bit"
LONG_DESCRIPTION = '"The Proton Game" is a console-based data-crunching game for younger and older data scientists. Act as a data-hacker and find Slawomir Pietraszko\'s credentials to the Proton server. You have to solve four data-based puzzles to find the login and password. There are many ways to solve these puzzles. You may use loops, data filtering, ordering, aggregation or other tools.\nThis game is linked with the "Pietraszko\'s Cave" story available at http://biecek.pl/BetaBit/Warsaw.\nIt\'s a part of Beta and Bit series. You will find more about the Beta and Bit series at http://biecek.pl/BetaBit.'
MAINTAINER = "Piotr Smuda"
MAINTAINER_EMAIL = "piotrsmuda@gmail.com"
LICENSE = "GNU"
URL = "https://github.com/BetaAndBit/BetaBitPython"
DOWNLOAD_URL = "https://github.com/BetaAndBit/BetaBitPython"
VERSION = "1.0"

try:
    from setuptools import setup
    _have_setuptools = True
except ImportError:
    from distutils.core import setup

def dependencies():
    """
    This function checks which imports are required.
    """
    
    requirments = []
    try:
        import pandas
    except ImportError:
        requirments.append("pandas")
    try:
        import numpy
    except ImportError:
        requirments.append("numpy")
    try:
        import string
    except ImportError:
        requirments.append("string")
    try:
        import os
    except ImportError:
        requirments.append("os")    
    try:
        import hashlib
    except ImportError:
        requirments.append("hashlib")
    try:
        import re
    except ImportError:
        requirments.append("re")
        
    return requirments

if __name__ == "__main__":
    
    requirments = dependencies()
    setup(name = NAME,
          description = DESCRIPTION,
          long_description = LONG_DESCRIPTION,
          author = MAINTAINER,
          author_email = MAINTAINER_EMAIL,
          maintainer = MAINTAINER,
          maintainer_email = MAINTAINER_EMAIL,
          license = LICENSE,
          url = URL,
          download_url = DOWNLOAD_URL,
          version = VERSION,
          install_requires = requirments,
          packages = ['betabit'],
          package_data = {'betabit': ['data/*.csv']})
                
          