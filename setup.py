#!/usr/bin/env python
#
#       setup.py
#
#       Copyright 2009 Thomas Jost <thomas.jost@gmail.com>
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

from setuptools import setup
import glob

exec(open('pympress/version.py').read())

setup(name="pympress",
      version=__version__,
      description="A simple dual-screen PDF reader designed for presentations",
      author="Thomas Jost, Christof Rath",
      author_email="thomas.jost@gmail.com, christof.rath@gmail.com",
      url="http://www.pympress.org/",
      download_url="https://github.com/nobecutan/pympress/releases",
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: X11 Applications :: GTK',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Information Technology',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Natural Language :: English',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Topic :: Multimedia :: Graphics :: Presentation',
          'Topic :: Multimedia :: Graphics :: Viewers',
      ],
      packages=["pympress"],
      scripts=["bin/pympress"],
      data_files=[
          ("share/pixmaps", glob.glob("share/pixmaps/pympress*")),
      ],
)

##
# Local Variables:
# mode: python
# indent-tabs-mode: nil
# py-indent-offset: 4
# fill-column: 80
# end:
