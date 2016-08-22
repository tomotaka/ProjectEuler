# -*- coding: utf-8 -*-


def coratz(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1


def gen_coratz(start):
    n = start
    yield n
    while True:
        n = coratz(n)
        yield n
        if n == 1:
            break


def main():
    """naive solution: slow"""
    assert len(list(gen_coratz(13))) == 10
    i = 1

    max_i = 0
    max_c = 0

    while i <= 1000000:
        c = 0
        numbers = []
        for _ in gen_coratz(i):
            c += 1
            numbers.append(_)

        # print '%d: %d: %s' % (i, c, numbers)

        if max_c < c:
            max_i, max_c = i, c
            print 'updated: %d: N=%d' % (i, c)

        i += 1


if __name__ == '__main__':
    main()
