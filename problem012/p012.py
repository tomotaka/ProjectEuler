# -*- coding: utf-8 -*-

_fcache = dict()


def triangle_number(n):
    return n * (n + 1) / 2


def factorize(n):
    factors = [1]
    i = 2
    while i <= n - 1:
        if n % i == 0:
            factors.append(i)
        i += 1
    factors.append(n)
    return factors


def f2(n):
    tn = triangle_number(n)
    a = n
    b = n + 1

    if a % 2 == 0:
        a = a / 2
    else:
        b = b / 2

    if a not in _fcache:
        fa = factorize(a)
        _fcache[a] = fa
    else:
        fa = _fcache[a]

    if b not in _fcache:
        fb = factorize(b)
        _fcache[b] = fb
    else:
        fb = _fcache[b]

    fn = set([1, tn])
    for f1 in fa:
        for f2 in fb:
            fn.add(f1 * f2)
    result = sorted(list(fn))
    _fcache[tn] = result
    return result


def show(n):
    tn = triangle_number(n)
    f = f2(n)
    print '%d: N=%d : %s' % (n, len(f), f)


def main():
    i = 1
    while True:
        f = f2(i)
        tn = triangle_number(i)
        print '%d: triangle-number=%d, factors=%d' % (i, tn, len(f))
        if 500 < len(f):
            break
        i += 1


if __name__ == '__main__':
    main()
