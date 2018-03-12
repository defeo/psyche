# -*- coding: utf-8 -*-

import unittest
from psyke import GF, EC

class TestEC(unittest.TestCase):
    def test_j(self):
        """
        Test that j-invariant is correct
        """
        # y² = x³ + x  (j = 1728)
        self.assertEqual(EC(GF(11)).j(), GF(11, 1728))
        # y² = x³ + x² + x  (j = 2048/3)
        self.assertEqual(EC(GF(11, 1)).j(), GF(11, 2048) / GF(11, 3))
