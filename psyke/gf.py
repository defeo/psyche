# -*- coding: utf-8 -*-

"""
An element a + b i of GF(p²), where i² = -1.
"""

from __future__ import print_function
from sage.rings.finite_rings.finite_field_constructor import GF as SageGF

class GF(object):
    def __init__(self, p, a=0, b=0):
        """
        Assumes p is prime.

        Gives an error if p ≠ 3 mod 4.
        """
        assert p % 4 == 3

        # Internally, we represent our element as a Sage field element.
        #
        # Rewrite your own implementation, of GF(p²) on top of Python integers
        I = SageGF(p)['I'].gen()
        base = SageGF(p**2, 'i', modulus=I**2 + 1)
        i = base.gen()
        self.elt = a + b*i

    def __add__(self, other):
        return GF(self.elt.parent().characteristic(),
                      *(self.elt + other.elt).polynomial().list())

    def __neg__(self):
        return GF(self.elt.parent().characteristic(),
                      *(-self.elt).polynomial().list())

    def __sub__(self, other):
        return GF(self.elt.parent().characteristic(),
                      *(self.elt - other.elt).polynomial().list())
    
    def __mul__(self, other):
        return GF(self.elt.parent().characteristic(),
                      *(self.elt * other.elt).polynomial().list())

    def square(self):
        return self * self

    def __pow__(self, exp):
        return GF(self.elt.parent().characteristic(),
                      *(self.elt**exp).polynomial().list())

    def inverse(self):
        return GF(self.elt.parent().characteristic(),
                      *(~self.elt).polynomial().list())
        
    def __truediv__(self, other):
        return self * other.inverse()
    __div__ = __truediv__    # Python 2 compatibility

    def __eq__(self, other):
        return self.elt == other.elt

    def __repr__(self):
        return repr(self.elt)

    def _sage(self):
        return self.elt
