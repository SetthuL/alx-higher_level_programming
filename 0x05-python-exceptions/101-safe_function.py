#!/usr/bin/python3
from __future__ import print_function
import sys


def safe_function(fct, *args):
    try:
        sl = fct(*args)
    except Exception as dr:
        print("Exception: {}".format(dr), file=sys.stderr)
        return None
    else:
        return (sl)
