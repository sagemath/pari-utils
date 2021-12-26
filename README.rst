pari-utils
==========

A Python library to parse PARI/GP configuration and header files. This
is mainly used in the code generation of https://github.com/sagemath/cypari2
and https://github.com/sagemath/pari-jupyter.

This library supports only Python 3.

Installation
------------

Using pip
^^^^^^^^^

Requirements:

- PARI/GP >= 2.9.4 (header files and library)
- Python >= 3.7
- setuptools >= 40.6.0, wheel

Install pari-utils via the Python Package Index (PyPI) via

::

    $ pip install pari-utils [--user]

(the optional option *--user* allows to install pari-utils for a single user
and avoids using pip with administrator rights). Depending on your operating
system the pip command might also be called pip2 or pip3.

If you want to try the development version use

::

    $ pip install git+https://github.com/sagemath/pari-utils.git [--user]

Contributing
------------

Submit pull request or get in touch with the SageMath developers.
