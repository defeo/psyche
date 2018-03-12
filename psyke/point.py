# -*- coding: utf-8 -*-

"""
An elliptic curve point
"""

from __future__ import print_function

class Point(object):
    def __init__(self, E, x):
        """
        A point on E with x-coordinate x
        """
        self.curve = E
        self.P = E.sage().lift_x(x)

    def double(self):
        return Point(self.curve, (2*self.P)[0])

    def triple(self):
        return Point(self.curve, (3*self.P)[0])

    def k_times_plus(self, k, other, diff):
        Q = other.P
        if (self.P - other.P)[0] != diff.P[0]:
            Q = -Q
            assert (self.P - Q)[0] == diff.P[0]
        return Point(self.curve, (k*self.P + Q)[0])

    def __repr__(self):
        return repr(self.P)

    def _sage(self):
        return self.P
