# -*- coding: utf-8 -*-
t = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'
}


def s(n):
    if n == 1000:
        return 'one thousand'

    ret = ''

    if 100 <= n:
        h = n / 100
        ret += '%s hundred ' % t[h]

    n2 = n % 100
    if n2 == 0:
        return ret
    elif 100 <= n:
        ret += 'and '

    if (1 <= n2 and n2 <= 19) or n2 % 10 == 0:
        # print '-- n=%d n2=%d' % (n, n2)
        ret += t[n2]
    else:
        n3 = n2 - (n2 % 10)
        n4 = n2 % 10
        ret += '%s-%s' % (t[n3], t[n4])

    return ret


def main():
    count = 0
    for i in xrange(1, 1000 + 1):
        si = s(i)
        si = si.replace('-', '')
        si = si.replace(' ', '')
        # print '%d %s' % (i, si)
        count += len(si)
    print count


if __name__ == '__main__':
    main()
