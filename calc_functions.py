#!/usr/bin/env python3
##
## EPITECH PROJECT, 2020
## Projects 108Trigo
## File description:
## calc_matrix.py
##

import sys
from math import *

def calc_fct_eval(x, n):
    res = 1

    if x == 0:
        return(1)
    try :
        for k in range(0, n + 1):
            res = res * ((sin(x / ((2 * k) + 1))) / (x / ((2 * k) + 1)))
    except ZeroDivisionError:
        sys.exit(84)
    return(res)

def calc_midpoint(n):
    res = 0
    x = 0.25

    try :
        for i in range (0, 10000):
            res = res + (0.5 * calc_fct_eval(x, n))
            x += 0.5
    except ZeroDivisionError:
        sys.exit(84)
    return(res)

def calc_trapezoid(n):
    res = 0

    for i in range (1, 10000):
        res += calc_fct_eval(i * 0.5, n)
    res = 0.25 * ((1 + calc_fct_eval(5000, n)) + 2 * res)
    return(res)

def calc_simpson(n):
    res = 0
    res1 = 0
    res2 = 0
    x = 0.25

    for i in range (1, 10000):
        res1 += calc_fct_eval(i * 0.5, n)
    for i in range (0, 10000):
        res2 += calc_fct_eval((i * 0.5) + 0.25, n)
    res = 5000 / 60000 * (1 + calc_fct_eval(5000, n) + 2 * res1 + 4 * res2);
    return(res)