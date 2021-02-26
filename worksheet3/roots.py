#!/usr/bin/env python
#
# Author: Oscar Benjamin
# Date: Feb 2021
# Description:
#   Command line script to find integer roots of polynomials with
#   integer coefficients.


#-------------------------------------------------------------------#
#                                                                   #
#                   Command-line interface                          #
#                                                                   #
#-------------------------------------------------------------------#

PROGRAM_EXPLANATION = """
Usage:
$ python roots.py COEFF1 COEFF2 ...

Find integer roots of a polynomial with integer coefficients.

Example:

Find the roots of x^4 - 3x^3 - 75x^2 + 475x - 750.

$ python roots.py 1 -3 -75 475 -750
-10
3
5
"""


def main(*arguments):
    """Main entry point for the program"""
    if not arguments:
        print(PROGRAM_EXPLANATION)
        return

    poly = parse_coefficients(arguments)
    roots = integer_roots(poly)
    print_roots(roots)


def parse_coefficients(arguments):
    """Convert string arguments to integer

    >>> parse_coefficients(["2", "3"])
    [2, 3]
    """
    return [int(arg) for arg in arguments]


def print_roots(roots):
    """Print the roots one per line if there are any

    >>> print_roots([2, 3])
    2
    3
    """
    if roots:
        roots_str = [str(r) for r in roots]
        print('\n'.join(roots_str))


#-------------------------------------------------------------------#
#                                                                   #
#                      Polynomial functions                         #
#                                                                   #
#-------------------------------------------------------------------#


class BadPolynomialError(Exception):
    """Raised by polynomial routines when the polynomial is invalid.

    A valid polynomial is a list of coefficients like [1, 2, 1]

    The first (leading) coefficient must *not* be zero in a valid polynomial.
    """
    pass

def find_factors(x):
    factors = []
    # in the ascending order of absolute values
    if x > 0:
        for i in range(1, x + 1):
            if x % i == 0:
                factors.append(i)
    elif x < 0:
        for i in range(x, 0):
            if x % i == 0:
                factors.insert(0, i)
    else:
        factors.append(0)
    return factors

def integer_roots(poly):
    num_coef = len(poly)
    # add exceptions
    if (num_coef>0 and (poly[0]==0 or not isinstance(poly[0], int) ) ) \
        or not isinstance(poly, list):
        raise BadPolynomialError("Invalid coefficients")

    print(poly)
    if num_coef == 0:
        return []
    # find integer factors of a_0 and a_n
    ps = find_factors(poly[-1])
    qs = find_factors(poly[0])
    # find rational roots
    int_roots = []
    for p in ps:
        for q in qs:
            # only keep integer roots
            if p % q == 0:
                tmp = p/q
                # use append for positive, insert for negative
                if tmp < 0: tmp = -1*tmp
                if is_root(poly, tmp):
                    int_roots.append(tmp)
                if is_root(poly, -1*tmp):
                    int_roots.insert(0, -1*tmp)
    return int_roots

def evaluate_polynomial(poly, xval):
    num_coef = len(poly)
    # add exceptions
    if (num_coef>0 and (poly[0]==0 or not isinstance(poly[0], int) ) ) \
        or not isinstance(poly, list):
        raise BadPolynomialError("Invalid coefficients")
    # no coefficients given
    if num_coef == 0:
        return 0
    # evaluating
    val = 0
    for i in range(num_coef):
        power = num_coef-i-1
        val = val + poly[i] * (xval**power)
    return val

def is_root(poly, xval):
    num_coef = len(poly)
    # add exceptions
    if (num_coef>0 and (poly[0]==0 or not isinstance(poly[0], int) ) ) \
        or not isinstance(poly, list):
        raise BadPolynomialError("Invalid coefficients")
    # test root
    val = 0
    for i in range(num_coef):
        power = num_coef-i-1
        val = val + poly[i] * (xval**power)
    if val == 0:
        return True
    else:
        return False
       


#-------------------------------------------------------------------#
#                                                                   #
#                           Unit tests                              #
#                                                                   #
#-------------------------------------------------------------------#

#
# Run these tests with pytest:
#
#    $ pytest roots.py
#

def test_evaluate_polynomial():
    assert evaluate_polynomial([], 1) == 0
    assert evaluate_polynomial([1], 2) == 1
    assert evaluate_polynomial([1, 2], 3) == 5
    assert evaluate_polynomial([1, 2, 1], 4) == 25

    # Invalid inputs should raise BadPolynomialError
    from pytest import raises
    raises(BadPolynomialError, lambda: evaluate_polynomial([0], 1))
    raises(BadPolynomialError, lambda: evaluate_polynomial({}, 1))
    raises(BadPolynomialError, lambda: evaluate_polynomial([[1]], 1))


def test_is_root():
    assert is_root([], 1) is True
    assert is_root([1], 1) is False
    assert is_root([1, 1], 1) is False
    assert is_root([1, 1], -1) is True
    assert is_root([1, -1], 1) is True
    assert is_root([1, -1], -1) is False
    assert is_root([1, -5, 6], 2) is True
    assert is_root([1, -5, 6], 3) is True
    assert is_root([1, -5, 6], 4) is False

    # Invalid inputs should raise BadPolynomialError
    from pytest import raises
    raises(BadPolynomialError, lambda: is_root([0], 1))
    raises(BadPolynomialError, lambda: is_root({}, 1))
    raises(BadPolynomialError, lambda: is_root([[1]], 1))


def test_integer_roots():
    # In the case of the zero polynomial every value is a root but we return
    # the empty list because we can't list every possible value!
    assert integer_roots([]) == []
    assert integer_roots([1]) == []
    assert integer_roots([1, 1]) == [-1]
    assert integer_roots([2, 1]) == []
    assert integer_roots([1, -5, 6]) == [2, 3]
    assert integer_roots([1, 5, 6]) == [-3, -2]
    assert integer_roots([1, 2, 1]) == [-1]
    assert integer_roots([1, -2, 1]) == [1]
    assert integer_roots([1, -2, 1]) == [1]
    assert integer_roots([1, -3, -75, 475, -750]) == [-10, 3, 5]

    # Invalid inputs should raise BadPolynomialError
    from pytest import raises
    raises(BadPolynomialError, lambda: integer_roots([0]))
    raises(BadPolynomialError, lambda: integer_roots({}))
    raises(BadPolynomialError, lambda: integer_roots([[1]]))


if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]
    main(*arguments)
