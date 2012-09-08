#!/usr/bin/env python
import sys
from distutils.core import setup
from rapper import __version__

if sys.version < "2.5":
    sys.exit("Python 2.5 or higher is required")

setup(name="rapper",
      version=__version__,
      description="A unified interface for storing data in different databases.",
#      long_description="""""",
      license="Apache License 2.0",
      author="myfreeweb",
      author_email="floatboth@me.com",
      url="https://github.com/myfreeweb/rapper",
      requires=[],
      packages=[],
      keywords=["persistence", "database", "storage", "postgresql", "mongodb",
                "nosql", "hstore"],
      classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries",
      ],
      package_data={},
)
