# -*- coding: utf-8 -*-


def is_pandigital(n):
    s = str(n)
    if len(s) != 9:
        return False

    check = [0] * 9
    for c in s:
        check[int(c) - 1] = 1
    return sum(check) == 9


def catprod(n, m):
    numbers = [ n * i for i in xrange(1, m + 1) ]
    return int(''.join([ str(i) for i in numbers ]))


def main():
    # print is_pandigital('123456789')
    # print is_pandigital('125678934')
    # print is_pandigital('')
    # print is_pandigital('1')
    # print is_pandigital('148729')

    # print catprod(192, 3)

    max_i = None
    max_j = None
    max_cp = None

    i = 1
    while True:
        j = 1
        while True:
            cp = catprod(i, j)
            if 9 < len(str(cp)):
                break
            elif is_pandigital(cp):
                if max_cp is None:
                    max_i, max_j, max_cp = i, j, cp
                elif max_cp < cp:
                    max_i, max_j, max_cp = i, j, cp
                # print 'updated: i=%d, j=%d, cp=%d' % (i, j, cp)

            j += 1

        i += 1
        if 5 < len(str(i)):
            break

    print 'max: i=%d, j=%d, cp=%d' % (max_i, max_j, max_cp)


if __name__ == '__main__':
    main()
