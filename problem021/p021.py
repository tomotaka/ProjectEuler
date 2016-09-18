# -*- coding: utf-8 -*-


def factors(n):
    ret = [1]
    i = 2
    while i < n:
        if n % i == 0:
            ret.append(i)
        i += 1
    return ret


def d(n):
    return sum(factors(n))


def main():
    n_list = set([])
    i = 1

    while i < 10000:
        if i in n_list:
            print 'skip %d' % i
            i += 1
            continue

        d_v = d(i)
        d_d_v = d(d_v)

        if d_d_v == i:
            if d_v == i:
                i += 1
                continue
            n_list.add(i)
            n_list.add(d_v)
            print 'add %d and %d' % (i, d_v)

        i += 1

    print '-------------'
    print 'ans=%d' % sum(n_list)


if __name__ == '__main__':
    main()
