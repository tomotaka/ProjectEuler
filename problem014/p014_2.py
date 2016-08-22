# -*- coding: utf-8 -*-
_cache = dict()


def coratz(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1


def len_coratz(n):
    orig = n
    length = 1
    while n != 1:
        n = coratz(n)
        if n in _cache:
            length += _cache[n]
            break
        else:
            length += 1

    _cache[orig] = length
    return length


def main():
    """use cache"""
    assert len_coratz(2) == 2
    assert len_coratz(13) == 10
    i = 2

    max_i = 0
    max_c = 0

    while i <= 1000000:
        c = len_coratz(i)

        # print '%d: %d: %s' % (i, c, numbers)

        if max_c < c:
            max_i, max_c = i, c
            print 'updated: %d: N=%d' % (i, c)

        i += 1


if __name__ == '__main__':
    main()
