# -*- coding: utf-8 -*-

raw_data = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""


def load(data):
    lines = data.split('\n')
    rows = []
    for line in lines:
        line = line.strip()
        if line == '':
            continue
        row = [ int(n) for n in line.split() ]
        rows.append(row)
    return rows


def main():
    import pprint
    data = load(raw_data)

    max_cache = dict()
    for ri in xrange(len(data)):
        row = data[ri]
        for ci, n in enumerate(data[ri]):
            if ri == 0:
                max_cache[(ri, ci)] = n
            else:
                if ci == 0:
                    max_cache[(ri, ci)] = max_cache[(ri - 1, ci)] + n
                elif ci == len(data[ri]) - 1:
                    max_cache[(ri, ci)] = max_cache[(ri - 1, ci - 1)] + n
                else:
                    left_max = max_cache[(ri - 1, ci - 1)]
                    right_max = max_cache[(ri - 1, ci)]
                    max_cache[(ri, ci)] = max(left_max, right_max) + n

    last_row_idx = len(data) - 1
    last_row_length = len(data[last_row_idx])
    values = [ max_cache[(last_row_idx, ci)] for ci in xrange(last_row_length) ]
    max_value = max(values)
    # print '--------'
    print max_value
    # print '--------'
    # for ri, rdata in enumerate(data):
    #     print '%s' % ' '.join([ str(max_cache[(ri, ci)]) for ci in xrange(len(rdata))])


if __name__ == '__main__':
    main()
