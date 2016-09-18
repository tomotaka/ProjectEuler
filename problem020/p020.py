# -*- coding: utf-8 -*-
import math


def main():
    ans = 0
    for c in str(math.factorial(100)):
        ans += int(c)
    print ans


if __name__ == '__main__':
    main()
