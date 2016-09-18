# -*- coding: utf-8 -*-
import datetime

WEEKDAYS = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')


def is_leapyear(y):
    if y % 400 == 0:
        return True
    elif y % 100 == 0:
        return False
    elif y % 4 == 0:
        return True
    else:
        return False


def day_of_month(y, m):
    if m == 2:
        if is_leapyear(y):
            return 29
        else:
            return 28
    elif m == 4 or m == 6 or m == 9 or m == 11:
        return 30
    else:
        return 31


def next_ym(y, m):
    if m == 12:
        return (y + 1, 1)
    else:
        return (y, m + 1)


def next_ymw(y, m, weekday_of_day1):
    next_y, next_m = next_ym(y, m)
    dom = day_of_month(y, m)
    add_day = dom
    next_w = (weekday_of_day1 + add_day) % 7
    return (next_y, next_m, next_w)


def main():
    # y1990, m2, w199002 = next_ym(1990, 1, 0)
    wd = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
    y, m, w = (1900, 1, 0)
    c = 0
    while True:
        y, m, w = next_ymw(y, m, w)
        # print '%04d/%02d/01 is %s / seikai=%d' % (y, m, w, datetime.date(y, m, 1).weekday())
        if w == 6:
            print '%04d/%02d/01 is Sunday' % (y, m)
            dt = datetime.date(y, m, 1)
            print 'seikai=%s' % dt.weekday()

            c += 1

        if y == 2000 and m == 12:
            break

    print '---------'
    print c






if __name__ == '__main__':
    main()
