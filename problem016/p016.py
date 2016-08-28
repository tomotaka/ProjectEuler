# -*- coding: utf-8 -*-


def main():
    n = 2 ** 1000
    print sum([ int(c) for c in str(n) ])


if __name__ == '__main__':
    main()
