#!/usr/bin/env python3
##
## EPITECH PROJECT, 2020
## Projects 110borwein
## File description:
## help.py
##

import sys

def helper():
    print("USAGE")
    print("    ./110borwein n\n")
    print("DESCRIPTION")
    print("    n    constant defining the integral to be computed")

def check_n(n):
    try :
        n = int(sys.argv[1])
    except ValueError:
        sys.exit(84)
    if (n < 0 or n > 1000):
        sys.exit(84)

def check_error(ac, av):
    if ac != 2:
        sys.exit(84)
    if av[1] == "-h":
        helper();
        sys.exit(0)