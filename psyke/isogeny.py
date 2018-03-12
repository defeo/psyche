# -*- coding: utf-8 -*-

"""
An elliptic curve isogeny
"""

from __future__ import print_function
from .ec import EC

class Isogeny(object):
    def __init__(self, E, gen):
        self.I = E.isogeny(gen)

    def degree():
        return self.I.degree()

    def eval(*points):
        j = self.I.codomain().j_invariant()
        x = j.parent().polynomial_ring().gen()
        A = (256*(x**2 - 3)**3 - (x**2 - 4)*j).any_root()
        im = EC(A)
        return im, [im.point(self.I(P)) for P in points]

class FourIsogeny(Isogeny):
    pass

class ThreeIsogeny(Isogeny):
    pass

class SecretIsogeny(Isogeny):
    pass
