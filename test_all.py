# -*- coding: utf-8 -*-
import random

from Karatsuba_Multiplication import karatsuba


def test_hello_pytest():

    for i in range(1000):
        n1, n2 = random.randint(0, 10000), random.randint(0, 10000)

        assert n1 * n2 == karatsuba(n1, n2)
