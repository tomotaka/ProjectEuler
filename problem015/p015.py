# -*- coding: utf-8 -*-


def factorial(n):
    ret = 1
    for i in xrange(1, n + 1):
        ret *= i
    return ret


def combination(a, b):
    return factorial(a) / (factorial(a - b) * factorial(b))


def main():
    """total operation: 20go-down + 20go-right = 40, problem is to
    choice 20go-right(or down) operations from total 40 operations"""
    print combination(40, 20)


if __name__ == '__main__':
    main()
