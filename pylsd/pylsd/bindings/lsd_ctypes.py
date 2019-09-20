#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-19 02:09:53
# @Author  : Gefu Tang (tanggefu@gmail.com)
# @Link    : https://github.com/primetang/pylsd
# @Version : 0.0.1

import ctypes
import os
import sys
import random
import numpy as np
from pkg_resources import resource_filename
from .. import lib


def load_lsd_library():

    root_dir = os.path.abspath(os.path.dirname(__file__))

    libnames = ['linux/liblsd.so']
    libdir = 'lib'
    if sys.platform == 'win32':
        if sys.maxsize > 2 ** 32:
            libnames = ['win32/x64/lsd.dll', 'win32/x64/liblsd.dll']
        else:
            libnames = ['win32/x86/lsd.dll', 'win32/x86/liblsd.dll']
    elif sys.platform == 'darwin':
        libnames = ['darwin/liblsd.dylib']

    lsdlib = ctypes.cdll[os.path.join(resource_filename('pylsd', libdir), libnames[0])]
    return lsdlib

lsdlib = load_lsd_library()
if lsdlib == None:
    raise ImportError('Cannot load dynamic library. Did you compile LSD?')
