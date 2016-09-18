# -*- coding: utf-8 -*-
is_abun_map = dict()


def factors(n):
    ret = [1]
    i = 2
    while i < n:
        if n % i == 0:
            ret.append(i)
        i += 1
    return ret


def is_abundant(n):
    sumf = sum(factors(n))
    return (n < sumf)


def is_gousei(n):
    a = 12
    half = n / 2
    while a <= half:
        b = n - a

        if a not in is_abun_map:
            is_abun_map[a] = is_abundant(a)

        if b != a and b not in is_abun_map:
            is_abun_map[b] = is_abundant(b)

        if is_abun_map[a] and is_abun_map[b]:
            return True

        a += 1

    return False


def main():
    i = 28123 - 1
    while 24 <= i:
        if is_gousei(i):
            print '%5d: True' % i
        else:
            print '%5d: False!' % i
            break

        i -= 1


if __name__ == '__main__':
    main()
