# -*- coding: utf-8 -*-

"""
An elliptic curve
"""

from __future__ import print_function
from sage.schemes.elliptic_curves.constructor import EllipticCurve
from .gf import GF
from .point import Point

class EC(object):
    def __init__(self, A, C=None):
        """
        Cy² = Cx³ + Ax + Cx
        """

        # Internally, we represent it as a Sage elliptic curve.
        a = A/C if C is not None else A
        self.ec = EllipticCurve([0, a._sage(), 0, 1, 0])


    def j(self):
        j = self.ec.j_invariant()
        return GF(j.parent().characteristic(), *j.polynomial().list())

    def point(self, x):
        return Point(self, x)

    def four_isogeny(self, gen):
        pass

    def three_isogeny(self, gen):
        pass

    def secret_isogeny(self, gen):
        pass

    def __repr__(self):
        return repr(self.ec)

    def _sage(self):
        return self.ec
